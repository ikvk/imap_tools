import imaplib

from .message import MailMessage
from .folder import MailBoxFolderManager
from .utils import cleaned_uid_set

# Maximal line length when calling readline(). This is to prevent reading arbitrary length lines.
imaplib._MAXLINE = 4 * 1024 * 1024  # 4Mb


class MailBoxUnexpectedStatusError(Exception):
    """Unexpected status in response"""


class StandardMessageFlags:
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


class MailBox:
    """Working with the email box through IMAP4"""

    email_message_class = MailMessage
    folder_manager_class = MailBoxFolderManager

    def __init__(self, host='', port=None, ssl=True, keyfile=None, certfile=None, ssl_context=None):
        """
        :param host: host's name (default: localhost)
        :param port: port number (default: standard IMAP4 SSL port)
        :param ssl: use client class over SSL connection (IMAP4_SSL) if True, else use IMAP4
        :param keyfile: PEM formatted file that contains your private key (default: None)
        :param certfile: PEM formatted certificate chain file (default: None)
        :param ssl_context: SSLContext object that contains your certificate chain and private key (default: None)
        Note: if ssl_context is provided, then parameters keyfile or
              certfile should not be set otherwise ValueError is raised.
        """
        self._host = host
        self._port = port
        self._keyfile = keyfile
        self._certfile = certfile
        self._ssl_context = ssl_context
        if ssl:
            self.box = imaplib.IMAP4_SSL(
                host, port or imaplib.IMAP4_SSL_PORT, keyfile, certfile, ssl_context)
        else:
            self.box = imaplib.IMAP4(host, port or imaplib.IMAP4_PORT)
        self._username = None
        self._password = None
        self._initial_folder = None
        self.folder = None
        self.login_result = None

    @staticmethod
    def check_status(command, command_result, expected='OK'):
        """
        Check that command responses status equals <expected> status
        If not, raises MailBoxUnexpectedStatusError
        """
        typ, data = command_result[0], command_result[1]
        if typ != expected:
            raise MailBoxUnexpectedStatusError(
                'Response status for command "{command}" == "{typ}", "{exp}" expected, data: {data}'.format(
                    command=command, typ=typ, data=str(data), exp=expected))

    def login(self, username: str, password: str, initial_folder: str = 'INBOX'):
        self._username = username
        self._password = password
        self._initial_folder = initial_folder
        result = self.box.login(self._username, self._password)
        self.check_status('box.login', result)
        self.folder = self.folder_manager_class(self)
        self.folder.set(self._initial_folder)
        self.login_result = result
        return self  # return self in favor of context manager

    def logout(self):
        result = self.box.logout()
        self.check_status('box.logout', result, expected='BYE')
        return result

    def fetch(self, search_criteria: str = 'ALL', charset: str = 'US-ASCII', limit: int = None,
              miss_defect=True, miss_no_uid=True, mark_seen=True) -> iter:
        """
        Mail message generator in current folder by search criteria
        :param search_criteria: message search criteria (see examples at ./doc/imap_search_criteria.txt)
        :param charset: IANA charset, indicates charset of the strings that appear in the search criteria. See rfc2978
        :param limit: limit number of read emails, useful for actions with a large number of messages, like "move"
        :param miss_defect: miss emails with defects
        :param miss_no_uid: miss emails without uid
        :param mark_seen: mark emails as seen on fetch
        :return generator: MailMessage
        """
        search_result = self.box.search(charset, search_criteria)
        self.check_status('box.search', search_result)
        # first element is string with email numbers through the gap
        for i, message_id in enumerate(search_result[1][0].decode().split(' ') if search_result[1][0] else ()):
            if limit and i >= limit:
                break
            # get message by id
            fetch_result = self.box.fetch(message_id, "(BODY[] UID FLAGS)" if mark_seen else "(BODY.PEEK[] UID FLAGS)")
            self.check_status('box.fetch', fetch_result)
            mail_message = self.email_message_class(message_id, fetch_result[1])
            if miss_defect and mail_message.obj.defects:
                continue
            if miss_no_uid and not mail_message.uid:
                continue
            yield mail_message

    def expunge(self) -> tuple:
        result = self.box.expunge()
        self.check_status('box.expunge', result)
        return result

    def delete(self, uid_list) -> tuple:
        """Delete email messages"""
        uid_str = cleaned_uid_set(uid_list)
        store_result = self.box.uid('STORE', uid_str, '+FLAGS', r'(\Deleted)')
        self.check_status('box.delete', store_result)
        expunge_result = self.expunge()
        return store_result, expunge_result

    def copy(self, uid_list, destination_folder: str) -> tuple or None:
        """Copy email messages into the specified folder"""
        uid_str = cleaned_uid_set(uid_list)
        copy_result = self.box.uid('COPY', uid_str, destination_folder)
        self.check_status('box.copy', copy_result)
        return copy_result

    def move(self, uid_list, destination_folder: str) -> tuple:
        """Move email messages into the specified folder"""
        # here for avoid double fetch in uid_set
        uid_str = cleaned_uid_set(uid_list)
        copy_result = self.copy(uid_str, destination_folder)
        delete_result = self.delete(uid_str)
        return copy_result, delete_result

    def flag(self, uid_list, flag_set: [str] or str, value: bool) -> tuple:
        """
        Set/unset email flags
        Standard flags contains in StandardMessageFlags.all
        """
        uid_str = cleaned_uid_set(uid_list)
        if type(flag_set) is str:
            flag_set = [flag_set]
        store_result = self.box.uid(
            'STORE', uid_str, ('+' if value else '-') + 'FLAGS',
            '({})'.format(' '.join(('\\' + i for i in flag_set))))
        self.check_status('box.flag', store_result)
        expunge_result = self.expunge()
        return store_result, expunge_result

    def seen(self, uid_list, seen_val: bool) -> tuple:
        """
        Mark email as read/unread
        This is shortcut for flag method
        """
        return self.flag(uid_list, StandardMessageFlags.SEEN, seen_val)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.logout()
