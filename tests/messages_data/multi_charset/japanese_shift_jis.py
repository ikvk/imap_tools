import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='test',
    from_='xxxxxxx@docomo.ne.jp',
    to=('unknown@example.com',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2014, 5, 28, 17, 18, 19, tzinfo=datetime.timezone(datetime.timedelta(seconds=32400))),
    date_str='Wed, 28 May 2014 17:18:19 +0900 (JST)',
    text='あいうえお\r\n\r\nこのメールはテスト用のメールです。\r\n\r\n今後ともよろしくお願い申し上げます！\r\n',
    html='',
    headers={'delivered-to': ('unknown@example.com',), 'date': ('Wed, 28 May 2014 17:18:19 +0900 (JST)',), 'from': ('xxxxxxx@docomo.ne.jp',), 'to': ('unknown@example.com',), 'subject': ('test',), 'message-id': ('<xxxxx@docomo.ne.jp>',), 'mime-version': ('1.0',), 'content-type': ('text/plain; charset="Shift_JIS"',), 'content-transfer-encoding': ('8bit',)},
    attachments=[],
    from_values=EmailAddress(name='', email='xxxxxxx@docomo.ne.jp'),
    to_values=(EmailAddress(name='', email='unknown@example.com'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)