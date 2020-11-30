import sys
import imaplib
from email.errors import StartBoundaryNotFoundDefect, MultipartInvariantViolationDefect

from .message import MailMessage, MailMessageFlags
from .folder import MailBoxFolderManager
from .utils import cleaned_uid_set, check_command_status, chunks, encode_folder
from .errors import MailboxStarttlsError, MailboxLoginError, MailboxLogoutError, MailboxSearchError, \
    MailboxFetchError, MailboxExpungeError, MailboxDeleteError, MailboxCopyError, MailboxFlagError

# Maximal line length when calling readline(). This is to prevent reading arbitrary length lines.
imaplib._MAXLINE = 4 * 1024 * 1024  # 4Mb


class BaseMailBox:
    """Working with the email box"""

    email_message_class = MailMessage
    folder_manager_class = MailBoxFolderManager
    with_headers_only_allowed_errors = (StartBoundaryNotFoundDefect, MultipartInvariantViolationDefect)
    timeout_not_supported_error = 'timeout argument supported since python 3.9'

    def __init__(self):
        self.folder = None  # folder manager
        self.login_result = None
        self.box = self._get_mailbox_client()

    def _get_mailbox_client(self) -> imaplib.IMAP4:
        raise NotImplementedError

    def login(self, username: str, password: str, initial_folder: str or None = 'INBOX'):
        login_result = self.box.login(username, password)
        check_command_status(login_result, MailboxLoginError)
        special = ['163.com', '126.com', 'yeah.net']
        if any(w in username and w for w in special):
            imaplib.Commands['ID'] = ('AUTH')
            args = ("name", "hsu1943", "contact", "osnail1943@gmail.com", "version", "1.0.0", "vendor", "hsu1943")
            id_result = self.box._simple_command('ID', '("' + '" "'.join(args) + '")')
            print(id_result)
            check_command_status(id_result, MailboxLoginError)
        self.folder = self.folder_manager_class(self)
        if initial_folder is not None:
            self.folder.set(initial_folder)
        self.login_result = login_result
        return self  # return self in favor of context manager

    def logout(self):
        result = self.box.logout()
        check_command_status(result, MailboxLogoutError, expected='BYE')
        return result

    def search(self, criteria: str or bytes = 'ALL', charset: str = 'US-ASCII') -> [str]:
        """
        Search mailbox for matching message numbers (this is not uids)
        :param criteria: message search criteria (see examples at ./doc/imap_search_criteria.txt)
        :param charset: IANA charset, indicates charset of the strings that appear in the search criteria. See rfc2978
        :return list of str
        """
        encoded_criteria = criteria if type(criteria) is bytes else str(criteria).encode(charset)
        search_result = self.box.search(charset, encoded_criteria)
        check_command_status(search_result, MailboxSearchError)
        return search_result[1][0].decode().split(' ') if search_result[1][0] else []

    def _fetch_by_one(self, message_nums: [str], message_parts: str, reverse: bool) -> iter:  # noqa
        for message_num in message_nums:
            fetch_result = self.box.fetch(message_num, message_parts)
            check_command_status(fetch_result, MailboxFetchError)
            yield fetch_result[1]

    def _fetch_in_bulk(self, message_nums: [str], message_parts: str, reverse: bool) -> iter:
        if not message_nums:
            return
        fetch_result = self.box.fetch(','.join(message_nums), message_parts)
        check_command_status(fetch_result, MailboxFetchError)
        for built_fetch_item in chunks((reversed if reverse else iter)(fetch_result[1]), 2):
            yield built_fetch_item

    def fetch(self, criteria: str or bytes = 'ALL', charset: str = 'US-ASCII', limit: int or slice = None,
              miss_defect=True, miss_no_uid=True, mark_seen=True, reverse=False, headers_only=False,
              bulk=False) -> iter:
        """
        Mail message generator in current folder by search criteria
        :param criteria: message search criteria (see examples at ./doc/imap_search_criteria.txt)
        :param charset: IANA charset, indicates charset of the strings that appear in the search criteria. See rfc2978
        :param limit: int | slice - limit number of read emails | slice emails range for read
                      useful for actions with a large number of messages, like "move" | paging
        :param miss_defect: miss emails with defects
        :param miss_no_uid: miss emails without uid
        :param mark_seen: mark emails as seen on fetch
        :param reverse: in order from the larger date to the smaller
        :param headers_only: get only email headers (without text, html, attachments)
        :param bulk: False - fetch each message separately per N commands - low memory consumption, slow
                     True  - fetch all messages per 1 command - high memory consumption, fast
        :return generator: MailMessage
        """
        message_parts = "(BODY{}[{}] UID FLAGS RFC822.SIZE)".format(
            '' if mark_seen else '.PEEK', 'HEADER' if headers_only else '')
        limit_range = slice(0, limit) if type(limit) is int else limit or slice(None)
        assert type(limit_range) is slice
        nums = tuple((reversed if reverse else iter)(self.search(criteria, charset)))[limit_range]
        for fetch_item in (self._fetch_in_bulk if bulk else self._fetch_by_one)(nums, message_parts, reverse):  # noqa
            mail_message = self.email_message_class(fetch_item)
            if miss_defect and mail_message.obj.defects:
                if headers_only:
                    if not all(d.__class__ in self.with_headers_only_allowed_errors for d in mail_message.obj.defects):
                        continue
                else:
                    continue
            if miss_no_uid and not mail_message.uid:
                continue
            yield mail_message

    def expunge(self) -> tuple:
        result = self.box.expunge()
        check_command_status(result, MailboxExpungeError)
        return result

    def delete(self, uid_list) -> (tuple, tuple) or None:
        """
        Delete email messages
        Do nothing on empty uid_list
        :return: None on empty uid_list, command results otherwise
        """
        uid_str = cleaned_uid_set(uid_list)
        if not uid_str:
            return None
        store_result = self.box.uid('STORE', uid_str, '+FLAGS', r'(\Deleted)')
        check_command_status(store_result, MailboxDeleteError)
        expunge_result = self.expunge()
        return store_result, expunge_result

    def copy(self, uid_list, destination_folder: str or bytes) -> tuple or None:
        """
        Copy email messages into the specified folder
        Do nothing on empty uid_list
        :return: None on empty uid_list, command results otherwise
        """
        uid_str = cleaned_uid_set(uid_list)
        if not uid_str:
            return None
        copy_result = self.box.uid('COPY', uid_str, encode_folder(destination_folder))  # noqa
        check_command_status(copy_result, MailboxCopyError)
        return copy_result

    def move(self, uid_list, destination_folder: str or bytes) -> (tuple, tuple) or None:
        """
        Move email messages into the specified folder
        Do nothing on empty uid_list
        :return: None on empty uid_list, command results otherwise
        """
        # here for avoid double fetch in uid_set
        uid_str = cleaned_uid_set(uid_list)
        if not uid_str:
            return None
        copy_result = self.copy(uid_str, destination_folder)
        delete_result = self.delete(uid_str)
        return copy_result, delete_result

    def flag(self, uid_list, flag_set: [str] or str, value: bool) -> (tuple, tuple) or None:
        """
        Set/unset email flags
        Do nothing on empty uid_list
        Standard flags contains in message.MailMessageFlags.all
        :return: None on empty uid_list, command results otherwise
        """
        uid_str = cleaned_uid_set(uid_list)
        if not uid_str:
            return None
        if type(flag_set) is str:
            flag_set = [flag_set]
        store_result = self.box.uid(
            'STORE', uid_str, ('+' if value else '-') + 'FLAGS',
            '({})'.format(' '.join(('\\' + i for i in flag_set))))
        check_command_status(store_result, MailboxFlagError)
        expunge_result = self.expunge()
        return store_result, expunge_result

    def seen(self, uid_list, seen_val: bool) -> (tuple, tuple) or None:
        """
        Mark email as read/unread
        This is shortcut for flag method
        """
        return self.flag(uid_list, MailMessageFlags.SEEN, seen_val)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.logout()


class MailBoxUnencrypted(BaseMailBox):
    """Working with the email box through IMAP4"""

    def __init__(self, host='', port=143, timeout=None):
        """
        :param host: host's name (default: localhost)
        :param port: port number
        :param timeout: timeout in seconds for the connection attempt, since python 3.9
        """
        if timeout and sys.version_info.minor < 9:
            raise ValueError(self.timeout_not_supported_error)
        self._host = host
        self._port = port
        self._timeout = timeout
        super().__init__()

    def _get_mailbox_client(self):
        if sys.version_info.minor < 9:
            return imaplib.IMAP4(self._host, self._port)
        else:
            return imaplib.IMAP4(self._host, self._port, self._timeout)  # noqa


class MailBox(BaseMailBox):
    """Working with the email box through IMAP4 over SSL connection"""

    def __init__(self, host='', port=993, timeout=None, keyfile=None, certfile=None, ssl_context=None, starttls=False):
        """
        :param host: host's name (default: localhost)
        :param port: port number
        :param timeout: timeout in seconds for the connection attempt, since python 3.9
        :param keyfile: PEM formatted file that contains your private key (deprecated)
        :param certfile: PEM formatted certificate chain file (deprecated)
        :param ssl_context: SSLContext object that contains your certificate chain and private key
        :param starttls: whether to use starttls
        """
        if timeout and sys.version_info.minor < 9:
            raise ValueError(self.timeout_not_supported_error)
        self._host = host
        self._port = port
        self._timeout = timeout
        self._keyfile = keyfile
        self._certfile = certfile
        self._ssl_context = ssl_context
        self._starttls = starttls
        super().__init__()

    def _get_mailbox_client(self):
        if self._starttls:
            if self._keyfile or self._certfile:
                raise ValueError("starttls cannot be combined with keyfile neither with certfile.")
            if sys.version_info.minor < 9:
                client = imaplib.IMAP4(self._host, self._port)
            else:
                client = imaplib.IMAP4(self._host, self._port, self._timeout)  # noqa
            result = client.starttls(self._ssl_context)
            check_command_status(result, MailboxStarttlsError)
            return client
        else:
            if sys.version_info.minor < 9:
                return imaplib.IMAP4_SSL(self._host, self._port, self._keyfile, self._certfile, self._ssl_context)
            else:
                return imaplib.IMAP4_SSL(self._host, self._port, self._keyfile,  # noqa
                                         self._certfile, self._ssl_context, self._timeout)

    def xoauth2(self, username: str, access_token: str, initial_folder: str = 'INBOX'):
        """Authenticate to account using OAuth 2.0 mechanism"""
        auth_string = 'user={}\1auth=Bearer {}\1\1'.format(username, access_token)
        result = self.box.authenticate('XOAUTH2', lambda x: auth_string)  # noqa
        check_command_status(result, MailboxLoginError)
        self.folder = self.folder_manager_class(self)
        self.folder.set(initial_folder)
        self.login_result = result
        return self
