import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='Xxxxxx',
    from_='xxxxxx@xxxxxxxx.xxx',
    to=('xxxxxxx@xxxxxxxxxxx.xxx',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2012, 4, 6, 1, 1, 1, tzinfo=datetime.timezone.utc),
    date_str='Fri, 6 Apr 2012 01:01:01 +0000',
    text='Test\r\n',
    html='<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/1999/REC-html401-19991224/strict.dtd"><html><head>\r\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8">\r\n<title>Test</title>\r\n<body>\r\n<p>Test</p>\r\n</body>\r\n',
    headers={'received': ('from xxxx.xxxxxxx.xxx (127.0.0.1) by\r\n xxxx.xxxxxxxx.xxx (127.0.01) with Microsoft SMTP Server id\r\n 11.1.111.1; Thu, 5 Apr 2012 01:01:01 -0700',), 'message-id': ('<e4b473$b3jkq@xxxx.xxxx.xxxxxxxx.xxx>',), 'to': ('<xxxxxxx@xxxxxxxxxxx.xxx>',), 'subject': ('Xxxxxx',), 'date': ('Fri, 6 Apr 2012 01:01:01 +0000',), 'from': ('Xxxxx <xxxxxx@xxxxxxxx.xxx>',), 'x-mailer': ('PHP/5.2.6',), 'content-type': ('multipart/mixed;\r\n\tboundary="----=_NextPart_476c4fde88e507bb8028170e8cf47c73"',), 'mime-version': ('1.0',)},
    attachments=[
        dict(
            filename='LOGO.png',
            content_id='LOGO.png',
            content_disposition='attachment',
            content_type='application/octetstream',
            payload=b'H\xd2\x0f',
        ),
        ],
    from_values=EmailAddress(name='Xxxxx', email='xxxxxx@xxxxxxxx.xxx'),
    to_values=(EmailAddress(name='', email='xxxxxxx@xxxxxxxxxxx.xxx'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)