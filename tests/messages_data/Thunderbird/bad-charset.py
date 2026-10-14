import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='plaintext + HMTL, both with a bad charset',
    from_='test@example.com',
    to=('test@example.com',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2017, 12, 30, 19, 31, 21, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))),
    date_str='Sat, 30 Dec 2017 19:31:21 +0100',
    text='Despite the bad charset we can find the search term Mtterhorn.\nNote that the umlaut is encoded in windows-1252.\n\n',
    html='<body>\nDespite the bad charset we can find the search term Matterhörn.\nNote that the umlaut is encoded in UTF-8.</body>\n',
    headers={'to': ('test@example.com',), 'from': ('test@example.com',), 'subject': ('plaintext + HMTL, both with a bad charset',), 'message-id': ('<a30f750d-d56c-8a52-971c-f95a131e8332@example.com>',), 'date': ('Sat, 30 Dec 2017 19:31:21 +0100',), 'user-agent': ('Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101\n Thunderbird/59.0a1',), 'mime-version': ('1.0',), 'content-type': ('multipart/alternative;\n boundary="------------FAB286B8794CC63C0A0FD1BB"',)},
    attachments=[],
    from_values=EmailAddress(name='', email='test@example.com'),
    to_values=(EmailAddress(name='', email='test@example.com'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)