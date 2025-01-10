import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='testing',
    from_='foo@example.com',
    to=('blah@example.com',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2005, 6, 6, 22, 21, 22, tzinfo=datetime.timezone(datetime.timedelta(seconds=7200))),
    date_str='Mon, 6 Jun 2005 22:21:22 +0200',
    text='This is the first part.\r\n',
    html='',
    headers={'mime-version': ('1.0 (Apple Message framework v730)',), 'content-type': ('multipart/mixed; boundary=Apple-Mail-13-196941151',), 'message-id': ('<9169D984-4E0B-45EF-82D4-8F5E53AD7012@example.com>',), 'from': ('foo@example.com',), 'subject': ('testing',), 'date': ('Mon, 6 Jun 2005 22:21:22 +0200',), 'to': ('blah@example.com',)},
    attachments=[
        dict(
            filename='',
            content_id='qbFGyPQAS8',
            content_disposition='inline',
            content_type='image/jpeg',
            payload=b"\x8d\xa9\xa2\xb1*\x86H\x86\xf7\r\x01\x07\x02\xa0\x800\x88\xda\x9a+1\x0b0\t\x06\x05+\x0e\x03\x02\x1a\x05\x000\x80\x06\t*\x86J6\xa6\x8a\xc1\x07\x01\x00\x00\xa0\x82\x05J0\x82\x05F0\x82\x04.\x8d\xa9\xa2\xb1\x02\x02\x04?\xbe\xbaD0\r\x06\t*\x88\xda\x9a+\r\x01\x01\x05\x05\x00011\x0b0\t\x06\x03U\x04\x06\x13\x02F6\xa6\x8a\xc0\n\x06\x03U\x04\n\x13\x03TDC1\x140\x12\x06\x8d\xa9\xa2\xb3\x13\x0bTDC OCES CH\xda\x9a+\r040229115901Z\x17\r06026\xa6\x8a\xc22901Z0\x81\x801\x0b0\t\x06\x03U\x04\x8d\xa9\xa2\xb0K1)0'\x06\x03U\x04\n\x13 H\xda\x9a+. organisatorisk tin6\xa6\x8a\xc4nin",
        ),
        ],
    from_values=EmailAddress(name='', email='foo@example.com'),
    to_values=(EmailAddress(name='', email='blah@example.com'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)