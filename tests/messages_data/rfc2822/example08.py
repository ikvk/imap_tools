import datetime
    
DATA = dict(
    subject='Saying Hello',
    from_='jdoe@machine.example',
    to=('mary@example.net',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(1997, 11, 21, 9, 55, 6, tzinfo=datetime.timezone(datetime.timedelta(-1, 64800))),
    date_str='Fri, 21 Nov 1997 09:55:06 -0600',
    text='This is a message just to say hello.\r\nSo, "Hello".\r\n',
    html='',
    headers={'resent-from': ('Mary Smith <mary@example.net>',), 'resent-to': ('Jane Brown <j-brown@other.example>',), 'resent-date': ('Mon, 24 Nov 1997 14:22:01 -0800',), 'resent-message-id': ('<78910@example.net>',), 'from': ('John Doe <jdoe@machine.example>',), 'to': ('Mary Smith <mary@example.net>',), 'subject': ('Saying Hello',), 'date': ('Fri, 21 Nov 1997 09:55:06 -0600',), 'message-id': ('<1234@local.machine.example>',)},
    attachments=[],
    from_values={'email': 'jdoe@machine.example', 'name': 'John Doe', 'full': 'John Doe <jdoe@machine.example>'},
    to_values=({'email': 'mary@example.net', 'name': 'Mary Smith', 'full': 'Mary Smith <mary@example.net>'},),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)