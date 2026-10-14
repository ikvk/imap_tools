import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='HTML quoted-printable body ending on a soft line break',
    from_='sender@example.invalid',
    to=('recipient@example.invalid',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2026, 7, 6, 6, 6, 6, tzinfo=datetime.timezone.utc),
    date_str='Mon, 6 Jul 2026 06:06:06 +0000',
    text='',
    html='<html>\n<body>\n<p>The needle qptrailinghtml sits in the aggregated part.</p>\n</body>\n</html>\n',
    headers={'to': ('recipient@example.invalid',), 'from': ('sender@example.invalid',), 'subject': ('HTML quoted-printable body ending on a soft line break',), 'message-id': ('<qp-trailing-equals-html@example.invalid>',), 'date': ('Mon, 6 Jul 2026 06:06:06 +0000',), 'mime-version': ('1.0',), 'content-type': ('text/html; charset="utf-8"',), 'content-transfer-encoding': ('quoted-printable',)},
    attachments=[],
    from_values=EmailAddress(name='', email='sender@example.invalid'),
    to_values=(EmailAddress(name='', email='recipient@example.invalid'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)