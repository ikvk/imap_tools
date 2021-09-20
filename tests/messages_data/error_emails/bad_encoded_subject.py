import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='TEST',
    from_='',
    to=(),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(1900, 1, 1, 0, 0),
    date_str='',
    text='TEST\r\n',
    html='',
    headers={'subject': ('=?NONE?B?VEVTVA=?=',)},
    attachments=[],
    from_values=None,
    to_values=(),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)