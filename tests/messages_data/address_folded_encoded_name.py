import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='Folded display name test',
    from_='team@example.com',
    to=('folded@example.com',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2026, 10, 14, 12, 5, tzinfo=datetime.timezone.utc),
    date_str='Tue, 14 Oct 2026 12:05:00 +0000',
    text='Body for folded display name test.',
    html='',
    headers={'from': ('Team\r\n =?utf-8?q?M=C3=BCnchen?= <team@example.com>',), 'to': ('Folded =?utf-8?q?M=C3=BCnchen?=\r\n <folded@example.com>',), 'subject': ('=?utf-8?q?Folded_display_name_test?=',), 'date': ('Tue, 14 Oct 2026 12:05:00 +0000',), 'message-id': ('<folded-encoded-001@example.com>',), 'mime-version': ('1.0',), 'content-type': ('text/plain; charset="utf-8"',), 'content-transfer-encoding': ('7bit',)},
    attachments=[],
    from_values=EmailAddress(name='Team München', email='team@example.com'),
    to_values=(EmailAddress(name='Folded München', email='folded@example.com'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)