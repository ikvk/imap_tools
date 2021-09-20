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
    from_values=EmailAddress('Каукин Владимир', 'kaukinvk@yandex.ru', 'Каукин Владимир <kaukinvk@yandex.ru>'),
    to_values=(EmailAddress('', 'aa@aa.ru', 'aa@aa.ru'), EmailAddress('', 'bb@aa.ru', 'bb@aa.ru')),
    cc_values=(EmailAddress('', 'cc@aa.ru', 'cc@aa.ru'), EmailAddress('', 'dd@aa.ru', 'dd@aa.ru')),
    bcc_values=(EmailAddress('', 'zz1@aa.ru', 'zz1@aa.ru'), EmailAddress('', 'zz2@aa.ru', 'zz2@aa.ru')),
    reply_to_values=(EmailAddress('привет', 'foma1@company.ru', 'привет <foma1@company.ru>'), EmailAddress('пока', 'petr1@company.ru', 'пока <petr1@company.ru>'), EmailAddress('привет', 'foma2@company.ru', 'привет <foma2@company.ru>'), EmailAddress('пока', 'petr2@company.ru', 'пока <petr2@company.ru>')),
)