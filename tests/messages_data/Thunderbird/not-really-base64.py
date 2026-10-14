import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject="claims to be base64 but isn't",
    from_='sender@test.invalid',
    to=('recipient@test.invalid',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2026, 9, 18, 12, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=10800))),
    date_str='Fri, 18 Sep 2026 12:00:00 +0300',
    text='@rۚ\\jǺ;Z{^',
    html='',
    headers={'from': ('sender@test.invalid',), 'to': ('recipient@test.invalid',), 'subject': ("claims to be base64 but isn't",), 'message-id': ('<not-really-base64@test.invalid>',), 'date': ('Fri, 18 Sep 2026 12:00:00 +0300',), 'mime-version': ('1.0',), 'content-type': ('text/plain; charset=UTF-8',), 'content-transfer-encoding': ('base64',)},
    attachments=[],
    from_values=EmailAddress(name='', email='sender@test.invalid'),
    to_values=(EmailAddress(name='', email='recipient@test.invalid'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)