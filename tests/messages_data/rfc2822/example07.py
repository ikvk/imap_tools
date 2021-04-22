import datetime
    
DATA = dict(
    subject='Re: Saying Hello',
    from_='jdoe@machine.example',
    to=('smith@home.example',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(1997, 11, 21, 11, 0, tzinfo=datetime.timezone(datetime.timedelta(-1, 64800))),
    date_str='Fri, 21 Nov 1997 11:00:00 -0600',
    text='This is a reply to your reply.\r\n',
    html='',
    headers={'to': ('"Mary Smith: Personal Account" <smith@home.example>',), 'from': ('John Doe <jdoe@machine.example>',), 'subject': ('Re: Saying Hello',), 'date': ('Fri, 21 Nov 1997 11:00:00 -0600',), 'message-id': ('<abcd.1234@local.machine.tld>',), 'in-reply-to': ('<3456@example.net>',), 'references': ('<1234@local.machine.example> <3456@example.net>',)},
    attachments=[],
    from_values={'email': 'jdoe@machine.example', 'name': 'John Doe', 'full': 'John Doe <jdoe@machine.example>'},
    to_values=({'email': 'smith@home.example', 'name': 'Mary Smith: Personal Account', 'full': 'Mary Smith: Personal Account <smith@home.example>'},),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)