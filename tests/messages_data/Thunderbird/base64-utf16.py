import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='base64 encoded UTF-16 body',
    from_='sender@test.invalid',
    to=('recipient@test.invalid',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2026, 9, 18, 12, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=10800))),
    date_str='Fri, 18 Sep 2026 12:00:00 +0300',
    text='utf16Marker eins\r\nzwei utf16End',
    html='',
    headers={'from': ('sender@test.invalid',), 'to': ('recipient@test.invalid',), 'subject': ('base64 encoded UTF-16 body',), 'message-id': ('<base64-utf16@test.invalid>',), 'date': ('Fri, 18 Sep 2026 12:00:00 +0300',), 'mime-version': ('1.0',), 'content-type': ('text/plain; charset=UTF-16',), 'content-transfer-encoding': ('base64',)},
    attachments=[],
    from_values=EmailAddress(name='', email='sender@test.invalid'),
    to_values=(EmailAddress(name='', email='recipient@test.invalid'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)