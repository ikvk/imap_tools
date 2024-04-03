import re
import sys
import datetime
from itertools import zip_longest
from email.utils import getaddresses, parsedate_to_datetime
from email.header import decode_header, Header
from typing import AnyStr, Union, Optional, Tuple, Iterable, Any, List, Dict, Iterator

from .consts import SHORT_MONTH_NAMES, MailMessageFlags
from .imap_utf7 import utf7_encode


def clean_uids(uid_set: Union[str, Iterable[str]]) -> str:
    """
    Prepare set of uid for use in IMAP commands
    uid RE patterns are not strict and allow invalid combinations, but simple. Example: 2,4:7,9,12:*
    :param uid_set:
        str, that is comma separated uids
        Iterable, that contains str uids
    :return: str - uids, concatenated by a comma
    """
    # str
    if type(uid_set) is str:
        if re.search(r'^([\d*:]+,)*[\d*:]+$', uid_set):  # *optimization for already good str
            return uid_set
        uid_set = uid_set.split(',')
    # check uid types
    for uid in uid_set:
        if type(uid) is not str:
            raise TypeError('uid "{}" is not string'.format(str(uid)))
        if not re.match(r'^[\d*:]+$', uid.strip()):
            raise TypeError('Wrong uid: "{}"'.format(uid))
    return ','.join(i.strip() for i in uid_set)


def check_command_status(command_result: tuple, exception: type, expected='OK'):
    """
    Check that IMAP command responses status equals <expected> status
    If not, raise specified <exception>
    :param command_result: imap command result: tuple(typ, data)
    :param exception: exception subclass of UnexpectedCommandStatusError, that raises
    :param expected: expected command status
    """
    typ, data = command_result[0], command_result[1]
    if typ != expected:
        raise exception(command_result=command_result, expected=expected)


def decode_value(value: AnyStr, encoding: Optional[str] = None) -> str:
    """Converts value to utf-8 encoding"""
    if isinstance(encoding, str):
        encoding = encoding.lower()
    if isinstance(value, bytes):
        try:
            return value.decode(encoding or 'utf-8', 'ignore')
        except LookupError:  # unknown encoding
            return value.decode('utf-8', 'ignore')
    return value


class EmailAddress:
    """Parsed email address info"""
    __slots__ = 'name', 'email'

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    @property
    def full(self):
        return '{} <{}>'.format(self.name, self.email) if self.name and self.email else self.name or self.email

    def __repr__(self):
        return "{}(name={}, email={})".format(
            self.__class__.__name__, repr(self.name), repr(self.email))

    def __eq__(self, other):
        return all(getattr(self, i) == getattr(other, i) for i in self.__slots__)


def parse_email_addresses(raw_header: Union[str, Header]) -> Tuple[EmailAddress, ...]:
    """
    Parse email addresses from header
    :param raw_header: example: '=?UTF-8?B?0J7Qu9C1=?= <name@company.ru>,\r\n "\'\\"z, z\\"\'" <imap.tools@ya.ru>'
    :return: (EmailAddress, ...)
    """
    result = []
    if type(raw_header) is Header:
        raw_header = decode_value(*decode_header(raw_header)[0])
    for raw_name, email in getaddresses([raw_header.replace('\r\n', '').replace('\n', '')]):
        name = decode_value(*decode_header(raw_name)[0]).strip()
        email = email.strip()
        if not (name or email):
            continue
        result.append(EmailAddress(
            name=name or (email if '@' not in email else ''),
            email=email if '@' in email else '',
        ))
    return tuple(result)


def parse_email_date(value: str) -> datetime.datetime:
    """
    Parsing the date described in rfc2822
    Result datetime may be naive or with tzinfo
    1900-1-1 for unparsed
    """
    try:
        return parsedate_to_datetime(value)
    except Exception:  # noqa
        pass
    match = re.search(
        r'(?P<date>\d{1,2}\s+(' + '|'.join(SHORT_MONTH_NAMES) + r')\s+\d{4})\s+' +
        r'(?P<time>\d{1,2}:\d{1,2}(:\d{1,2})?)\s*' +
        r'(?P<zone_sign>[+-])?(?P<zone>\d{4})?',
        value
    )
    if match:
        group = match.groupdict()
        day, month, year = group['date'].split()
        time_values = group['time'].split(':')
        zone_sign = int('{}1'.format(group.get('zone_sign') or '+'))
        zone = group['zone']
        try:
            return datetime.datetime(
                year=int(year),
                month=SHORT_MONTH_NAMES.index(month) + 1,
                day=int(day),
                hour=int(time_values[0]),
                minute=int(time_values[1]),
                second=int(time_values[2]) if len(time_values) > 2 else 0,
                tzinfo=datetime.timezone(datetime.timedelta(
                    hours=int(zone[:2]) * zone_sign,
                    minutes=int(zone[2:]) * zone_sign
                )) if zone else None,
            )
        except ValueError:
            pass
    return datetime.datetime(1900, 1, 1)


def quote(value: AnyStr) -> AnyStr:
    if isinstance(value, str):
        return '"' + value.replace('\\', '\\\\').replace('"', '\\"') + '"'
    else:
        return b'"' + value.replace(b'\\', b'\\\\').replace(b'"', b'\\"') + b'"'


def pairs_to_dict(items: List[Any]) -> Dict[Any, Any]:
    """Example: ['MESSAGES', '3', 'UIDNEXT', '4'] -> {'MESSAGES': '3', 'UIDNEXT': '4'}"""
    if len(items) % 2 != 0:
        raise ValueError('An even-length array is expected')
    return dict((items[i * 2], items[i * 2 + 1]) for i in range(len(items) // 2))


def chunks(iterable: Iterable[Any], n: int, fill_value: Optional[Any] = None) -> Iterator[Tuple[Any, ...]]:
    """
    Group data into fixed-length chunks or blocks
        [iter(iterable)]*n creates one iterator, repeated n times in the list
        izip_longest then effectively performs a round-robin of "each" (same) iterator
    Examples:
        chunks('ABCDEFGH', 3, '?') --> [('A', 'B', 'C'), ('D', 'E', 'F'), ('G', 'H', '?')]
        chunks([1, 2, 3, 4, 5], 2) --> [(1, 2), (3, 4), (5, None)]
    """
    return zip_longest(*[iter(iterable)] * n, fillvalue=fill_value)


def encode_folder(folder: AnyStr) -> bytes:
    """Encode folder name"""
    if isinstance(folder, bytes):
        return folder
    else:
        return quote(utf7_encode(folder))


def clean_flags(flag_set: Union[str, Iterable[str]]) -> List[str]:
    """
    Check the correctness of the flags
    :return: list of str - flags
    """
    if type(flag_set) is str:
        flag_set = [flag_set]
    upper_sys_flags = tuple(i.upper() for i in MailMessageFlags.all)
    for flag in flag_set:
        if not type(flag) is str:
            raise ValueError('Flag - str value expected, but {} received'.format(type(flag_set)))
        if flag.upper() not in upper_sys_flags and flag.startswith('\\'):
            raise ValueError('Non system flag must not start with "\\"')
    return flag_set


def check_timeout_arg_support(timeout):
    """If timeout arg not supports - raise ValueError"""
    if timeout is not None and sys.version_info.minor < 9:
        raise ValueError('imaplib.IMAP4 timeout argument supported since python 3.9')


def replace_html_ct_charset(html: str, new_charset: str) -> str:
    """Replace charset in META tag with content-type attribute in HTML text"""
    meta_ct_match = re.search(r'<\s*meta .*?content-type.*?>', html, re.IGNORECASE | re.DOTALL)
    if meta_ct_match:
        meta = meta_ct_match.group(0)
        meta_new = re.sub(r'charset\s*=\s*[a-zA-Z0-9_:.+-]+', 'charset={}'.format(new_charset), meta, 1, re.IGNORECASE)
        html = html.replace(meta, meta_new)
    return html


def chunks_crop(lst: iter, n: int) -> iter:
    """
    Yield successive n-sized chunks from lst.
    import pprint
    pprint.pprint(list(chunks(range(10, 75), 10)))
    [[10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
     [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
     [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
     [40, 41, 42, 43, 44, 45, 46, 47, 48, 49],
     [50, 51, 52, 53, 54, 55, 56, 57, 58, 59],
     [60, 61, 62, 63, 64, 65, 66, 67, 68, 69],
     [70, 71, 72, 73, 74]]
    """
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


class SortCriteria:
    """
    Sort criteria
    https://datatracker.ietf.org/doc/html/rfc5256
    ARRIVAL - Internal date and time of the message.
        This differs from the ON criteria in SEARCH, which uses just the internal date.
    CC - [IMAP] addr-mailbox of the first "cc" address.
    DATE - Sent date and time, as described in section 2.2.
    FROM - [IMAP] addr-mailbox of the first "From" address.
    SIZE - Size of the message in octets.
    SUBJECT - Base subject text.
    TO - [IMAP] addr-mailbox of the first "To" address.
    """
    ARRIVAL_DT_ASC = 'ARRIVAL'
    CC_ASC = 'CC'
    DATE_ASC = 'DATE'
    FROM_ASC = 'FROM'
    SIZE_ASC = 'SIZE'
    SUBJECT_ASC = 'SUBJECT'
    TO_ASC = 'TO'

    ARRIVAL_DT_DESC = 'REVERSE ARRIVAL'
    CC_DESC = 'REVERSE CC'
    DATE_DESC = 'REVERSE DATE'
    FROM_DESC = 'REVERSE FROM'
    SIZE_DESC = 'REVERSE SIZE'
    SUBJECT_DESC = 'REVERSE SUBJECT'
    TO_DESC = 'REVERSE TO'

    all = (
        ARRIVAL_DT_ASC, CC_ASC, DATE_ASC, FROM_ASC, SIZE_ASC, SUBJECT_ASC, TO_ASC,
        ARRIVAL_DT_DESC, CC_DESC, DATE_DESC, FROM_DESC, SIZE_DESC, SUBJECT_DESC, TO_DESC,
    )
