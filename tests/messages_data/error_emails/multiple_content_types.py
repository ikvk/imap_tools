import datetime
    
DATA = dict(
    subject='Redacted',
    from_='redacted@flashmail.net',
    to=('redacted@Enron.com',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(1900, 1, 1, 0, 0),
    date_str='',
    text='foo\r\n',
    html='<p>foo</p>\r\n',
    headers={'from': ('<redacted@flashmail.net>',), 'subject': ('Redacted',), 'to': ('<redacted@Enron.com>',), 'message-id': ('<105647271315.NCV17523@x263.net>',), 'mime-version': ('1.0',), 'content-type': ('multipart/alternative; boundary="----_001_5973_47T00ZN9.15SY2428"', 'text/plain')},
    attachments=[],
    from_values={'email': 'redacted@flashmail.net', 'name': '', 'full': 'redacted@flashmail.net'},
    to_values=({'email': 'redacted@Enron.com', 'name': '', 'full': 'redacted@Enron.com'},),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)