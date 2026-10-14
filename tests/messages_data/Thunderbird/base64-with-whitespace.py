import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='Bug 1487421 - BASE64 MIME body and attachment with empty lines in between',
    from_='from@example.com',
    to=('to@example.com',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2018, 8, 31, 16, 33, tzinfo=datetime.timezone(datetime.timedelta(seconds=7200))),
    date_str='Tue, 31 Aug 2018 16:33:00 +0200',
    text='abcdefghijklmnopqrstuvwxyz',
    html='',
    headers={'date': ('Tue, 31 Aug 2018 16:33:00 +0200',), 'from': ('From <from@example.com>',), 'to': ('To <to@example.com>',), 'subject': ('Bug 1487421 - BASE64 MIME body and attachment with empty lines in between',), 'mime-version': ('1.0',), 'message-id': ('<1dcZe4@example.com>',), 'content-type': ('multipart/mixed;\r\n boundary="------------DA562B250842CC7332F16476"',)},
    attachments=[
        dict(
            filename='test.txt',
            content_id='',
            content_disposition='attachment',
            content_type='text/plain',
            payload=b'abcdefghijklmnopqrstuvwxyz',
        ),
        ],
    from_values=EmailAddress(name='From', email='from@example.com'),
    to_values=(EmailAddress(name='To', email='to@example.com'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)