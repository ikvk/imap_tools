import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='Redacted',
    from_='redacted@example.com',
    to=('redacted@example.com',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2002, 1, 22, 14, 35, 28, tzinfo=datetime.timezone.utc),
    date_str='Tue, 22 Jan 2002 14:35:28 UT',
    text='',
    html='',
    headers={'message-id': ('<200201221435.g0MEZP927213@mailman.enron.com>',), 'content-type': ('multipart/related; boundary="_----------=_10117101281980"',), 'mime-version': ('1.0',), 'date': ('Tue, 22 Jan 2002 14:35:28 UT',), 'subject': ('Redacted',), 'to': ('redacted@example.com',), 'from': ('redacted@example.com',), 'return-path': ('redacted@example.com',)},
    attachments=[],
    from_values=EmailAddress(name='', email='redacted@example.com'),
    to_values=(EmailAddress(name='', email='redacted@example.com'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)