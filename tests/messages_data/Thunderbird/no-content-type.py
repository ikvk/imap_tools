import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='Message with no content-type in header',
    from_='sender@example.invalid',
    to=('recipient@example.invalid',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(1900, 1, 1, 0, 0),
    date_str='',
    text='Try a Thunderbird Quick Filter for waldo in the message body.\n',
    html='',
    headers={'from': ('sender@example.invalid',), 'to': ('recipient@example.invalid',), 'subject': ('Message with no content-type in header',), 'message-id': ('<no-content-type@example.invalid>',)},
    attachments=[],
    from_values=EmailAddress(name='', email='sender@example.invalid'),
    to_values=(EmailAddress(name='', email='recipient@example.invalid'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)