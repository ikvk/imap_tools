import datetime
    
DATA = dict(
    subject='',
    from_='john.q.public@example.com',
    to=('mary@example.net', 'jdoe@test.example'),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2003, 7, 1, 10, 52, 37, tzinfo=datetime.timezone(datetime.timedelta(0, 7200))),
    date_str='Tue, 1 Jul 2003 10:52:37 +0200',
    text='Hi everyone.\r\n',
    html='',
    headers={'from': ('Joe Q. Public <john.q.public@example.com>',), 'to': ('Mary Smith <@machine.tld:mary@example.net>, , jdoe@test   . example',), 'date': ('Tue, 1 Jul 2003 10:52:37 +0200',), 'message-id': ('<5678.21-Nov-1997@example.com>',)},
    attachments=[],
    from_values={'email': 'john.q.public@example.com', 'name': 'Joe Q. Public', 'full': 'Joe Q. Public <john.q.public@example.com>'},
    to_values=({'email': 'mary@example.net', 'name': 'Mary Smith', 'full': 'Mary Smith <mary@example.net>'}, {'email': 'jdoe@test.example', 'name': '', 'full': 'jdoe@test.example'}),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)