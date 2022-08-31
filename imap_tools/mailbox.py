import re
import sys
import imaplib
import datetime
from collections import UserString
from typing import AnyStr, Optional, List, Iterable, Sequence, Union, Tuple, Iterator

from .consts import UID_PATTERN
from .message import MailMessage
from .folder import MailBoxFolderManager
from .idle import IdleManager
from .utils import clean_uids, check_command_status, chunks, encode_folder, clean_flags, decode_value, \
    check_timeout_arg_support
from .errors import MailboxStarttlsError, MailboxLoginError, MailboxLogoutError, MailboxNumbersError, \
    MailboxFetchError, MailboxExpungeError, MailboxDeleteError, MailboxCopyError, MailboxFlagError, \
    MailboxAppendError, MailboxUidsError, MailboxTaggedResponseError

# Maximal line length when calling readline(). This is to prevent reading arbitrary length lines.
# 20Mb is enough for search response with about 2 000 000 message numbers
imaplib._MAXLINE = 20 * 1024 * 1024  # 20Mb

Criteria = Union[AnyStr, UserString]

PYTHON_VERSION_MINOR = sys.version_info.minor


class BaseMailBox:
    """Working with the email box"""

    email_message_class = MailMessage
    folder_manager_class = MailBoxFolderManager
    idle_manager_class = IdleManager

    def __init__(self):
        self.client = self._get_mailbox_client()
        self.folder = self.folder_manager_class(self)
        self.idle = self.idle_manager_class(self)
        self.login_result = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.logout()

    def _get_mailbox_client(self) -> imaplib.IMAP4:
        raise NotImplementedError

    def consume_until_tagged_response(self, tag: bytes):
        """Waiting for tagged response"""
        tagged_commands = self.client.tagged_commands
        response_set = []
        while True:
            response: bytes = self.client._get_response()  # noqa, example: b'IJDH3 OK IDLE Terminated'
            if tagged_commands[tag]:
                break
            response_set.append(response)
        result = tagged_commands.pop(tag)
        check_command_status(result, MailboxTaggedResponseError)
        return result, response_set

    def login(self, username: str, password: str, initial_folder: Optional[str] = 'INBOX') -> 'BaseMailBox':
        """Authenticate to account"""
        login_result = self.client._simple_command('LOGIN', username, self.client._quote(password))  # noqa
        check_command_status(login_result, MailboxLoginError)
        self.client.state = 'AUTH'  # logic from self.client.login
        if initial_folder is not None:
            self.folder.set(initial_folder)
        self.login_result = login_result
        return self  # return self in favor of context manager

    def login_utf8(self, username: str, password: str, initial_folder: Optional[str] = 'INBOX') -> 'BaseMailBox':
        """Authenticate to an account with a UTF-8 username and/or password"""
        # rfc2595 section 6 - PLAIN SASL mechanism
        encoded = (b"\0" + username.encode("utf8") + b"\0" + password.encode("utf8"))
        # Assumption is the server supports AUTH=PLAIN capability
        login_result = self.client.authenticate("PLAIN", lambda x: encoded)
        check_command_status(login_result, MailboxLoginError)
        if initial_folder is not None:
            self.folder.set(initial_folder)
        self.login_result = login_result
        return self

    def xoauth2(self, username: str, access_token: str, initial_folder: Optional[str] = 'INBOX') -> 'BaseMailBox':
        """Authenticate to account using OAuth 2.0 mechanism"""
        auth_string = 'user={}\1auth=Bearer {}\1\1'.format(username, access_token)
        result = self.client.authenticate('XOAUTH2', lambda x: auth_string)  # noqa
        check_command_status(result, MailboxLoginError)
        if initial_folder is not None:
            self.folder.set(initial_folder)
        self.login_result = result
        return self

    def logout(self) -> tuple:
        """Informs the server that the client is done with the connection"""
        result = self.client.logout()
        check_command_status(result, MailboxLogoutError, expected='BYE')
        return result

    def numbers(self, criteria: Criteria = 'ALL', charset: str = 'US-ASCII') -> List[str]:
        """
        Search mailbox for matching message numbers in current folder (this is not uids)
        :param criteria: message search criteria (see examples at ./doc/imap_search_criteria.txt)
        :param charset: IANA charset, indicates charset of the strings that appear in the search criteria. See rfc2978
        :return email message numbers
        """
        encoded_criteria = criteria if type(criteria) is bytes else str(criteria).encode(charset)
        search_result = self.client.search(charset, encoded_criteria)
        check_command_status(search_result, MailboxNumbersError)
        return search_result[1][0].decode().split() if search_result[1][0] else []

    def uids(self, criteria: Criteria = 'ALL', charset: str = 'US-ASCII', miss_no_uid=True) -> List[str]:
        """
        Search mailbox for matching message uids in current folder
        :param criteria: message search criteria (see examples at ./doc/imap_search_criteria.txt)
        :param charset: IANA charset, indicates charset of the strings that appear in the search criteria. See rfc2978
        :param miss_no_uid: not add None values to result when uid item not matched to pattern
        :return: email message uids
        """
        nums = self.numbers(criteria, charset)
        if not nums:
            return []
        fetch_result = self.client.fetch(','.join(nums), "(UID)")
        check_command_status(fetch_result, MailboxUidsError)
        result = []
        for fetch_item in fetch_result[1]:
            # fetch_item: AnyStr  # todo uncomment after drop 3.5
            uid_match = re.search(UID_PATTERN, decode_value(fetch_item))  # noqa
            if uid_match:
                result.append(uid_match.group('uid'))
            elif not miss_no_uid:
                result.append(None)
        return result

    def _fetch_by_one(self, message_nums: Sequence[str], message_parts: str, reverse: bool) -> Iterator[list]:  # noqa
        for message_num in message_nums:
            fetch_result = self.client.fetch(message_num, message_parts)
            check_command_status(fetch_result, MailboxFetchError)
            yield fetch_result[1]

    def _fetch_in_bulk(self, message_nums: Sequence[str], message_parts: str, reverse: bool) -> Iterator[list]:
        if not message_nums:
            return
        fetch_result = self.client.fetch(','.join(message_nums), message_parts)
        check_command_status(fetch_result, MailboxFetchError)
        for built_fetch_item in chunks((reversed if reverse else iter)(fetch_result[1]), 2):
            yield built_fetch_item

    def fetch(self, criteria: Criteria = 'ALL', charset: str = 'US-ASCII', limit: Optional[Union[int, slice]] = None,
              miss_no_uid=True, mark_seen=True, reverse=False, headers_only=False,
              bulk=False) -> Iterator[MailMessage]:
        """
        Mail message generator in current folder by search criteria
        :param criteria: message search criteria (see examples at ./doc/imap_search_criteria.txt)
        :param charset: IANA charset, indicates charset of the strings that appear in the search criteria. See rfc2978
        :param limit: int | slice - limit number of read emails | slice emails range for read
                      useful for actions with a large number of messages, like "move" | paging
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
        nums = tuple((reversed if reverse else iter)(self.numbers(criteria, charset)))[limit_range]
        for fetch_item in (self._fetch_in_bulk if bulk else self._fetch_by_one)(nums, message_parts, reverse):  # noqa
            mail_message = self.email_message_class(fetch_item)
            if miss_no_uid and not mail_message.uid:
                continue
            yield mail_message

    def expunge(self) -> tuple:
        result = self.client.expunge()
        check_command_status(result, MailboxExpungeError)
        return result

    def delete(self, uid_list: Union[str, Iterable[str]]) -> Optional[Tuple[tuple, tuple]]:
        """
        Delete email messages
        Do nothing on empty uid_list
        :return: None on empty uid_list, command results otherwise
        """
        uid_str = clean_uids(uid_list)
        if not uid_str:
            return None
        store_result = self.client.uid('STORE', uid_str, '+FLAGS', r'(\Deleted)')
        check_command_status(store_result, MailboxDeleteError)
        expunge_result = self.expunge()
        return store_result, expunge_result

    def copy(self, uid_list: Union[str, Iterable[str]], destination_folder: AnyStr) -> Optional[tuple]:
        """
        Copy email messages into the specified folder
        Do nothing on empty uid_list
        :return: None on empty uid_list, command results otherwise
        """
        uid_str = clean_uids(uid_list)
        if not uid_str:
            return None
        copy_result = self.client.uid('COPY', uid_str, encode_folder(destination_folder))  # noqa
        check_command_status(copy_result, MailboxCopyError)
        return copy_result

    def move(self, uid_list: Union[str, Iterable[str]], destination_folder: AnyStr) -> Optional[Tuple[tuple, tuple]]:
        """
        Move email messages into the specified folder
        Do nothing on empty uid_list
        :return: None on empty uid_list, command results otherwise
        """
        uid_str = clean_uids(uid_list)
        if not uid_str:
            return None
        copy_result = self.copy(uid_str, destination_folder)
        delete_result = self.delete(uid_str)
        return copy_result, delete_result

    def flag(self, uid_list: Union[str, Iterable[str]], flag_set: Union[str, Iterable[str]], value: bool) \
            -> Optional[Tuple[tuple, tuple]]:
        """
        Set/unset email flags
        Do nothing on empty uid_list
        System flags contains in consts.MailMessageFlags.all
        :return: None on empty uid_list, command results otherwise
        """
        uid_str = clean_uids(uid_list)
        if not uid_str:
            return None
        store_result = self.client.uid(
            'STORE', uid_str, ('+' if value else '-') + 'FLAGS',
            '({})'.format(' '.join(clean_flags(flag_set))))
        check_command_status(store_result, MailboxFlagError)
        expunge_result = self.expunge()
        return store_result, expunge_result

    def append(self, message: Union[MailMessage, bytes],
               folder: AnyStr = 'INBOX',
               dt: Optional[datetime.datetime] = None,
               flag_set: Optional[Union[str, Iterable[str]]] = None) -> tuple:
        """
        Append email messages to server
        :param message: MailMessage object or bytes
        :param folder: destination folder, INBOX by default
        :param dt: email message datetime with tzinfo, now by default, imaplib.Time2Internaldate types supported
        :param flag_set: email message flags, no flags by default. System flags at consts.MailMessageFlags.all
        :return: command results
        """
        if PYTHON_VERSION_MINOR < 6:
            timezone = datetime.timezone(datetime.timedelta(hours=0))
        else:
            timezone = datetime.datetime.now().astimezone().tzinfo  # system timezone
        cleaned_flags = clean_flags(flag_set or [])
        typ, dat = self.client.append(
            encode_folder(folder),  # noqa
            '({})'.format(' '.join(cleaned_flags)) if cleaned_flags else None,
            dt or datetime.datetime.now(timezone),  # noqa
            message if type(message) is bytes else message.obj.as_bytes()
        )
        append_result = (typ, dat)
        check_command_status(append_result, MailboxAppendError)
        return append_result


class MailBoxUnencrypted(BaseMailBox):
    """Working with the email box through IMAP4"""

    def __init__(self, host='', port=143, timeout=None):
        """
        :param host: host's name (default: localhost)
        :param port: port number
        :param timeout: timeout in seconds for the connection attempt, since python 3.9
        """
        check_timeout_arg_support(timeout)
        self._host = host
        self._port = port
        self._timeout = timeout
        super().__init__()

    def _get_mailbox_client(self) -> imaplib.IMAP4:
        if PYTHON_VERSION_MINOR < 9:
            return imaplib.IMAP4(self._host, self._port)
        else:
            return imaplib.IMAP4(self._host, self._port, self._timeout)  # noqa


class MailBox(BaseMailBox):
    """Working with the email box through IMAP4 over SSL connection"""

    def __init__(self, host='', port=993, timeout=None, keyfile=None, certfile=None, ssl_context=None):
        """
        :param host: host's name (default: localhost)
        :param port: port number
        :param timeout: timeout in seconds for the connection attempt, since python 3.9
        :param keyfile: PEM formatted file that contains your private key (deprecated)
        :param certfile: PEM formatted certificate chain file (deprecated)
        :param ssl_context: SSLContext object that contains your certificate chain and private key
        """
        check_timeout_arg_support(timeout)
        self._host = host
        self._port = port
        self._timeout = timeout
        self._keyfile = keyfile
        self._certfile = certfile
        self._ssl_context = ssl_context
        super().__init__()

    def _get_mailbox_client(self) -> imaplib.IMAP4:
        if PYTHON_VERSION_MINOR < 9:
            return imaplib.IMAP4_SSL(self._host, self._port, self._keyfile, self._certfile, self._ssl_context)
        else:
            return imaplib.IMAP4_SSL(self._host, self._port, self._keyfile, self._certfile, self._ssl_context,
                                     self._timeout)


class MailBoxTls(BaseMailBox):
    """Working with the email box through IMAP4 with STARTTLS"""

    def __init__(self, host='', port=993, timeout=None, ssl_context=None):
        """
        :param host: host's name (default: localhost)
        :param port: port number
        :param timeout: timeout in seconds for the connection attempt, since python 3.9
        :param ssl_context: SSLContext object that contains your certificate chain and private key
        """
        check_timeout_arg_support(timeout)
        self._host = host
        self._port = port
        self._timeout = timeout
        self._ssl_context = ssl_context
        super().__init__()

    def _get_mailbox_client(self) -> imaplib.IMAP4:
        if PYTHON_VERSION_MINOR < 9:
            client = imaplib.IMAP4(self._host, self._port)
        else:
            client = imaplib.IMAP4(self._host, self._port, self._timeout)  # noqa
        result = client.starttls(self._ssl_context)
        check_command_status(result, MailboxStarttlsError)
        return client
