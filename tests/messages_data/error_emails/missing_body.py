import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='REDACTED',
    from_='redacted@attglobal.net',
    to=('', '@mailman.enron.com'),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2001, 11, 27, 15, 2, 35, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=57600))),
    date_str='Tue, 27 Nov 2001 15:02:35 -0800',
    text='',
    html='',
    headers={'message-id': ('<001301c17797$9cd0ef30$a3ab620c@vaio>',), 'from': ('"SCS_2" <redacted@attglobal.net>',), 'to': ('<Undisclosed-Recipient:@mailman.enron.com;>',), 'subject': ('REDACTED',), 'date': ('Tue, 27 Nov 2001 15:02:35 -0800',), 'mime-version': ('1.0',), 'content-type': ('multipart/mixed;\r\n\tboundary="----=_NextPart_000_000F_01C17754.8C3CAF30"',), 'x-priority': ('3',), 'x-msmail-priority': ('Normal',), 'x-mailer': ('Microsoft Outlook Express 5.00.2919.6700',), 'x-mimeole': ('Produced By Microsoft MimeOLE V5.00.2919.6700',), 'return-path': ('redacted@attglobal.net',)},
    attachments=[],
    from_values=EmailAddress(name='SCS_2', email='redacted@attglobal.net'),
    to_values=(EmailAddress(name='Undisclosed-Recipient', email=''), EmailAddress(name='', email='@mailman.enron.com')),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)