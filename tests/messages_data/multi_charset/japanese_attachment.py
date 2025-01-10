import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='testing',
    from_='raasdnil@gmail.com',
    to=('raasdnil@gmail.com',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2009, 10, 16, 23, 39, 34, tzinfo=datetime.timezone(datetime.timedelta(seconds=39600))),
    date_str='Fri, 16 Oct 2009 23:39:34 +1100',
    text='testing\r\n\r\n-- \r\nhttp://lindsaar.net/\r\nRails, RSpec and Life blog....\r\n',
    html='',
    headers={'mime-version': ('1.0',), 'received': ('by 10.231.35.72 with HTTP; Fri, 16 Oct 2009 05:39:34 -0700 (PDT)',), 'date': ('Fri, 16 Oct 2009 23:39:34 +1100',), 'delivered-to': ('raasdnil@gmail.com',), 'message-id': ('<57a815bf0910160539m64240421gb35ea52e101aedbc@mail.gmail.com>',), 'subject': ('testing',), 'from': ('Mikel Lindsaar <raasdnil@gmail.com>',), 'to': ('Mikel Lindsaar <raasdnil@gmail.com>',), 'content-type': ('multipart/mixed; boundary=00032557395e3572cf04760cb060',)},
    attachments=[
        dict(
            filename='てすと.txt',
            content_id='',
            content_disposition='attachment',
            content_type='text/plain',
            payload=b'this is a test\n\xe3\x81\x93\xe3\x82\x8c\xe3\x82\x8f\xe3\x81\xa6\xe3\x81\x99\xe3\x81\xa8',
        ),
        ],
    from_values=EmailAddress(name='Mikel Lindsaar', email='raasdnil@gmail.com'),
    to_values=(EmailAddress(name='Mikel Lindsaar', email='raasdnil@gmail.com'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)