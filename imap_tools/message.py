import re
import email
import base64
import imaplib
from functools import lru_cache
from email.header import decode_header

from .utils import decode_value, parse_email_addresses, parse_email_date


class MailMessage:
    """The email message"""

    def __init__(self, fetch_data):
        raw_message_data, raw_uid_data, raw_flag_data = self._get_message_data_parts(fetch_data)
        self._raw_uid_data = raw_uid_data
        self._raw_flag_data = raw_flag_data
        self.obj = email.message_from_bytes(raw_message_data)

    @classmethod
    def from_bytes(cls, raw_message_data: bytes):
        """Alternative constructor"""
        return cls([(None, raw_message_data)])

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
                raw_flag_data.append(fetch_item[0])  # may contains flags (google, dovecot)
                raw_message_data = fetch_item[1]
        return raw_message_data, raw_uid_data, raw_flag_data

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
        result_set = parse_email_addresses(self.obj['From'] or '')
        return result_set[0] if result_set else None

    @property
    @lru_cache()
    def from_(self) -> str:
        """Sender email"""
        return self.from_values['email'] if self.from_values else ''

    @property
    @lru_cache()
    def to_values(self) -> (dict,):
        """Recipients (all data)"""
        return parse_email_addresses(self.obj['To'] or '')

    @property
    @lru_cache()
    def to(self) -> (str,):
        """Recipients emails"""
        return tuple(i['email'] for i in self.to_values)

    @property
    @lru_cache()
    def cc_values(self) -> (dict,):
        """Carbon copy (all data)"""
        return parse_email_addresses(self.obj['Cc'] or '')

    @property
    @lru_cache()
    def cc(self) -> (str,):
        """Carbon copy emails"""
        return tuple(i['email'] for i in self.cc_values)

    @property
    @lru_cache()
    def bcc_values(self) -> (dict,):
        """Blind carbon copy (all data)"""
        return parse_email_addresses(self.obj['Bcc'] or '')

    @property
    @lru_cache()
    def bcc(self) -> (str,):
        """Blind carbon copy emails"""
        return tuple(i['email'] for i in self.bcc_values)

    @property
    @lru_cache()
    def reply_to_values(self) -> (dict,):
        """Reply-to emails (all data)"""
        return parse_email_addresses(self.obj['Reply-To'] or '')

    @property
    @lru_cache()
    def reply_to(self) -> (str,):
        """Reply-to emails"""
        return tuple(i['email'] for i in self.reply_to_values)

    @property
    @lru_cache()
    def date_str(self) -> str:
        """Message sent date"""
        return str(self.obj['Date'] or '')

    @property
    @lru_cache()
    def date(self):
        """
        Message sent date
        :rtype: datetime.datetime
        """
        return parse_email_date(self.date_str)

    @property
    @lru_cache()
    def text(self) -> str:
        """Plain text of the mail message"""
        for part in self.obj.walk():
            # multipart/* are containers
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get_content_type() in ('text/plain', 'text/'):
                return decode_value(part.get_payload(decode=True), part.get_content_charset())
        return ''

    @property
    @lru_cache()
    def html(self) -> str:
        """HTML text of the mail message"""
        for part in self.obj.walk():
            # multipart/* are containers
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get_content_type() == 'text/html':
                return decode_value(part.get_payload(decode=True), part.get_content_charset())
        return ''

    @property
    @lru_cache()
    def headers(self) -> {str: (str,)}:
        """Message headers"""
        raw_headers = getattr(self.obj, '_headers', ())
        return {key: tuple(v for k, v in raw_headers if k == key) for key in set(i[0] for i in raw_headers)}

    @property
    @lru_cache()
    def attachments(self) -> ['Attachment']:
        """
        Mail message attachments list
        :return: [Attachment]
        """
        results = []
        i = 0
        for part in self.obj.walk():
            if part.get_content_maintype() == 'multipart':
                # multipart/* are just containers
                continue
            if part.get('Content-Disposition') is None:
                continue
            filename = part.get_filename()
            if not filename:
                if part.get('Content-Type') == 'message/rfc822':
                    filename = f"mail_as_attachment{str(i)}"
                    i += 1
                else:
                    continue  # this is what happens when Content-Disposition = inline

            results.append(Attachment(part))
        return results


class Attachment:
    """An attachment for a MailMessage"""

    def __init__(self, part):
        self._part = part

    @property
    @lru_cache()
    def filename(self) -> str:
        filename = self._part.get_filename()
        if not filename and self._part.get("Content-Type") == "message/rfc822":
            filename = "mail_as_attachment"
        return ''.join(decode_value(*part) for part in decode_header(filename))

    @property
    @lru_cache()
    def content_type(self) -> str:
        return self._part.get_content_type()

    @property
    @lru_cache()
    def payload(self) -> bytes:
        payload = self._part.get_payload(decode=True)
        if payload:
            return payload
        # multipart payload, such as .eml (see get_payload)
        multipart_payload = self._part.get_payload()
        if isinstance(multipart_payload, list):
            for payload_item in multipart_payload:
                if hasattr(payload_item, 'as_bytes'):
                    payload_item_bytes = payload_item.as_bytes()  # noqa
                    cte = str(self._part.get('content-transfer-encoding', '')).lower().strip()
                    if payload_item_bytes and cte:
                        if cte == 'base64':
                            return base64.b64decode(payload_item_bytes)
                        elif cte in ('7bit', '8bit', 'quoted-printable', 'binary'):
                            return payload_item_bytes  # quopri.decodestring
        # could not find payload
        return b''
