import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='5 HTML + embedded image',
    from_='test@example.com',
    to=('test@example.com',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2017, 12, 30, 19, 26, 23, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))),
    date_str='Sat, 30 Dec 2017 19:26:23 +0100',
    text='',
    html='<html>\r\n  <head>\r\n\r\n    <meta http-equiv="content-type" content="text/html; charset=utf-8">\r\n  </head>\r\n  <body text="#000000" bgcolor="#FFFFFF">\r\n    <p><tt>Search for huhu</tt></p>\r\n    <p><img src="cid:part1.8C5E6A81.D0C1B91A@jorgk.com" alt=""></p>\r\n  </body>\r\n</html>',
    headers={'to': ('test@example.com',), 'from': ('test@example.com',), 'subject': ('5 HTML + embedded image',), 'message-id': ('<c1ddcd5d-71c1-9c9d-1b81-e3b9abb99030@example.com>',), 'date': ('Sat, 30 Dec 2017 19:26:23 +0100',), 'user-agent': ('Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101\n Thunderbird/59.0a1',), 'mime-version': ('1.0',), 'content-type': ('multipart/related;\n boundary="------------B2BBD36A919AB2B2F84E2469"',), 'content-language': ('en-GB',)},
    attachments=[
        dict(
            filename='kigaaldcbanejcbi.png',
            content_id='part1.8C5E6A81.D0C1B91A@jorgk.com',
            content_disposition='inline',
            content_type='image/png',
            payload=b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10\x08\x02\x00\x00\x00\x90\x91h6\x00\x00\x00\x01sRGB\x00\xae\xce\x1c\xe9\x00\x00\x00\x04gAMA\x00\x00\xb1\x8f\x0b\xfca\x05\x00\x00\x00\tpHYs\x00\x00\x0e\xc3\x00\x00\x0e\xc3\x01\xc7o\xa8d\x00\x00\x00\x12tEXtSoftware\x00Greenshot^U\x08\x05\x00\x00\x00iIDAT8O\xdd\xd0;\x12\x80 \x0cE\xd1\xecL>n\x07q\xffM|\x04F2\x88\x80\xadon\xc5p(\xa0\xdd\x9e\xc8\x9b\xa8\n\xdd\x9cM\xfd\x17\x10\x91\xbe\x9a+\xc0\xe3\xb6\xe4L\xcc\xc1\x00\x88\xd1\xaf\x94Z`\xb7#\x9d\x121s\xd7\x8c@\xd7L\x00\xd6\x989\xc0\xb4Y\x02\xd8mV\x01&\xe6\xf1\xad\x03\x80\xe1\xbc\x82\xda;\xc0>\x02\xe6\x0b\xcbE9\xc5E)/\xc9\x00\x00\x00\x00IEND\xaeB`\x82',
        ),
        ],
    from_values=EmailAddress(name='', email='test@example.com'),
    to_values=(EmailAddress(name='', email='test@example.com'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)