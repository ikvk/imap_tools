import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='Fwd: Signed email causes file attachments',
    from_='xxxxxxxxx.xxxxxxx@gmail.com',
    to=('xxxxx@xxxxxxxxx.com',),
    cc=(),
    bcc=(),
    reply_to=('xxxxxxxxx.xxxxxxx@gmail.com',),
    date=datetime.datetime(2005, 5, 8, 14, 9, 11, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=68400))),
    date_str='Sun, 8 May 2005 14:09:11 -0500',
    text='We should not include these files or vcards as attachments.\r\n\r\n---------- Forwarded message ----------\r\nFrom: xxxxx xxxxxx <xxxxxxxx@xxx.com>\r\nDate: May 8, 2005 1:17 PM\r\nSubject: Signed email causes file attachments\r\nTo: xxxxxxx@xxxxxxxxxx.com\r\n\r\n\r\nHi,\r\n\r\nTest attachments oddly encoded with japanese charset.\r\n\r\n',
    html='',
    headers={'return-path': ('<xxxxxxxxx.xxxxxxx@gmail.com>',), 'message-id': ('<e85734b90505081209eaaa17b@mail.gmail.com>',), 'date': ('Sun, 8 May 2005 14:09:11 -0500',), 'from': ('xxxxxxxxx xxxxxxx <xxxxxxxxx.xxxxxxx@gmail.com>',), 'reply-to': ('xxxxxxxxx xxxxxxx <xxxxxxxxx.xxxxxxx@gmail.com>',), 'to': ('xxxxx xxxx <xxxxx@xxxxxxxxx.com>',), 'subject': ('Fwd: Signed email causes file attachments',), 'in-reply-to': ('<F6E2D0B4-CC35-4A91-BA4C-C7C712B10C13@mac.com>',), 'mime-version': ('1.0',), 'content-type': ('multipart/mixed; \r\n\tboundary="----=_Part_5028_7368284.1115579351471"',), 'references': ('<F6E2D0B4-CC35-4A91-BA4C-C7C712B10C13@mac.com>',)},
    attachments=[
        dict(
            filename='01 Quien Te Dij�at. Pitbull.mp3',
            content_id='',
            content_disposition='attachment',
            content_type='application/octet-stream',
            payload=b'0\x80\x06\t*\x86H\x86\xf7\r\x01\x07\x02\xa0\x800\x80\x02\x01\x011\x0b0\t\x06\x05+\x0e\x03\x02\x1a\x05\x000\x80\x06\t*\x86H\x86\xf7\r\x01\x07\x01\x00\x00\xa0\x82\x06\x140\x82\x02\xcd0\x82\x026\xa0\x03\x02\x01\x02\x02\x03\x0e\\\xf90\r\x06\t*\x86H\x86\xf7\r\x01\x01\x04\x05\x000b1\x0b0\t\x06\x03U\x04\x06\x13\x02ZA1%0#\x06\x03U\x04\n\x13\x1cThawte Consulting (Pty) Ltd.1,0*\x06\x03U\x04\x03\x13#Thawte Personal Freemail Issuing CA0\x1e\x17\r050329093910Z\x17\r060329093910Z0B1\x1f0\x1d\x06\x03U\x04\x03\x13\x16Thawte Freemail Member1\x1f0\x1d\x06\t*\x86H\x86\xf7\r\x01\t\x01\x16\x10smhaunch@mac.com0\x82\x01"0\r\x06\t*\x86H\x86\xf7\r\x01\x01\x01\x05\x00\x03\x82\x01\x0f\x000\x82\x01\n\x02\x82\x01\x01\x00\x9f\xdd\x1d>\xc6\x12\xdc\xb8\xdf1\x8d\xb5\xd4\xe4\x98\xac4\x0b\xcf\x03X>P\x0b\xef\xef\xf4\\\x0f\xa4w/?\xad\x19\xf2\x10qF\xc2\x13B\x0eh4\x07\xaaq\x0b\xbc\xf7\xc7\x12C\xff\xc1\x9f\t\xdf\x88aE\rQ\x05y\x9b\xd3$\xc5\xf3\xfd\xa55WeR\x18-\xa0p',
        ),
        ],
    from_values=EmailAddress(name='xxxxxxxxx xxxxxxx', email='xxxxxxxxx.xxxxxxx@gmail.com'),
    to_values=(EmailAddress(name='xxxxx xxxx', email='xxxxx@xxxxxxxxx.com'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(EmailAddress(name='xxxxxxxxx xxxxxxx', email='xxxxxxxxx.xxxxxxx@gmail.com'),),
)