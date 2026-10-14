import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='Test HTML Parsing',
    from_='alice@example.com',
    to=('bob@example.com',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(1900, 1, 1, 0, 0),
    date_str='',
    text='',
    html='<html>\n<head>\n  <style>\n    .header { opacity: 0.8; }\n  </style>\n  <script>\n    var specificCity = "HiddenCity";\n  </script>\n</head>\n<body>\n  <p>I am traveling to M&uuml;nster for work.</p>\n  <p>I need to call AT&amp;T because my phone is broken. A &lt; B.</p>\n  <p>The weather is beauti&shy;ful, and I am meeting my co&zwnj;worker.</p>\n  <p>Don\'t miss the Sale&nbsp;Today!</p>\n</body>\n</html>\n',
    headers={'from': ('Alice <alice@example.com>',), 'to': ('Bob <bob@example.com>',), 'subject': ('Test HTML Parsing',), 'content-type': ('text/html; charset=UTF-8',), 'content-transfer-encoding': ('7bit',)},
    attachments=[],
    from_values=EmailAddress(name='Alice', email='alice@example.com'),
    to_values=(EmailAddress(name='Bob', email='bob@example.com'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)