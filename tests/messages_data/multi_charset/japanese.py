import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='まみむめも',
    from_='raasdnil@gmail.com',
    to=('raasdnil@gmail.com',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(1900, 1, 1, 0, 0),
    date_str='',
    text='かきくえこ\n\n-- \nhttp://lindsaar.net/\nRails, RSpec and Life blog....\n',
    html='',
    headers={'mime-version': ('1.0',), 'subject': ('=?UTF-8?B?44G+44G/44KA44KB44KC?=',), 'from': ('Mikel Lindsaar <raasdnil@gmail.com>',), 'to': ('=?UTF-8?B?44G/44GR44KL?= <raasdnil@gmail.com>',), 'content-type': ('text/plain; charset=UTF-8',), 'content-transfer-encoding': ('base64',)},
    attachments=[],
    from_values=EmailAddress(name='Mikel Lindsaar', email='raasdnil@gmail.com'),
    to_values=(EmailAddress(name='みける', email='raasdnil@gmail.com'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)