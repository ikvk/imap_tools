import re
import email
import codecs
import imaplib
from functools import lru_cache
from email.header import decode_header


def decode_value(value, encoding) -> str:
    """Converts value to utf-8 encoding"""
    if isinstance(value, bytes):
        if encoding in ['utf-8', None]:
            return value.decode('utf-8', 'ignore')
        else:
            try:
                return value.decode(encoding)
            except LookupError:  # unknown encoding
                return value.decode('utf-8', 'ignore')
    return value


def parse_email_address(value: str) -> dict:
    """
    Parse email address str, example: "Ivan Petrov" <ivan@mail.ru>
    @:return dict(name: str, email: str, full: str)
    """
    address = ''.join(char for char in value if char.isprintable())
    address = re.sub('[\n\r\t]+', ' ', address)
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


class MailMessage:
    """The email message"""

    def __init__(self, message_id: str, fetch_data):
        raw_message_data, raw_uid_data, raw_flag_data = self._get_message_data_parts(fetch_data)
        self._raw_uid_data = raw_uid_data
        self._raw_flag_data = raw_flag_data
        self.id = message_id
        self.obj = email.message_from_bytes(raw_message_data)

    @staticmethod
    def _get_message_data_parts(fetch_data) -> (bytes, bytes, [bytes]):
        """
        :param fetch_data: Message object model
        :returns (raw_message_data: bytes, raw_uid_data: bytes, raw_flag_data: [bytes])
        *Elements may contain byte strings in any order, like: b'4517 (FLAGS (\\Recent NonJunk))'
        """
        raw_message_data = b''
        raw_uid_data = b''
        raw_flag_data = []
        for fetch_item in fetch_data:
            # flags
            if type(fetch_item) is bytes and imaplib.ParseFlags(fetch_item):
                raw_flag_data.append(fetch_item)
            # data, uid
            if type(fetch_item) is tuple:
                raw_uid_data = fetch_item[0]
                raw_message_data = fetch_item[1]
        return raw_message_data, raw_uid_data, raw_flag_data

    def _parse_addresses(self, value: str) -> (dict,):
        """
        Parse email addresses from header (see decode_header)
        @:return tuple(dict(name: str, email: str, full: str))
        """
        if value not in self.obj:
            return ()
        dh = decode_header(self.obj[value])
        return tuple(parse_email_address(part) for part in decode_value(dh[0][0], dh[0][1]).split(','))

    @property
    @lru_cache()
    def uid(self) -> str or None:
        """Message UID"""
        # zimbra, yandex, gmail, gmx
        uid_match = re.search(r'UID\s+(?P<uid>\d+)', self._raw_uid_data.decode())
        if uid_match:
            return uid_match.group('uid')
        # mail.ru, ms exchange server
        for raw_flag_item in self._raw_flag_data:
            uid_flag_match = re.search(r'(^|\s+)UID\s+(?P<uid>\d+)($|\s+)', raw_flag_item.decode())
            if uid_flag_match:
                return uid_flag_match.group('uid')
        return None

    @property
    @lru_cache()
    def flags(self) -> (str,):
        """
        Message flags
        *This attribute will not be changed after actions: flag, seen
        """
        result = []
        for raw_flag_item in self._raw_flag_data:
            result.extend(imaplib.ParseFlags(raw_flag_item))
        return tuple(i.decode().strip().replace('\\', '').upper() for i in result)

    @property
    @lru_cache()
    def subject(self) -> str:
        """Message subject"""
        if 'subject' in self.obj:
            msg_subject = decode_header(self.obj['subject'])
            return decode_value(msg_subject[0][0], msg_subject[0][1])
        return ''

    @property
    @lru_cache()
    def from_values(self) -> dict or None:
        """Sender (all data)"""
        result = self._parse_addresses('from')
        return result[0] if result else None

    @property
    @lru_cache()
    def from_(self) -> str:
        """Sender email"""
        return self.from_values['email'] if self.from_values else ''

    @property
    @lru_cache()
    def to_values(self) -> (dict,):
        """Recipients (all data)"""
        return self._parse_addresses('to')

    @property
    @lru_cache()
    def to(self) -> (str,):
        """Recipients emails"""
        return tuple(i['email'] for i in self.to_values)

    @property
    @lru_cache()
    def cc_values(self) -> (dict,):
        """Carbon copy (all data)"""
        return self._parse_addresses('cc')

    @property
    @lru_cache()
    def cc(self) -> (str,):
        """Carbon copy emails"""
        return tuple(i['email'] for i in self.cc_values)

    @property
    @lru_cache()
    def bcc_values(self) -> (dict,):
        """Blind carbon copy (all data)"""
        return self._parse_addresses('bcc')

    @property
    @lru_cache()
    def bcc(self) -> (str,):
        """Blind carbon copy emails"""
        return tuple(i['email'] for i in self.bcc_values)

    @property
    @lru_cache()
    def date(self) -> str:
        """Message date"""
        return str(self.obj['Date'] or '')

    @property
    @lru_cache()
    def text(self) -> str:
        """The text of the mail message"""
        for part in self.obj.walk():
            # multipart/* are just containers
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get_content_type() in ('text/plain', 'text/'):
                return part.get_payload(decode=True).decode(part.get_content_charset(failobj='utf-8'), 'ignore')
        return ''

    @property
    @lru_cache()
    def html(self) -> str:
        """HTML text of the mail message"""
        for part in self.obj.walk():
            # multipart/* are just containers
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get_content_type() == 'text/html':
                return part.get_payload(decode=True).decode(part.get_content_charset(failobj='utf-8'), 'ignore')
        return ''

    @property
    @lru_cache()
    def attachments(self) -> [(str, bytes)]:
        """
        Attachments of the mail message (generator)
        :return: [(filename: str, payload: bytes)]
        """
        result = []
        for part in self.obj.walk():
            if part.get_content_maintype() == 'multipart':
                # multipart/* are just containers
                continue
            if part.get('Content-Disposition') is None:
                continue
            filename = part.get_filename()
            if not part.get_filename():
                continue  # this is what happens when Content-Disposition = inline
            filename = decode_value(*decode_header(filename)[0])
            payload = part.get_payload(decode=True)
            if payload:
                result.append((filename, payload))
            else:
                # multipart payload, such as .eml (see get_payload)
                multipart_payload = part.get_payload()
                if isinstance(multipart_payload, list):
                    for payload_item in multipart_payload:
                        if hasattr(payload_item, 'as_bytes'):
                            payload_item_bytes = payload_item.as_bytes()
                            cte = str(part.get('content-transfer-encoding', '')).lower()
                            if payload_item_bytes and cte:
                                result.append((filename, codecs.decode(payload_item_bytes, cte)))
        return result
