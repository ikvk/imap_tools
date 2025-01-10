import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='NOTE: 한국말로 하는 것',
    from_='jamis@37signals.com',
    to=('willard15georgina@jamis.backpackit.com',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2005, 5, 2, 16, 7, 5, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=64800))),
    date_str='Mon, 2 May 2005 16:07:05 -0600',
    text='대부분의 마찬가지로, 우리는 하나님을 믿습니다.\r\n\r\n제 이름은 Jamis입니다.',
    html='',
    headers={'mime-version': ('1.0 (Apple Message framework v622)',), 'content-transfer-encoding': ('base64',), 'message-id': ('<d3b8cf8e49f04480850c28713a1f473e@37signals.com>',), 'content-type': ('text/plain;\r\n  charset=EUC-KR;\r\n  format=flowed',), 'to': ('willard15georgina@jamis.backpackit.com',), 'from': ('Jamis Buck <jamis@37signals.com>',), 'subject': ('=?EUC-KR?Q?NOTE:_=C7=D1=B1=B9=B8=BB=B7=CE_=C7=CF=B4=C2_=B0=CD?=',), 'date': ('Mon, 2 May 2005 16:07:05 -0600',)},
    attachments=[],
    from_values=EmailAddress(name='Jamis Buck', email='jamis@37signals.com'),
    to_values=(EmailAddress(name='', email='willard15georgina@jamis.backpackit.com'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)