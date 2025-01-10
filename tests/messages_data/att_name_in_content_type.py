import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='Daily Data: D09.ZPH (Averaged data)',
    from_='status@sender.com',
    to=('data@email.com',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2020, 11, 9, 14, 49, 7, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=57600))),
    date_str='Mon, 09 Nov 2020 14:49:07 -0800 (PST)',
    text='Daily Data: D09.ZPH (Averaged data)\nEmail generated: 10/11/2020 00:04:03.765\nEmail sent: 10/11/2020 00:49:03.125',
    html='',
    headers={'message-id': ('<5fa9c763.1c69fb81.76d95.43d7@mx.google.com>',), 'date': ('Mon, 09 Nov 2020 14:49:07 -0800 (PST)',), 'mime-version': ('1.0',), 'from': ('"Sender" <status@sender.com>',), 'to': ('"Data Email" <data@email.com>',), 'subject': ('Daily Data: D09.ZPH (Averaged data)',), 'content-type': ('multipart/mixed; boundary=--boundary_20_d4727d16-8454-4fa4-9da0-950a95b2c962',)},
    attachments=[
        dict(
            filename='D09.ZPH.txt',
            content_id='',
            content_disposition='',
            content_type='application/octet-stream',
            payload=b'123',
        ),
        ],
    from_values=EmailAddress(name='Sender', email='status@sender.com'),
    to_values=(EmailAddress(name='Data Email', email='data@email.com'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)