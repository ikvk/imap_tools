import datetime
    
DATA = dict(
    subject='',
    from_='john.q.public@example.com',
    to=('mary@x.test', 'jdoe@example.org', 'one@y.test'),
    cc=('boss@nil.test', 'sysservices@example.net'),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2003, 7, 1, 10, 52, 37, tzinfo=datetime.timezone(datetime.timedelta(0, 7200))),
    date_str='Tue, 1 Jul 2003 10:52:37 +0200',
    text='Hi everyone.\r\n',
    html='',
    headers={'from': ('"Joe Q. Public" <john.q.public@example.com>',), 'to': ('Mary Smith <mary@x.test>, jdoe@example.org, Who? <one@y.test>',), 'cc': ('<boss@nil.test>, "Giant; \\"Big\\" Box" <sysservices@example.net>',), 'date': ('Tue, 1 Jul 2003 10:52:37 +0200',), 'message-id': ('<5678.21-Nov-1997@example.com>',)},
    attachments=[],
    from_values={'email': 'john.q.public@example.com', 'name': 'Joe Q. Public', 'full': 'Joe Q. Public <john.q.public@example.com>'},
    to_values=({'email': 'mary@x.test', 'name': 'Mary Smith', 'full': 'Mary Smith <mary@x.test>'}, {'email': 'jdoe@example.org', 'name': '', 'full': 'jdoe@example.org'}, {'email': 'one@y.test', 'name': 'Who?', 'full': 'Who? <one@y.test>'}),
    cc_values=({'email': 'boss@nil.test', 'name': '', 'full': 'boss@nil.test'}, {'email': 'sysservices@example.net', 'name': 'Giant; "Big" Box', 'full': 'Giant; "Big" Box <sysservices@example.net>'}),
    bcc_values=(),
    reply_to_values=(),
)