import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='Repeated recipients',
    from_='sender@example.com',
    to=('team@example.com', 'plain@example.com'),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2026, 10, 14, 12, 10, tzinfo=datetime.timezone.utc),
    date_str='Tue, 14 Oct 2026 12:10:00 +0000',
    text='Body for repeated recipients test.',
    html='',
    headers={'from': ('Sender <sender@example.com>',), 'to': ('Team =?utf-8?q?M=C3=BCnchen?= <team@example.com>', 'Plain Name <plain@example.com>'), 'subject': ('=?utf-8?q?Repeated_recipients?=',), 'date': ('Tue, 14 Oct 2026 12:10:00 +0000',), 'message-id': ('<repeated-recipients-001@example.com>',), 'mime-version': ('1.0',), 'content-type': ('text/plain; charset="utf-8"',), 'content-transfer-encoding': ('7bit',)},
    attachments=[],
    from_values=EmailAddress(name='Sender', email='sender@example.com'),
    to_values=(EmailAddress(name='Team München', email='team@example.com'), EmailAddress(name='Plain Name', email='plain@example.com')),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)