import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='',
    from_='john.q.public@example.com',
    to=('mary@example.net', 'jdoe@test.example'),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2003, 7, 1, 10, 52, 37, tzinfo=datetime.timezone(datetime.timedelta(seconds=7200))),
    date_str='Tue, 1 Jul 2003 10:52:37 +0200',
    text='Hi everyone.\r\n',
    html='',
    headers={'from': ('Joe Q. Public <john.q.public@example.com>',), 'to': ('Mary Smith <@machine.tld:mary@example.net>, , jdoe@test   . example',), 'date': ('Tue, 1 Jul 2003 10:52:37 +0200',), 'message-id': ('<5678.21-Nov-1997@example.com>',)},
    attachments=[],
    from_values=EmailAddress(name='Joe Q. Public', email='john.q.public@example.com'),
    to_values=(EmailAddress(name='Mary Smith', email='mary@example.net'), EmailAddress(name='', email='jdoe@test.example')),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)