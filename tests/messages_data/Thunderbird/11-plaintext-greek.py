import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='11 plaintext - Greek - ISO-8859-7',
    from_='test@example.com',
    to=('test@example.com',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2017, 12, 30, 19, 15, 38, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))),
    date_str='Sat, 30 Dec 2017 19:15:38 +0100',
    text='Search for Greek text Καλησπέρα\n\n',
    html='',
    headers={'to': ('test@example.com',), 'from': ('test@example.com',), 'subject': ('11 plaintext - Greek - ISO-8859-7',), 'message-id': ('<9ec4f4cb-b14b-aed6-a042-58897d12e4a9@example.com>',), 'date': ('Sat, 30 Dec 2017 19:15:38 +0100',), 'user-agent': ('Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101\n Thunderbird/59.0a1',), 'mime-version': ('1.0',), 'content-type': ('text/plain; charset=ISO-8859-7; format=flowed',), 'content-transfer-encoding': ('8bit',)},
    attachments=[],
    from_values=EmailAddress(name='', email='test@example.com'),
    to_values=(EmailAddress(name='', email='test@example.com'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)