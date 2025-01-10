import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='Filth',
    from_='xxx@xxxx.xxx',
    to=('xxx@xxxx.xxx',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2005, 5, 8, 12, 30, 8, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=68400))),
    date_str='Sun, 8 May 2005 12:30:08 -0500',
    text="Some text\r\n\r\n--\r\nThis Orange Multi Media Message was sent wirefree from an Orange\r\nMMS phone. If you would like to reply, please text or phone the\r\nsender directly by using the phone number listed in the sender's\r\naddress. To learn more about Orange's Multi Media Messaging\r\nService, find us on the Web at xxx.xxxx.xxx.uk/mms\r\n\r\n\r\n--mimepart_427e4cb4ca329_133ae40413c81ef-\r\n",
    html='',
    headers={'return-path': ('<xxx@xxxx.xxx>',), 'received': ('from xxx.xxxx.xxx by xxx.xxxx.xxx with ESMTP id 6AAEE3B4D23 for <xxx@xxxx.xxx>; Sun, 8 May 2005 12:30:23 -0500', 'from xxx.xxxx.xxx by xxx.xxxx.xxx with ESMTP id j48HUC213279 for <xxx@xxxx.xxx>; Sun, 8 May 2005 12:30:13 -0500', 'from conversion-xxx.xxxx.xxx.net by xxx.xxxx.xxx id <0IG600901LQ64I@xxx.xxxx.xxx> for <xxx@xxxx.xxx>; Sun, 8 May 2005 12:30:12 -0500', 'from agw1 by xxx.xxxx.xxx with ESMTP id <0IG600JFYLYCAxxx@xxxx.xxx> for <xxx@xxxx.xxx>; Sun, 8 May 2005 12:30:12 -0500'), 'date': ('Sun, 8 May 2005 12:30:08 -0500',), 'from': ('xxx@xxxx.xxx',), 'to': ('xxx@xxxx.xxx',), 'message-id': ('<7864245.1115573412626.JavaMxxx@xxxx.xxx>',), 'subject': ('Filth',), 'mime-version': ('1.0',), 'content-type': ('multipart/mixed; boundary=mimepart_427e4cb4ca329_133ae40413c81ef',), 'x-mms-priority': ('1',), 'x-mms-transaction-id': ('3198421808-0',), 'x-mms-message-type': ('0',), 'x-mms-sender-visibility': ('1',), 'x-mms-read-reply': ('1',), 'x-original-to': ('xxx@xxxx.xxx',), 'x-mms-message-class': ('0',), 'x-mms-delivery-report': ('0',), 'x-mms-mms-version': ('16',), 'delivered-to': ('xxx@xxxx.xxx',), 'x-nokia-ag-version': ('2.0',)},
    attachments=[],
    from_values=EmailAddress(name='', email='xxx@xxxx.xxx'),
    to_values=(EmailAddress(name='', email='xxx@xxxx.xxx'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)