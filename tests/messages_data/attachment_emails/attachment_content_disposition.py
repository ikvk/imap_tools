import datetime
    
DATA = dict(
    subject='testing',
    from_='foo@example.com',
    to=('blah@example.com',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2005, 6, 6, 22, 21, 22, tzinfo=datetime.timezone(datetime.timedelta(0, 7200))),
    date_str='Mon, 6 Jun 2005 22:21:22 +0200',
    text='This is the first part.\r\n',
    html='',
    headers={'mime-version': ('1.0 (Apple Message framework v730)',), 'content-type': ('multipart/mixed; boundary=Apple-Mail-13-196941151',), 'message-id': ('<9169D984-4E0B-45EF-82D4-8F5E53AD7012@example.com>',), 'from': ('foo@example.com',), 'subject': ('testing',), 'date': ('Mon, 6 Jun 2005 22:21:22 +0200',), 'to': ('blah@example.com',)},
    attachments=[
        dict(
            filename='api.rb',
            content_id='',
            content_disposition='attachment',
            content_type='text/x-ruby-script',
            payload=b'puts "Hello, world!"\r\ngets\r\n',
        ),
        ],
    from_values={'email': 'foo@example.com', 'name': '', 'full': 'foo@example.com'},
    to_values=({'email': 'blah@example.com', 'name': '', 'full': 'blah@example.com'},),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)