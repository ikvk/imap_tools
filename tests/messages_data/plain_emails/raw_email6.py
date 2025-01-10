import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='',
    from_='xxx@xxxx.xxx',
    to=('xxxxxxxxxxx@xxxx.xxxx.xxx',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2005, 5, 10, 15, 27, 3, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=68400))),
    date_str='Tue, 10 May 2005 15:27:03 -0500',
    text="Test test. Hi. Waving. m\r\n\r\n----------------------------------------------------------------\r\nSent via Bell Mobility's Text Messaging service. \r\nEnvoy par le service de messagerie texte de Bell Mobilit.\r\n----------------------------------------------------------------\r\n",
    html='',
    headers={'return-path': ('<xxx@xxxx.xxx>',), 'received': ('from xxx.xxxx.xxx by xxx.xxxx.xxx with ESMTP id C1B953B4CB6 for <xxxxx@Exxx.xxxx.xxx>; Tue, 10 May 2005 15:27:05 -0500', 'from SMS-GTYxxx.xxxx.xxx by xxx.xxxx.xxx with ESMTP id ca for <xxxxx@Exxx.xxxx.xxx>; Tue, 10 May 2005 15:27:04 -0500', 'from xxx.xxxx.xxx by SMS-GTYxxx.xxxx.xxx with ESMTP id j4AKR3r23323 for <xxxxx@Exxx.xxxx.xxx>; Tue, 10 May 2005 15:27:03 -0500'), 'date': ('Tue, 10 May 2005 15:27:03 -0500',), 'from': ('xxx@xxxx.xxx',), 'sender': ('xxx@xxxx.xxx',), 'to': ('xxxxxxxxxxx@xxxx.xxxx.xxx',), 'message-id': ('<xxx@xxxx.xxx>',), 'x-original-to': ('xxxxxxxxxxx@xxxx.xxxx.xxx',), 'delivered-to': ('xxx@xxxx.xxx',), 'importance': ('normal',), 'content-type': ('text/plain; charset=us-ascii',)},
    attachments=[],
    from_values=EmailAddress(name='', email='xxx@xxxx.xxx'),
    to_values=(EmailAddress(name='', email='xxxxxxxxxxx@xxxx.xxxx.xxx'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)