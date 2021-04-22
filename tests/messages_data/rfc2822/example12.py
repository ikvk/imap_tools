import datetime
    
DATA = dict(
    subject='Saying Hello',
    from_='jdoe@machine.example',
    to=('mary@example.net',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(1997, 11, 21, 9, 55, 6, tzinfo=datetime.timezone.utc),
    date_str='21 Nov 97 09:55:06 GMT',
    text='This is a message just to say hello.\r\nSo, "Hello".\r\n',
    html='',
    headers={'from': ('John Doe <jdoe@machine.example>',), 'to': ('Mary Smith <mary@example.net>',), 'subject': ('Saying Hello',), 'date': ('21 Nov 97 09:55:06 GMT',), 'message-id': ('<1234@local.machine.example>',)},
    attachments=[],
    from_values={'email': 'jdoe@machine.example', 'name': 'John Doe', 'full': 'John Doe <jdoe@machine.example>'},
    to_values=({'email': 'mary@example.net', 'name': 'Mary Smith', 'full': 'Mary Smith <mary@example.net>'},),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)