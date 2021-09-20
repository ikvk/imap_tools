import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='',
    from_='pete@silly.example',
    to=('c@a.test', 'joe@where.test', 'jdoe@one.test'),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(1969, 2, 13, 23, 32, 54, tzinfo=datetime.timezone(datetime.timedelta(-1, 73800))),
    date_str='Thu, 13 Feb 1969 23:32:54 -0330',
    text='Testing.\r\n',
    html='',
    headers={'from': ('Pete <pete@silly.example>',), 'to': ('A Group:Chris Jones <c@a.test>,joe@where.test,John <jdoe@one.test>;',), 'cc': ('Undisclosed recipients:;',), 'date': ('Thu, 13 Feb 1969 23:32:54 -0330',), 'message-id': ('<testabcd.1234@silly.example>',)},
    attachments=[],
    from_values=EmailAddress('Pete', 'pete@silly.example', 'Pete <pete@silly.example>'),
    to_values=(EmailAddress('Chris Jones', 'c@a.test', 'Chris Jones <c@a.test>'), EmailAddress('', 'joe@where.test', 'joe@where.test'), EmailAddress('John', 'jdoe@one.test', 'John <jdoe@one.test>')),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)