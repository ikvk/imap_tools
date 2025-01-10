import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='worse when you use them.',
    from_='xxxxx@xxxxx',
    to=('',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2005, 4, 27, 14, 15, 31, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=61200))),
    date_str='Wed, 27 Apr 2005 14:15:31 -0700',
    text='\r\nXXXXX Xxxxx\r\n',
    html='',
    headers={'mime-version': ('1.0 (Apple Message framework v619.2)',), 'to': ('"xxxxx@xxxxx" <matmail>',), 'message-id': ('<416eaebec6d333ec6939eaf8a7d80724@xxxxx>',), 'content-type': ('multipart/alternative;\r\n        boundary=Apple-Mail-5-1037861608',), 'from': ('"xxxxx@xxxxx" <xxxxx@xxxxx>',), 'subject': ('worse when you use them.',), 'date': ('Wed, 27 Apr 2005 14:15:31 -0700',)},
    attachments=[],
    from_values=EmailAddress(name='xxxxx@xxxxx', email='xxxxx@xxxxx'),
    to_values=(EmailAddress(name='xxxxx@xxxxx', email=''),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)