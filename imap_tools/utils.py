import re
import inspect
import datetime

short_month_names = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', "Dec")


def cleaned_uid_set(uid_set: str or [str] or iter) -> str:
    """
    Prepare set of uid for use in commands: delete/copy/move/seen
    uid_set can be:
        str, that is comma separated uids
        Iterable, that contains str uids
        Generator with "fetch" name, implicitly gets all non-empty uids
    """
    if not uid_set:
        raise ValueError('uid_set should not be empty')
    if type(uid_set) is str:
        uid_set = uid_set.split(',')
    if inspect.isgenerator(uid_set) and getattr(uid_set, '__name__', None) == 'fetch':
        uid_set = tuple(msg.uid for msg in uid_set if msg.uid)
    try:
        uid_set_iter = iter(uid_set)
    except TypeError:
        raise ValueError('Wrong uid type: "{}"'.format(type(uid_set)))
    for uid in uid_set_iter:
        if type(uid) is not str:
            raise ValueError('uid "{}" is not string'.format(str(uid)))
        if not uid.strip().isdigit():
            raise ValueError('Wrong uid: {}'.format(uid))
    return ','.join((i.strip() for i in uid_set))


class UnexpectedCommandStatusError(Exception):
    """Unexpected status in response"""


def check_command_status(command, command_result, expected='OK'):
    """
    Check that command responses status equals <expected> status
    If not, raises UnexpectedCommandStatusError
    """
    typ, data = command_result[0], command_result[1]
    if typ != expected:
        raise UnexpectedCommandStatusError(
            'Response status for command "{command}" == "{typ}", "{exp}" expected, data: {data}'.format(
                command=command, typ=typ, data=str(data), exp=expected))


def decode_value(value, encoding=None) -> str:
    """Converts value to utf-8 encoding"""
    if isinstance(encoding, str):
        encoding = encoding.lower()
    if isinstance(value, bytes):
        if encoding in ('utf-8', 'utf8', None):
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
    address = ''.join(char for char in value if char.isprintable()).strip()
    address = re.sub('[\n\r\t]+', ' ', address)
    result = {'email': '', 'name': '', 'full': address}
    match = re.match('(?P<name>.*)?<(?P<email>.*@.*)>', address, re.UNICODE)
    if match:
        group = match.groupdict()
        result['name'] = group['name'].strip()
        result['email'] = group['email'].strip()
    else:
        result['email' if '@' in address else 'name'] = address
    return result


def parse_email_date(value: str) -> datetime.datetime:
    """Parsing the date described in rfc2822"""
    match = re.search(r'(?P<date>\d{1,2}\s+(' + '|'.join(short_month_names) + r')\s+\d{4})\s+' +
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
            month=short_month_names.index(month) + 1,
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


def quote(value: str or bytes):
    if isinstance(value, str):
        return '"' + value.replace('\\', '\\\\').replace('"', '\\"') + '"'
    else:
        return b'"' + value.replace(b'\\', b'\\\\').replace(b'"', b'\\"') + b'"'


def pairs_to_dict(items: list) -> dict:
    """Example: ['MESSAGES', '3', 'UIDNEXT', '4'] -> {'MESSAGES': '3', 'UIDNEXT': '4'}"""
    if len(items) % 2 != 0:
        raise ValueError('An even-length array is expected')
    return dict((items[i * 2], items[i * 2 + 1]) for i in range(len(items) // 2))
