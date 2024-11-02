import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='Пример email с вложением и Content-ID',
    from_='sender@example.com',
    to=('recipient@example.com',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(1900, 1, 1, 0, 0),
    date_str='',
    text='текстовое сообщение с вложением, у которого есть Content-ID.\r\n',
    html='',
    headers={'from': ('sender@example.com',), 'to': ('recipient@example.com',), 'subject': ('\udcd0\udc9f\udcd1\udc80\udcd0\udcb8\udcd0\udcbc\udcd0\udcb5\udcd1\udc80 email \udcd1\udc81 \udcd0\udcb2\udcd0\udcbb\udcd0\udcbe\udcd0\udcb6\udcd0\udcb5\udcd0\udcbd\udcd0\udcb8\udcd0\udcb5\udcd0\udcbc \udcd0\udcb8 Content-ID',), 'mime-version': ('1.0',), 'content-type': ('multipart/mixed; boundary="boundary123"',)},
    attachments=[
        dict(
            filename='example.png',
            content_id='Test0 "漢字" mid1 "漢字" tail2',
            content_disposition='attachment',
            content_type='image/png',
            payload=b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x05\x00\x00\x00\x00\x15\x00\x00\x00\x13w\xc7u\xc0\x00\x00\x00\x12QS\x91+\x90\x98 ',
        ),
        ],
    from_values=EmailAddress(name='', email='sender@example.com'),
    to_values=(EmailAddress(name='', email='recipient@example.com'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)