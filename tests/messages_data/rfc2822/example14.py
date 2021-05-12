import datetime
    
DATA = dict(
    subject='Re: TESTテストテスト',
    from_='atsushi@example.com',
    to=('rudeboyjet@gmail.com',),
    cc=(),
    bcc=(),
    reply_to=('rudeboyjet@gmail.com',),
    date=datetime.datetime(2011, 8, 19, 10, 47, 17, tzinfo=datetime.timezone(datetime.timedelta(0, 32400))),
    date_str='Fri, 19 Aug 2011 10:47:17 +0900',
    text='Hello\r\n',
    html='',
    headers={'date': ('Fri, 19 Aug 2011 10:47:17 +0900',), 'from': ('Atsushi Yoshida <atsushi@example.com>',), 'reply-to': ('rudeboyjet@gmail.com',), 'subject': ('Re: TEST\r\n \r\n\t=?ISO-2022-JP?B?GyRCJUYlOSVIGyhC?=\r\n  =?ISO-2022-JP?B?GyRCJUYlOSVIGyhC?=',), 'to': ('rudeboyjet@gmail.com',), 'message-id': ('<0CC5E11ED2C1D@example.com>',), 'in-reply-to': ('<rid_5582199198@msgid.example.com>',), 'mime-version': ('1.0',), 'content-type': ('text/plain; charset=iso-2022-jp',), 'content-transfer-encoding': ('7bit',)},
    attachments=[],
    from_values={'email': 'atsushi@example.com', 'name': 'Atsushi Yoshida', 'full': 'Atsushi Yoshida <atsushi@example.com>'},
    to_values=({'email': 'rudeboyjet@gmail.com', 'name': '', 'full': 'rudeboyjet@gmail.com'},),
    cc_values=(),
    bcc_values=(),
    reply_to_values=({'email': 'rudeboyjet@gmail.com', 'name': '', 'full': 'rudeboyjet@gmail.com'},),
)