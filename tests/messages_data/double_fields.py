import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='double_fields',
    from_='kaukinvk@yandex.ru',
    to=('aa@aa.ru', 'bb@aa.ru'),
    cc=('cc@aa.ru', 'dd@aa.ru'),
    bcc=('zz1@aa.ru', 'zz2@aa.ru'),
    reply_to=('foma1@company.ru', 'petr1@company.ru', 'foma2@company.ru', 'petr2@company.ru'),
    date=datetime.datetime(2019, 5, 1, 12, 20),
    date_str='Wed, 01 May 2019 12:20',
    text='',
    html='<div>double_fields</div>',
    headers={'to': ('aa@aa.ru', 'bb@aa.ru', ''), 'cc': ('cc@aa.ru', 'dd@aa.ru'), 'bcc': ('zz1@aa.ru', 'zz2@aa.ru'), 'reply-to': ('=?UTF-8?B?0L/RgNC40LLQtdGC?= <foma1@company.ru>,\r\n =?UTF-8?B?0L/QvtC60LA=?= <petr1@company.ru>', '=?UTF-8?B?0L/RgNC40LLQtdGC?= <foma2@company.ru>,\r\n =?UTF-8?B?0L/QvtC60LA=?= <petr2@company.ru>'), 'from': ('=?utf-8?B?0JrQsNGD0LrQuNC9INCS0LvQsNC00LjQvNC40YA=?= <kaukinvk@yandex.ru>',), 'envelope-from': ('kaukinvk@yandex.ru',), 'subject': ('double_fields',), 'mime-version': ('1.0',), 'date': ('Wed, 01 May 2019 12:20',), 'message-id': ('<8872861556695229@myt5-262fb1897c00.qloud-c.yandex.net>',), 'content-type': ('multipart/mixed;\r\n\tboundary="----==--bound.887287.myt5-262fb1897c00.qloud-c.yandex.net"',), 'return-path': ('kaukinvk@yandex.ru',)},
    attachments=[],
    from_values=EmailAddress(name='Каукин Владимир', email='kaukinvk@yandex.ru'),
    to_values=(EmailAddress(name='', email='aa@aa.ru'), EmailAddress(name='', email='bb@aa.ru')),
    cc_values=(EmailAddress(name='', email='cc@aa.ru'), EmailAddress(name='', email='dd@aa.ru')),
    bcc_values=(EmailAddress(name='', email='zz1@aa.ru'), EmailAddress(name='', email='zz2@aa.ru')),
    reply_to_values=(EmailAddress(name='привет', email='foma1@company.ru'), EmailAddress(name='пока', email='petr1@company.ru'), EmailAddress(name='привет', email='foma2@company.ru'), EmailAddress(name='пока', email='petr2@company.ru')),
)