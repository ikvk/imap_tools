import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='NOTE: 한국말로 하는 것',
    from_='mikel@me.com',
    to=('bob@bob.com',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2008, 9, 20, 20, 4, 30, tzinfo=datetime.timezone(datetime.timedelta(seconds=10800))),
    date_str='Sat, 20 Sep 2008 20:04:30 +0300 (�������� ������ ��������������)',
    text='대부분의 마찬가지로, 우리는 하나님을 믿습니다.\r\n\r\n제 이름은 Jamis입니다.',
    html='',
    headers={'mime-version': ('1.0 (Apple Message framework v622)',), 'received': ('from jsj1wlrmd001.webex.com (by jsj1wlrmd001.webex.com\r\n  (8.12.10/8.12.11) with ESMTP id m8MKKPTs022429\r\n  for <xxxx@example.com>; Mon, 22 Sep 2008 20:20:25 GMT',), 'content-transfer-encoding': ('base64',), 'message-id': ('<d3b8cf8e49f04480850c28713a1f473e@lindsaar.net>',), 'content-type': ('text/plain;\r\n  charset=EUC-KR;\r\n  format=flowed',), 'to': ('bob@bob.com',), 'from': ('mikel@me.com',), 'subject': ('=?EUC-KR?Q?NOTE:_=C7=D1=B1=B9=B8=BB=B7=CE_=C7=CF=B4=C2_=B0=CD?=',), 'date': ('Sat, 20 Sep 2008 20:04:30 +0300 (\udcc3\udcb9\udcc3\udcb2\udcc3\udca5\udcc3\udcaf \udcc3\udcb7\udcc3\udca9\udcc3\udcb5 \udcc3\udca9\udcc3\udcb8\udcc3\udca5\udcc3\udcb9\udcc3\udcac\udcc3\udca9\udcc3\udcad)',)},
    attachments=[],
    from_values=EmailAddress(name='', email='mikel@me.com'),
    to_values=(EmailAddress(name='', email='bob@bob.com'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)