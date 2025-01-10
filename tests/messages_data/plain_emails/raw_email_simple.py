import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='Testing outlook',
    from_='mikel@nowhere.com',
    to=('mikel@somewhere.com',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2007, 10, 21, 19, 38, 13, tzinfo=datetime.timezone(datetime.timedelta(seconds=36000))),
    date_str='Sun, 21 Oct 2007 19:38:13 +1000',
    text='Hello Mikel\r\n\r\n',
    html='',
    headers={'return-path': ('<mikel@nowhere.com>',), 'received': ('from mikel091a by oaamta05sl.mx.bigpond.com with SMTP id <20071021093820.JFMT24025.oaamta05sl.mx.bigpond.com@mikel091a> for <mikel@nowhere.com.else>; Sun, 21 Oct 2007 19:38:20 +1000',), 'date': ('Sun, 21 Oct 2007 19:38:13 +1000',), 'from': ('Mikel Lindsaar <mikel@nowhere.com>',), 'to': ('Mikel <mikel@somewhere.com>',), 'message-id': ('<009601c813c6$19df3510$0437d30a@mikel091a>',), 'subject': ('Testing outlook',)},
    attachments=[],
    from_values=EmailAddress(name='Mikel Lindsaar', email='mikel@nowhere.com'),
    to_values=(EmailAddress(name='Mikel', email='mikel@somewhere.com'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)