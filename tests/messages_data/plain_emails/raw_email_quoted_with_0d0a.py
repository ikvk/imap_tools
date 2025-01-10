import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='testing',
    from_='foo@example.com',
    to=('blah@example.com',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2005, 6, 6, 22, 21, 22, tzinfo=datetime.timezone(datetime.timedelta(seconds=7200))),
    date_str='Mon, 6 Jun 2005 22:21:22 +0200',
    text="A fax has arrived from remote ID ''.\r\n------------------------------------------------------------\r\nTime: 3/9/2006 3:50:52 PM\r\nReceived from remote ID: \r\nInbound user ID XXXXXXXXXX, routing code XXXXXXXXX\r\nResult: (0/352;0/0) Successful Send\r\nPage record: 1 - 1\r\nElapsed time: 00:58 on channel 11\r\n\r\n",
    html='',
    headers={'mime-version': ('1.0 (Apple Message framework v730)',), 'message-id': ('<9169D984-4E0B-45EF-82D4-8F5E53AD7012@example.com>',), 'from': ('foo@example.com',), 'subject': ('testing',), 'date': ('Mon, 6 Jun 2005 22:21:22 +0200',), 'to': ('blah@example.com',), 'content-transfer-encoding': ('quoted-printable',), 'content-type': ('text/plain',)},
    attachments=[],
    from_values=EmailAddress(name='', email='foo@example.com'),
    to_values=(EmailAddress(name='', email='blah@example.com'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)