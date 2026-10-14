import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='Test mixed encoded names',
    from_='team@example.com',
    to=('joerg@example.com',),
    cc=('andre@example.com',),
    bcc=('jane@example.com',),
    reply_to=('reply@example.com',),
    date=datetime.datetime(2026, 10, 14, 12, 0, tzinfo=datetime.timezone.utc),
    date_str='Tue, 14 Oct 2026 12:00:00 +0000',
    text='Body for mixed encoded display names test.',
    html='',
    headers={'from': ('Team =?utf-8?q?M=C3=BCnchen?= <team@example.com>',), 'to': ('=?utf-8?q?J=C3=B6rg?= Example <joerg@example.com>',), 'cc': ('=?iso-8859-1?q?Andr=E9?= =?utf-8?q?_M=C3=BCller?= <andre@example.com>',), 'bcc': ('=?utf-8?q?Doe=2C_Jane?= Team <jane@example.com>',), 'reply-to': ('Team =?utf-8?q?M=C3=BCnchen?= <reply@example.com>',), 'subject': ('=?utf-8?q?Test_mixed_encoded_names?=',), 'date': ('Tue, 14 Oct 2026 12:00:00 +0000',), 'message-id': ('<mixed-encoded-001@example.com>',), 'mime-version': ('1.0',), 'content-type': ('text/plain; charset="utf-8"',), 'content-transfer-encoding': ('7bit',)},
    attachments=[],
    from_values=EmailAddress(name='Team München', email='team@example.com'),
    to_values=(EmailAddress(name='Jörg Example', email='joerg@example.com'),),
    cc_values=(EmailAddress(name='André Müller', email='andre@example.com'),),
    bcc_values=(EmailAddress(name='Doe, Jane Team', email='jane@example.com'),),
    reply_to_values=(EmailAddress(name='Team München', email='reply@example.com'),),
)