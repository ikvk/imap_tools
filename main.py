import re
import email
import imaplib
import datetime
from typing import Iterable
from email.header import decode_header

# Maximal line length when calling readline(). This is to prevent reading arbitrary length lines.
imaplib._MAXLINE = 4 * 1024 * 1024  # 4Mb


class MailBox(object):
    """The mail box"""

    # UID parse rules
    pattern_uid_re_set = [
        re.compile('\(UID (?P<uid>\d+) RFC822'),  # zimbra, yandex, gmail
        re.compile('(?P<uid>\d+) \(RFC822'),  # icewarp
    ]

    # some search criteria
    criteria_unseen = 'UNSEEN'
    criteria_seen = 'SEEN'
    criteria_all = 'ALL'

    # standard mail message flags
    standard_rw_flags = ('SEEN', 'ANSWERED', 'FLAGGED', 'DELETED', 'DRAFT')

    class MailBoxError(Exception):
        """Base exception"""

    class MailBoxFolderError(MailBoxError):
        """Wrong folder name error"""

    class MailBoxSearchError(MailBoxError):
        """Search error"""

    def __init__(self, *args):
        self.box = imaplib.IMAP4_SSL(*args)

    def login(self, username: str, password: str, initial_folder: str = 'INBOX'):
        self._username = username
        self._password = password
        self._initial_folder = initial_folder
        result = self.box.login(self._username, self._password)
        self.set_folder(self._initial_folder)
        # self.folder = MailFolderManager()
        return result

    def set_folder(self, folder):
        """Select current folder"""
        res = self.box.select(folder)
        if res[0] != 'OK':
            raise self.MailBoxFolderError(res[1])

    @staticmethod
    def parse_uid(data: bytes) -> str or None:
        for pattern_uid_re in MailBox.pattern_uid_re_set:
            uid_match = pattern_uid_re.search(data.decode())
            if uid_match:
                return uid_match.group('uid')
        return None

    @staticmethod
    def clean_message_data(data):
        """
        Get message data and uid data
        *Elements may contain byte strings in any order, like: b'4517 (FLAGS (\\Recent NonJunk))'
        """
        message_data = b''
        uid_data = b''
        for i in range(len(data)):
            # miss trash
            if type(data[i]) is bytes and b'(FLAGS' in data[i]:
                continue
            # data, uid
            if type(data[i]) is tuple:
                message_data = data[i][1]
                uid_data = data[i][0]

        return message_data, uid_data

    def fetch(self, search_criteria: str = None, limit: int = None, miss_defect=True) -> Iterable:
        """
        Mail message generator in current folder by search criteria
        :param search_criteria: Message search criteria (see examples at ./doc/imap_search_criteria.txt)
        :param limit: limit on the number of read emails
        :param miss_defect: miss defect emails
        """
        typ, data = self.box.search(None, search_criteria or self.criteria_all)
        if typ != 'OK':
            raise self.MailBoxSearchError('{0}: {1}'.format(typ, str(data)))
        # first element is string with email numbers through the gap
        message_id_set = data[0].decode().split(' ') if data[0] else ()
        for i, message_id in enumerate(message_id_set):
            if limit and i >= limit:
                break
            # get message by id
            typ, data = self.box.fetch(message_id, "(RFC822 UID)")  # *RFC-822 - format of the mail message
            message_data, uid_data = self.clean_message_data(data)
            message_obj = email.message_from_bytes(message_data)
            if message_obj:
                if not message_obj.defects or not miss_defect:  # miss defect emails
                    yield MailMessage(message_id, self.parse_uid(uid_data), message_obj)

    @staticmethod
    def parse_uid_arg(message_uid_arg: str or [str]) -> str:
        """
        Prepare list of uid for use in commands: delete/copy/move/seen
        """
        if not message_uid_arg:
            raise ValueError('message_uid_arg should not be empty')
        elif type(message_uid_arg) is list:
            return ','.join(message_uid_arg)
        elif type(message_uid_arg) is str:
            return message_uid_arg
        else:
            raise TypeError('str or list expected, {} given'.format(type(message_uid_arg)))

    def logout(self) -> tuple:
        return self.box.logout()

    def delete(self, message_uid_arg: str or [str], do_expunge: bool = True) -> bool:
        """
        Delete (email message/group of email messages)
        The most effective way: group - to pass a list of uid, a single method - pass the uid
        """
        if not message_uid_arg:
            return True
        store_result = self.box.uid('STORE', self.parse_uid_arg(message_uid_arg), '+FLAGS', '(\Deleted)')
        result = store_result[0] == 'OK'
        if result and do_expunge:
            self.expunge()
        return result

    def copy(self, message_uid_arg: str or [str], destination_folder: str, do_expunge: bool = True) -> bool:
        """
        Copy (email message/group of email messages) into the specified folder
        The most effective way: group - to pass a list of uid, a single method - pass the uid
        """
        if not message_uid_arg:
            return True
        copy_result = self.box.uid('COPY', self.parse_uid_arg(message_uid_arg), destination_folder)
        result = copy_result[0] == 'OK'
        if result and do_expunge:
            self.expunge()
        return result

    def move(self, message_uid_arg: str or [str], destination_folder: str, do_expunge: bool = True) -> bool:
        """
        Move (email message/group of email messages) into the specified folder
        The most effective way: group - to pass a list of uid, a single method - pass the uid
        """
        if not message_uid_arg:
            return True
        result = False
        uid_arg = self.parse_uid_arg(message_uid_arg)
        copy_result = self.copy(uid_arg, destination_folder, do_expunge=False)
        if copy_result:
            result = self.delete(uid_arg, do_expunge=False)
            if result and do_expunge:
                self.expunge()
        return result

    def flag(self, message_uid_arg: str or [str], flag_set: [str] or str, value: bool, do_expunge: bool = True) -> bool:
        """
        Change email flag
        Typical flags contains in MailBox.standard_rw_flags
        The most effective way: group - to pass a list of uid, a single method - pass the uid
        """
        flag_set = [flag_set] if type(flag_set) is str else flag_set
        for flag_name in flag_set:
            if flag_name.upper() not in self.standard_rw_flags:
                raise TypeError('Unsupported flag: {}'.format(flag_name))
        if not message_uid_arg:
            return True
        store_result = self.box.uid('STORE', self.parse_uid_arg(message_uid_arg), ('+' if value else '-') + 'FLAGS',
                                    '({})'.format(' '.join(('\\' + i for i in flag_set))))
        result = store_result[0] == 'OK'
        if result and do_expunge:
            self.expunge()
        return result

    def seen(self, message_uid_arg: str or [str], seen_val: bool, do_expunge: bool = True) -> bool:
        """
        Mark email as read/unread
        This is shortcut for flag method
        The most effective way: group - to pass a list of uid, a single method - pass the uid
        """
        return self.flag(message_uid_arg, 'Seen', seen_val, do_expunge)

    def expunge(self) -> tuple:
        """
        Remove any messages from the currently selected folder that have the \Deleted flag set.
        *Generates an EXPUNGE response for each deleted message.
        *Returned data contains a list of EXPUNGE message numbers in order received.
        """
        return self.box.expunge()


class MailMessage(object):
    """The email message"""

    def __init__(self, msg_id: str, msg_uid: str, msg_obj: 'email.message.Message'):
        self.id = msg_id
        self.uid = msg_uid
        self.obj = msg_obj

    @staticmethod
    def decode_value(value, encoding):
        """Converts value to utf-8 encoding"""
        if isinstance(value, bytes):
            if encoding in ['utf-8', None]:
                return value.decode('utf-8', 'ignore')
            else:
                return value.decode(encoding)
        return value

    @property
    def subject(self) -> str:
        """Message subject"""
        if 'subject' in self.obj:
            msg_subject = decode_header(self.obj['subject'])
            return self.decode_value(msg_subject[0][0], msg_subject[0][1])
        return ''

    @staticmethod
    def parse_email_address(address: str) -> dict:
        """
        Parse email address str, example: "Ivan Petrov" <ivan@mail.ru>
        @:return dict(name: str, email: str, full: str)
        """
        result = dict(email='', name='', full='')
        if '<' in address and '>' in address:
            match = re.match('(?P<name>.*)?(?P<email><.*>)', address, re.UNICODE)
            result['name'] = match.group('name').strip()
            result['email'] = match.group('email').strip('<>')
            result['full'] = address
        else:
            result['name'] = ''
            result['email'] = result['full'] = address.strip()
        return result

    @property
    def from_values(self) -> dict:
        """The address of the sender (all data)"""
        from_header_cleaned = re.sub('[\n\r\t]+', ' ', self.obj['from'])
        msg_from = decode_header(from_header_cleaned)
        msg_txt = ''.join(self.decode_value(part[0], part[1]) for part in msg_from)
        return self.parse_email_address(msg_txt)

    @property
    def from_(self) -> str:
        """The address of the sender"""
        return self.from_values['email']

    @property
    def to_values(self) -> list:
        """The addresses of the recipients (all data)"""
        if 'to' in self.obj:
            msg_to = decode_header(self.obj['to'])
            return [self.parse_email_address(part) for part in self.decode_value(msg_to[0][0], msg_to[0][1]).split(',')]
        return []

    @property
    def to(self) -> list:
        """The addresses of the recipients"""
        return [i['email'] for i in self.to_values]

    @property
    def date(self) -> datetime.datetime or None:
        """Message date"""
        if self.obj['Date']:
            return datetime.datetime.strptime(
                self.obj['Date'].split(', ')[-1].split(' (')[0], "%d %b %Y %H:%M:%S %z")
        return None

    @property
    def date_str(self) -> str:
        """Message date"""
        return str(self.obj['Date'] or '')

    @property
    def text(self) -> str or None:
        """The text of the mail message"""
        for part in self.obj.walk():
            # multipart/* are just containers
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get_content_type() in ('text/plain', 'text/'):
                return part.get_payload(decode=True).decode('utf-8', 'ignore')
        return None

    @property
    def html(self) -> str or None:
        """HTML text of the mail message"""
        for part in self.obj.walk():
            # multipart/* are just containers
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get_content_type() == 'text/html':
                return part.get_payload(decode=True).decode('utf-8', 'ignore')
        return None

    def get_attachments(self) -> Iterable(str, bytes):
        """Attachments of the mail message (generator)"""
        for part in self.obj.walk():
            # multipart/* are just containers
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue
            filename = part.get_filename()
            if not part.get_filename():
                continue  # this is what happens when Content-Disposition = inline
            filename = self.decode_value(*decode_header(filename)[0])
            payload = part.get_payload(decode=True)
            if not payload:
                continue
            yield filename, payload


class MailFolderManager(object):
    """operations with mail box folders"""

    # todo

    def get(self):
        pass

    def create(self):
        pass

    def rename(self):
        pass

    def status(self):
        pass

    def delete(self):
        pass

    def get_list(self):
        pass

    def get_sub_list(self):
        pass
