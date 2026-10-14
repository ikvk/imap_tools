import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='ISO-2022-JP and 7bit containing =67 and hence looking like quoted-printable',
    from_='test@example.com',
    to=('test@example.com',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2018, 4, 3, 19, 9, 16, tzinfo=datetime.timezone(datetime.timedelta(seconds=32400))),
    date_str='Tue, 3 Apr 2018 19:09:16 +0900',
    text='現況\r\n\r\n',
    html='',
    headers={'to': ('test@example.com',), 'from': ('test@example.com',), 'subject': ('ISO-2022-JP and 7bit containing =67 and hence looking like quoted-printable',), 'message-id': ('<10a2aa17-e92f-417c-864e-575d4e371702@example.com>',), 'date': ('Tue, 3 Apr 2018 19:09:16 +0900',), 'user-agent': ('Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101\r\n Thunderbird/52.6.0',), 'mime-version': ('1.0',), 'content-type': ('text/plain; charset=ISO-2022-JP; format=flowed',), 'content-language': ('ja-JP',), 'content-transfer-encoding': ('7bit',)},
    attachments=[],
    from_values=EmailAddress(name='', email='test@example.com'),
    to_values=(EmailAddress(name='', email='test@example.com'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)