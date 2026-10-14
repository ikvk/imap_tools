import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='Badly    \r\n folded   \r\n    headers,    \r\n one\r\n \r\n \r\n line\r\n with   space   between   To and From\r\n ',
    from_='sender@example.com',
    to=('recipient@example.com',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2018, 4, 14, 14, 1, 30, tzinfo=datetime.timezone(datetime.timedelta(seconds=7200))),
    date_str='Sat, 14 Apr 2018 14:01:30 +0200',
    text="Here's our body\r\n",
    html='',
    headers={'date': ('Sat, 14 Apr 2018 14:01:30 +0200',), 'subject': ('Badly    \r\n folded   \r\n    headers,    \r\n one\r\n \r\n \r\n line\r\n with   space   between   To and From\r\n ',), 'to': ('"Recipient  with  spaces" <recipient@example.com>\r\n ',), 'from': ('sender@example.com',)},
    attachments=[],
    from_values=EmailAddress(name='', email='sender@example.com'),
    to_values=(EmailAddress(name='Recipient  with  spaces', email='recipient@example.com'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)