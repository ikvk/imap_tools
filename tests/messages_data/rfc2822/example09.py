import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='Saying Hello',
    from_='jdoe@machine.example',
    to=('mary@example.net',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(1997, 11, 21, 9, 55, 6, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=64800))),
    date_str='Fri, 21 Nov 1997 09:55:06 -0600',
    text='This is a message just to say hello.\r\nSo, "Hello".\r\n',
    html='',
    headers={'received': ('from x.y.test\r\n   by example.net\r\n   via TCP\r\n   with ESMTP\r\n   id ABC12345\r\n   for <mary@example.net>;  21 Nov 1997 10:05:43 -0600', 'from machine.example by x.y.test; 21 Nov 1997 10:01:22 -0600'), 'from': ('John Doe <jdoe@machine.example>',), 'to': ('Mary Smith <mary@example.net>',), 'subject': ('Saying Hello',), 'date': ('Fri, 21 Nov 1997 09:55:06 -0600',), 'message-id': ('<1234@local.machine.example>',)},
    attachments=[],
    from_values=EmailAddress(name='John Doe', email='jdoe@machine.example'),
    to_values=(EmailAddress(name='Mary Smith', email='mary@example.net'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)