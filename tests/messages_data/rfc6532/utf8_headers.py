import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='Säying Hello',
    from_='jdöe@mächine.example',
    to=('märy@exämple.net',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(1900, 1, 1, 0, 0),
    date_str='',
    text='body\r\n',
    html='',
    headers={'from': ('"J\udcc3\udcb6hn Doe" <jd\udcc3\udcb6e@m\udcc3\udca4chine.example>',), 'to': ('"M\udcc3\udca4ry Smith" <m\udcc3\udca4ry@ex\udcc3\udca4mple.net>',), 'subject': ('S\udcc3\udca4ying Hello',)},
    attachments=[],
    from_values=EmailAddress(name='Jöhn Doe', email='jdöe@mächine.example'),
    to_values=(EmailAddress(name='Märy Smith', email='märy@exämple.net'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)