import inspect


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
