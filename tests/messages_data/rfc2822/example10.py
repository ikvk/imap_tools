import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='',
    from_='pete@silly.test',
    to=('c@public.example', 'joe@example.org', 'jdoe@one.test'),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(1969, 2, 13, 23, 32, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=73800))),
    date_str='Thu,\r\n      13\r\n        Feb\r\n          1969\r\n      23:32\r\n               -0330 (Newfoundland Time)',
    text='Testing.\r\n',
    html='',
    headers={'from': ('Pete(A wonderful \\) chap) <pete(his account)@silly.test(his host)>',), 'to': ("A Group(Some people)\r\n     :Chris Jones <c@(Chris's host.)public.example>,\r\n         joe@example.org,\r\n  John <jdoe@one.test> (my dear friend); (the end of the group)",), 'cc': ('(Empty list)(start)Undisclosed recipients  :(nobody(that I know))  ;',), 'date': ('Thu,\r\n      13\r\n        Feb\r\n          1969\r\n      23:32\r\n               -0330 (Newfoundland Time)',), 'message-id': ('<testabcd.1234@silly.test>',)},
    attachments=[],
    from_values=EmailAddress(name='Pete (A wonderful ) chap his account his host)', email='pete@silly.test'),
    to_values=(EmailAddress(name="Chris Jones (Chris's host.)", email='c@public.example'), EmailAddress(name='', email='joe@example.org'), EmailAddress(name='John', email='jdoe@one.test')),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)