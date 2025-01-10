import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='undef method parameter bug',
    from_='Big Bug bb@bug.com',
    to=('rubymail@ruby-lang.org',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2010, 2, 19, 10, 8, 29, tzinfo=datetime.timezone(datetime.timedelta(seconds=10800))),
    date_str='Fri, 19 Feb 2010 10:08:29 +0300',
    text='foo bar\r\n',
    html='',
    headers={'from': ('Big Bug bb@bug.com',), 'to': ('rubymail@ruby-lang.org',), 'subject': ('undef method parameter bug',), 'date': ('Fri, 19 Feb 2010 10:08:29 +0300',), 'mime-version': ('1.0',), 'content-type': ('Text/Plain; charset="iso-8859-1"',), 'content-transfer-encoding': ('quoted-printable',), 'message-id': ('201002191008.30117.foo.bar@company.com',)},
    attachments=[],
    from_values=EmailAddress(name='', email='Big Bug bb@bug.com'),
    to_values=(EmailAddress(name='', email='rubymail@ruby-lang.org'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)