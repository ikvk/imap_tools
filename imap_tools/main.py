# INTERNET MESSAGE ACCESS PROTOCOL - VERSION 4rev1 - https://tools.ietf.org/html/rfc3501
import re
import email
import imaplib
from email.header import decode_header
from . import imap_utf7

# Maximal line length when calling readline(). This is to prevent reading arbitrary length lines.
imaplib._MAXLINE = 4 * 1024 * 1024  # 4Mb


class ImapToolsError(Exception):
    """Base exception"""


class MailBox(object):
    """Working with the email box throught IMAP"""
    # for specify custom class
    email_message_class = None
    folder_manager_class = None

    class StandardMessageFlags(object):
        """Standard email message flags"""
        SEEN = 'SEEN'
        ANSWERED = 'ANSWERED'
        FLAGGED = 'FLAGGED'
        DELETED = 'DELETED'
        DRAFT = 'DRAFT'
        RECENT = 'RECENT'
        all = (
            SEEN, ANSWERED, FLAGGED, DELETED, DRAFT, RECENT
        )

    class MailBoxWrongFlagError(ImapToolsError):
        """Wrong flag for "flag" method"""

    class MailBoxUidParamError(ImapToolsError):
        """Wrong uid param"""

    def __init__(self, *args):
        self.box = imaplib.IMAP4_SSL(*args)
        self._box_args = args
        self._username = None
        self._password = None
        self._initial_folder = None
        self.folder = None

    @staticmethod
    def check_status(command, command_result, expected='OK'):
        """
        Check that command responses status equals <expected> status
        If not, raises ImapToolsError
        """
        typ, data = command_result[0], command_result[1]
        if typ != expected:
            raise ImapToolsError(
                'Response status for command "{command}" = "{typ}", "{exp}" expected, data: {data}'.format(
                    command=command, typ=typ, data=str(data), exp=expected))

    def login(self, username: str, password: str, initial_folder: str = 'INBOX'):
        self._username = username
        self._password = password
        self._initial_folder = initial_folder
        result = self.box.login(self._username, self._password)
        self.check_status('box.login', result)
        used_folder_manager_class = self.folder_manager_class or MailFolderManager
        self.folder = used_folder_manager_class(self)
        self.folder.set(self._initial_folder)
        return result

    def logout(self):
        result = self.box.logout()
        self.check_status('box.logout', result, expected='BYE')
        return result

    def fetch(self, search_criteria: str = 'ALL', limit: int = None, miss_defect=True) -> iter:
        """
        Mail message generator in current folder by search criteria
        :param search_criteria: Message search criteria (see examples at ./doc/imap_search_criteria.txt)
        :param limit: limit on the number of read emails
        :param miss_defect: miss defect emails
        :return generator: MailMessage
        """
        search_result = self.box.search(None, search_criteria)
        self.check_status('box.search', search_result)
        used_email_message_class = self.email_message_class or MailMessage
        # first element is string with email numbers through the gap
        for i, message_id in enumerate(search_result[1][0].decode().split(' ') if search_result[1][0] else ()):
            if limit and i >= limit:
                break
            # get message by id
            fetch_result = self.box.fetch(message_id, "(RFC822 UID FLAGS)")
            self.check_status('box.fetch', fetch_result)
            mail_message = used_email_message_class(message_id, fetch_result[1])
            if miss_defect and mail_message.obj.defects:
                continue
            yield mail_message

    @staticmethod
    def _uid_str(uid_list: [str]) -> str:
        """Prepare list of uid for use in commands: delete/copy/move/seen"""
        if not uid_list:
            raise MailBox.MailBoxUidParamError('uid_list should be not empty')
        if type(uid_list) not in (list, tuple, set):
            raise MailBox.MailBoxUidParamError(
                'uid_list must be list|tuple|set of strings, {} found: {}'.format(type(uid_list), uid_list))
        return ','.join(uid_list)

    def expunge(self) -> tuple:
        result = self.box.expunge()
        self.check_status('box.expunge', result)
        return result

    def delete(self, uid_list: [str]) -> tuple:
        """Delete email messages"""
        store_result = self.box.uid('STORE', self._uid_str(uid_list), '+FLAGS', '(\Deleted)')
        self.check_status('box.delete', store_result)
        expunge_result = self.expunge()
        return store_result, expunge_result

    def copy(self, uid_list: [str], destination_folder: str) -> tuple:
        """Copy email messages into the specified folder"""
        result = self.box.uid('COPY', self._uid_str(uid_list), destination_folder)
        self.check_status('box.copy', result)
        return result

    def move(self, uid_list: [str], destination_folder: str) -> tuple:
        """Move email messages into the specified folder"""
        copy_result = self.copy(uid_list, destination_folder)
        delete_result = self.delete(uid_list)
        return copy_result, delete_result

    def flag(self, uid_list: [str], flag_set: [str], value: bool) -> tuple:
        """
        Set email flags
        Typical flags contains in MailBox.StandardMessageFlags.all
        """
        for flag_name in flag_set:
            if flag_name.upper() not in self.StandardMessageFlags.all:
                raise self.MailBoxWrongFlagError('Unsupported flag: {}'.format(flag_name))
        store_result = self.box.uid(
            'STORE', self._uid_str(uid_list), ('+' if value else '-') + 'FLAGS',
            '({})'.format(' '.join(('\\' + i for i in flag_set))))
        self.check_status('box.flag', store_result)
        expunge_result = self.expunge()
        return store_result, expunge_result

    def seen(self, uid_list: [str], seen_val: bool) -> tuple:
        """
        Mark email as read/unread
        This is shortcut for flag method
        """
        return self.flag(uid_list, self.StandardMessageFlags.SEEN, seen_val)


class MailMessage(object):
    """The email message"""

    # UID parse rules
    pattern_uid_re_set = [
        re.compile('\(UID (?P<uid>\d+) RFC822'),  # zimbra, yandex, gmail
        re.compile('(?P<uid>\d+) \(RFC822'),  # icewarp
    ]

    def __init__(self, message_id: str, fetch_data):
        message_data, uid_data, flag_data = self._clean_message_data(fetch_data)
        self.id = message_id
        self.obj = email.message_from_bytes(message_data)
        self._uid_data = uid_data
        self._flag_data = flag_data

    @staticmethod
    def _clean_message_data(fetch_data):
        """
        :param fetch_data: Message object model
        :returns [message_data: bytes, uid_data: bytes, flag_data: list]
        *Elements may contain byte strings in any order, like: b'4517 (FLAGS (\\Recent NonJunk))'
        """
        message_data = b''
        uid_data = b''
        flag_data = []
        for fetch_item in fetch_data:
            # flags
            if type(fetch_item) is bytes and imaplib.ParseFlags(fetch_item):
                flag_data.extend(imaplib.ParseFlags(fetch_item))
            # data, uid
            if type(fetch_item) is tuple:
                uid_data = fetch_item[0]
                message_data = fetch_item[1]
        return message_data, uid_data, flag_data

    @staticmethod
    def _decode_value(value, encoding):
        """Converts value to utf-8 encoding"""
        if isinstance(value, bytes):
            if encoding in ['utf-8', None]:
                return value.decode('utf-8', 'ignore')
            else:
                return value.decode(encoding)
        return value

    @property
    def uid(self) -> str or None:
        """Message UID"""
        for pattern_uid_re in MailMessage.pattern_uid_re_set:
            uid_match = pattern_uid_re.search(self._uid_data.decode())
            if uid_match:
                return uid_match.group('uid')
        return None

    @property
    def flags(self) -> list:
        """
        Message flags
        *This attribute will not be changed after actions: flag, seen
        """
        return [i.decode().strip().replace('\\', '').upper() for i in self._flag_data]

    @property
    def subject(self) -> str:
        """Message subject"""
        if 'subject' in self.obj:
            msg_subject = decode_header(self.obj['subject'])
            return self._decode_value(msg_subject[0][0], msg_subject[0][1])
        return ''

    @staticmethod
    def _parse_email_address(address: str) -> dict:
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
        msg_txt = ''.join(self._decode_value(part[0], part[1]) for part in msg_from)
        return self._parse_email_address(msg_txt)

    @property
    def from_(self) -> str:
        """The address of the sender"""
        return self.from_values['email']

    @property
    def to_values(self) -> list:
        """The addresses of the recipients (all data)"""
        if 'to' in self.obj:
            msg_to = decode_header(self.obj['to'])
            return [self._parse_email_address(part) for part in
                    self._decode_value(msg_to[0][0], msg_to[0][1]).split(',')]
        return []

    @property
    def to(self) -> list:
        """The addresses of the recipients"""
        return [i['email'] for i in self.to_values]

    @property
    def date(self) -> str:
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

    def get_attachments(self) -> iter:
        """
        Attachments of the mail message (generator)
        :return: generator of tuple(filename: str, payload: bytes)
        """
        for part in self.obj.walk():
            # multipart/* are just containers
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue
            filename = part.get_filename()
            if not part.get_filename():
                continue  # this is what happens when Content-Disposition = inline
            filename = self._decode_value(*decode_header(filename)[0])
            payload = part.get_payload(decode=True)
            if not payload:
                continue
            yield filename, payload


class MailFolderManager(object):
    """Operations with mail box folders"""

    folder_status_options = ['MESSAGES', 'RECENT', 'UIDNEXT', 'UIDVALIDITY', 'UNSEEN']

    class MailBoxFolderWrongStatusError(ImapToolsError):
        """Wrong folder name error"""

    def __init__(self, mailbox):
        self.mailbox = mailbox
        self._current_folder = None

    def _normalise_folder(self, folder):
        """Normalise folder name"""
        if isinstance(folder, bytes):
            folder = folder.decode('ascii')
        return self._quote(imap_utf7.encode(folder))

    @staticmethod
    def _quote(arg):
        if isinstance(arg, str):
            return '"' + arg.replace('\\', '\\\\').replace('"', '\\"') + '"'
        else:
            return b'"' + arg.replace(b'\\', b'\\\\').replace(b'"', b'\\"') + b'"'

    @staticmethod
    def _pairs_to_dict(items: list) -> dict:
        """Example: ['MESSAGES', '3', 'UIDNEXT', '4'] -> {'MESSAGES': '3', 'UIDNEXT': '4'}"""
        if len(items) % 2 != 0:
            raise ValueError('An even-length array is expected')
        return dict((items[i * 2], items[i * 2 + 1]) for i in range(len(items) // 2))

    def set(self, folder):
        """Select current folder"""
        result = self.mailbox.box.select(folder)
        self.mailbox.check_status('box.select', result)
        self._current_folder = folder
        return result

    def exists(self, folder: str) -> bool:
        """Checks whether a folder exists on the server."""
        return len(self.list('', folder)) > 0

    def create(self, folder: str):
        """
        Create folder on the server. D
        *Use email box delimitor to separate folders. Example for "|" delimitor: "folder|sub folder"
        """
        result = self.mailbox.box._simple_command('CREATE', self._normalise_folder(folder))
        self.mailbox.check_status('CREATE', result)
        return result

    def get(self):
        """Get current folder"""
        return self._current_folder

    def rename(self, old_name: str, new_name: str):
        """Renemae folder from old_name to new_name"""
        result = self.mailbox.box._simple_command(
            'RENAME', self._normalise_folder(old_name), self._normalise_folder(new_name))
        self.mailbox.check_status('RENAME', result)
        return result

    def delete(self, folder: str):
        """Delete folder"""
        result = self.mailbox.box._simple_command('DELETE', self._normalise_folder(folder))
        self.mailbox.check_status('DELETE', result)
        return result

    def status(self, folder: str, options: [str] or None = None) -> dict:
        """
        Get the status of a folder
        :param folder: mailbox folder
        :param options: [str] with values from MailFolderManager.folder_status_options or None,
                by default - get all options
            MESSAGES - The number of messages in the mailbox.
            RECENT - The number of messages with the \Recent flag set.
            UIDNEXT - The next unique identifier value of the mailbox.
            UIDVALIDITY - The unique identifier validity value of the mailbox.
            UNSEEN - The number of messages which do not have the \Seen flag set.
        :return: dict with available options keys
        """
        command = 'STATUS'
        if not options:
            options = self.folder_status_options
        if not all([i in self.folder_status_options for i in options]):
            raise self.MailBoxFolderWrongStatusError(str(options))
        status_result = self.mailbox.box._simple_command(
            command, self._normalise_folder(folder), '({})'.format(' '.join(options)))
        self.mailbox.check_status(command, status_result)
        result = self.mailbox.box._untagged_response(status_result[0], status_result[1], command)
        self.mailbox.check_status(command, result)
        values = result[1][0].decode().split('(')[1].split(')')[0].split(' ')
        return self._pairs_to_dict(values)

    def list(self, folder: str = '', search_args: str = '*', subscribed_only: bool = False) -> list:
        """
        Get a listing of folders on the server
        :param folder: mailbox folder, if empty list shows all content from root
        :param search_args: search argumets, is case-sensitive mailbox name with possible wildcards
            * is a wildcard, and matches zero or more characters at this position
            % is similar to * but it does not match a hierarchy delimiter
        :param subscribed_only: bool - get only subscribed folders
        :return: [dict(
            flags: str - folder flags,
            delim: str - delimitor,
            name: str - folder name,
        )]
        """
        folder_item_re = re.compile(r'\((?P<flags>[\S ]*)\) "(?P<delim>[\S ]+)" (?P<name>.+)')
        command = 'LSUB' if subscribed_only else 'LIST'
        typ, data = self.mailbox.box._simple_command(command, self._normalise_folder(folder), search_args)
        typ, data = self.mailbox.box._untagged_response(typ, data, command)
        result = list()
        for folder_item in data:
            if not folder_item:
                continue
            folder_match = re.search(folder_item_re, imap_utf7.decode(folder_item))
            folder = folder_match.groupdict()
            if folder['name'].startswith('"') and folder['name'].endswith('"'):
                folder['name'] = folder['name'][1:len(folder['name']) - 1]
            result.append(folder)
        return result
