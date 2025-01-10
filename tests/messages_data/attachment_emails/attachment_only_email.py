import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='this message JUST contains an attachment',
    from_='rfinnie@domain.dom',
    to=('bob@domain.dom',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2003, 10, 23, 22, 40, 49, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=61200))),
    date_str='23 Oct 2003 22:40:49 -0700',
    text='',
    html='',
    headers={'subject': ('this message JUST contains an attachment',), 'from': ('Ryan Finnie <rfinnie@domain.dom>',), 'to': ('bob@domain.dom',), 'content-disposition': ('attachment; filename=blah.gz',), 'content-transfer-encoding': ('base64',), 'content-description': ('Attachment has identical content to above foo.gz',), 'message-id': ('<1066974048.4264.62.camel@localhost>',), 'mime-version': ('1.0',), 'date': ('23 Oct 2003 22:40:49 -0700',), 'content-type': ('application/x-gzip; NAME=blah.gz',)},
    attachments=[
        dict(
            filename='blah.gz',
            content_id='',
            content_disposition='attachment',
            content_type='application/x-gzip',
            payload=b'J\xe6\xe3y\xcbm\x86+&z\xcb\x1a\x81\xe2TI7(\x9e\xd6\xa2\x9e\xc6\xa7j\xdbZr\x19\x9e\x9e\xd1k\xa2drjqb\x9ex\x9e\xad\xf8\xa7\x9e\'\x9d\xa2f\xa2\x9d\xda&N\x86\xe8m\xda&j)\xdd\xa2`\xa8\x9e\xd7\xa7\xb48\xac\xa6\x8b"\xb6*\'j\xdbZr\x19\x9e\x9e\xd7\xe2\x95\xe9\xda\x99\xe0\x1b\x95\xa8`\xcc*\'\xb5\xe9\xedO*^j\x9ae\x89\xc6\xad\x8a\x89\xff\xc6\x0c\xe2\xa6v\xa6x\x06\xe5j\x183\n\x89\xedz{S\xad\xa9\xec}\xea\xc4\x9d\xca\x1d\x8ax\x1bj\xc7\xba\xe0*\'\xb5\xe9\xed\r\xeb\x1c\xae*m\x8a\x89\xc0\xb6\xd6\x9c\x86g\xa7\xb6\x16\xac\x89\xd7\xa7\xb6\'\x1a\x95\xca\'\xb5\xe9\xed\xb6\x86\x9b\xa2\xf7\x9f\xa2\x8831\xeb,j\x07\x88w]:\xeb\xde\xf8\xd3\x8f8\xdb\xae:\xd9\xc6\xa6zYhq\xa9a\xa2\xcbL\x8ag\x95z\xbb"\xa2}t\r\xab^\xdbs\x9c\xb7m4\xdfm\xb8\xd3\x8ft\xefM\x07\xe2\xc2\x008pf\x0f\xc0\x00\xe2\xf3\x0b\xd5s\xf2Tr\x12\xcbR\xcbT\x922\xf3\x12\xd4r\x13Uy\x00\x80\x1d\xb7\xbb\xeb\x85\x80',
        ),
        ],
    from_values=EmailAddress(name='Ryan Finnie', email='rfinnie@domain.dom'),
    to_values=(EmailAddress(name='', email='bob@domain.dom'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)