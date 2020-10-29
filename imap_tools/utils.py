import re
import inspect
import datetime
from itertools import zip_longest
from email.utils import getaddresses, parsedate_to_datetime
from email.header import decode_header, Header

SHORT_MONTH_NAMES = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')


def cleaned_uid_set(uid_set: str or [str] or iter) -> str:
    """
    Prepare set of uid for use in IMAP commands
    uid_set may be:
        str, that is comma separated uids
        Iterable, that contains str uids
        Generator with "fetch" name, implicitly gets all uids
    """
    # str
    if type(uid_set) is str:
        if re.search(r'^(\d+,)*\d+$', uid_set):  # *optimization for already good str
            return uid_set
        uid_set = uid_set.split(',')
    # Generator
    if inspect.isgenerator(uid_set) and getattr(uid_set, '__name__', None) == 'fetch':
        uid_set = tuple(msg.uid for msg in uid_set if msg.uid)
    # Iterable
    try:
        uid_set_iter = iter(uid_set)
    except TypeError:
        raise TypeError('Wrong uid_set arg type: "{}"'.format(type(uid_set)))
    # check uid types
    for uid in uid_set_iter:
        if type(uid) is not str:
            raise TypeError('uid "{}" is not string'.format(str(uid)))
        if not uid.strip().isdigit():
            raise TypeError('Wrong uid: "{}"'.format(uid))
    return ','.join((i.strip() for i in uid_set))


def check_command_status(command_result: tuple, exception: type, expected='OK'):
    """
    Check that IMAP command responses status equals <expected> status
    If not, raise specified <exception>
    :param command_result: imap command result
    :param exception: exception subclass of UnexpectedCommandStatusError, that raises
    :param expected: expected command status
    """
    typ, data = command_result[0], command_result[1]
    if typ != expected:
        raise exception(command_result=command_result, expected=expected)


def decode_value(value: bytes or str, encoding=None) -> str:
    """Converts value to utf-8 encoding"""
    if isinstance(encoding, str):
        encoding = encoding.lower()
    if isinstance(value, bytes):
        try:
            return value.decode(encoding or 'utf-8', 'ignore')
        except LookupError:  # unknown encoding
            return value.decode('utf-8', 'ignore')
    return value


def parse_email_addresses(raw_header: str or Header) -> (dict,):
    """
    Parse email addresses from header
    :param raw_header: example: '=?UTF-8?B?0J7Qu9C1=?= <name@company.ru>,\r\n "\'\\"z, z\\"\'" <imap.tools@ya.ru>'
    :return: tuple(dict(name: str, email: str, full: str))
    """
    result = []
    if type(raw_header) is Header:
        raw_header = decode_value(*decode_header(raw_header)[0])
    for raw_name, email in getaddresses([raw_header]):
        name = decode_value(*decode_header(raw_name)[0]).strip()
        email = email.strip()
        if not (name or email):
            continue
        result.append({
            'email': email if '@' in email else '',
            'name': name,
            'full': '{} <{}>'.format(name, email) if name and email else name or email
        })
    return tuple(result)


def parse_email_date(value: str) -> datetime.datetime:
    """
    Parsing the date described in rfc2822
    1900-1-1 for unparsed, may be naive or with tzinfo
    """
    try:
        return parsedate_to_datetime(value)
    except Exception:  # noqa
        pass
    match = re.search(r'(?P<date>\d{1,2}\s+(' + '|'.join(SHORT_MONTH_NAMES) + r')\s+\d{4})\s+' +
                      r'(?P<time>\d{1,2}:\d{1,2}(:\d{1,2})?)\s*' +
                      r'(?P<zone_sign>[+-])?(?P<zone>\d{4})?', value)
    if match:
        group = match.groupdict()
        day, month, year = group['date'].split()
        time_values = group['time'].split(':')
        zone_sign = int('{}1'.format(group.get('zone_sign') or '+'))
        zone = group['zone']
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
    else:
        return datetime.datetime(1900, 1, 1)


def quote(value: str or bytes) -> str or bytes:
    if isinstance(value, str):
        return '"' + value.replace('\\', '\\\\').replace('"', '\\"') + '"'
    else:
        return b'"' + value.replace(b'\\', b'\\\\').replace(b'"', b'\\"') + b'"'


def pairs_to_dict(items: list) -> dict:
    """Example: ['MESSAGES', '3', 'UIDNEXT', '4'] -> {'MESSAGES': '3', 'UIDNEXT': '4'}"""
    if len(items) % 2 != 0:
        raise ValueError('An even-length array is expected')
    return dict((items[i * 2], items[i * 2 + 1]) for i in range(len(items) // 2))


def grouper(iterable: iter, n: int, fill_value=None) -> iter:
    """
    Group data into fixed-length chunks or blocks
    Examples:
        grouper('ABCDEFGH', 3, '?') --> [('A', 'B', 'C'), ('D', 'E', 'F'), ('G', 'H', '?')]
        grouper([1, 2, 3, 4, 5], 2) --> [(1, 2), (3, 4), (5, None)]
    """
    return zip_longest(*[iter(iterable)] * n, fillvalue=fill_value)


def parse_flags_strict(resp: bytes) -> tuple or None:
    match = re.compile(br'.*FLAGS \((?P<flags>[^\)]*)\)').match(resp)
    if not match:
        return None

    return tuple(match.group('flags').split())
