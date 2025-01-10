import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='',
    from_='john.q.public@example.com',
    to=('mary@x.test', 'jdoe@example.org', 'one@y.test'),
    cc=('boss@nil.test', 'sysservices@example.net'),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2003, 7, 1, 10, 52, 37, tzinfo=datetime.timezone(datetime.timedelta(seconds=7200))),
    date_str='Tue, 1 Jul 2003 10:52:37 +0200',
    text='Hi everyone.\r\n',
    html='',
    headers={'from': ('"Joe Q. Public" <john.q.public@example.com>',), 'to': ('Mary Smith <mary@x.test>, jdoe@example.org, Who? <one@y.test>',), 'cc': ('<boss@nil.test>, "Giant; \\"Big\\" Box" <sysservices@example.net>',), 'date': ('Tue, 1 Jul 2003 10:52:37 +0200',), 'message-id': ('<5678.21-Nov-1997@example.com>',)},
    attachments=[],
    from_values=EmailAddress(name='Joe Q. Public', email='john.q.public@example.com'),
    to_values=(EmailAddress(name='Mary Smith', email='mary@x.test'), EmailAddress(name='', email='jdoe@example.org'), EmailAddress(name='Who?', email='one@y.test')),
    cc_values=(EmailAddress(name='', email='boss@nil.test'), EmailAddress(name='Giant; "Big" Box', email='sysservices@example.net')),
    bcc_values=(),
    reply_to_values=(),
)