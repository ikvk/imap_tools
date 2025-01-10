import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='test',
    from_='from@example.com',
    to=('unknown@example.com',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2014, 5, 28, 17, 18, 19, tzinfo=datetime.timezone(datetime.timedelta(seconds=32400))),
    date_str='Wed, 28 May 2014 17:18:19 +0900 (JST)',
    text='스티해\r\n',
    html='',
    headers={'delivered-to': ('unknown@example.com',), 'date': ('Wed, 28 May 2014 17:18:19 +0900 (JST)',), 'from': ('from@example.com',), 'to': ('unknown@example.com',), 'subject': ('test',), 'message-id': ('<from@example.com>',), 'mime-version': ('1.0',), 'content-type': ('text/plain; charset="ks_c_5601-1987"',), 'content-transfer-encoding': ('8bit',)},
    attachments=[],
    from_values=EmailAddress(name='', email='from@example.com'),
    to_values=(EmailAddress(name='', email='unknown@example.com'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)