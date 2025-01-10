import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='Re: Test: "漢字" mid "漢字" tail',
    from_='jamis@37signals.com',
    to=('jamis@37signals.com',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2005, 5, 2, 16, 7, 5, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=64800))),
    date_str='Mon, 2 May 2005 16:07:05 -0600',
    text='대부분의 마찬가지로, 우리는 하나님을 믿습니다.\r\n\r\n제 이름은 Jamis입니다.',
    html='',
    headers={'mime-version': ('1.0 (Apple Message framework v622)',), 'content-transfer-encoding': ('base64',), 'message-id': ('<d3b8cf8e49f04480850c28713a1f473e@37signals.com>',), 'content-type': ('text/plain;\r\n  charset=EUC-KR;\r\n  format=flowed',), 'to': ('jamis@37signals.com',), 'from': ('Jamis Buck <jamis@37signals.com>',), 'subject': ('Re: Test: =?UTF-8?B?Iua8ouWtlyI=?= mid =?UTF-8?B?Iua8ouWtlyI=?= tail',), 'date': ('Mon, 2 May 2005 16:07:05 -0600',)},
    attachments=[],
    from_values=EmailAddress(name='Jamis Buck', email='jamis@37signals.com'),
    to_values=(EmailAddress(name='', email='jamis@37signals.com'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)