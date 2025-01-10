import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='Re: Test reply email',
    from_='xxxxxxxx@xxx.org',
    to=('mikel@xxxx.net',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2007, 11, 18, 19, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(seconds=39600))),
    date_str='Sun, 18 Nov 2007 19:56:07 +1100',
    text='Message body\r\n',
    html='',
    headers={'return-path': ('<xxxxxxxx@xxx.org>',), 'received': ('from me ([unix socket])\r\n\t by xxxxx1.xxxx.net (Cyrus v2.2.12) with LMTPA;\r\n\t Sun, 18 Nov 2007 00:56:33 -0800', 'from smtp.xxxx.org (unknown [127.0.0.1])\r\n\tby xxxxx1.xxxx.net (Postfix) with ESMTP id F128477EB5;\r\n\tSun, 18 Nov 2007 00:56:32 -0800 (PST)', 'from omta02sl.mx.bigpond.com (omta02sl.mx.bigpond.com [144.140.93.154])\r\n\tby smtp.xxxx.org (Postfix) with ESMTP id 2D567ACC08;\r\n\tSun, 18 Nov 2007 00:56:28 -0800 (PST)', 'from oaamta05sl.mx.bigpond.com ([124.183.219.10])\r\n          by omta02sl.mx.bigpond.com with ESMTP\r\n          id <20071118085627.YVPI22254.omta02sl.mx.bigpond.com@oaamta05sl.mx.bigpond.com>;\r\n          Sun, 18 Nov 2007 08:56:27 +0000', 'from [10.0.0.1] (really [124.183.219.10])\r\n          by oaamta05sl.mx.bigpond.com with ESMTP\r\n          id <20071118085627.TQWF6995.oaamta05sl.mx.bigpond.com@[10.0.0.1]>;\r\n          Sun, 18 Nov 2007 08:56:27 +0000'), 'message-id': ('<473FFE27.20003@xxx.org>',), 'date': ('Sun, 18 Nov 2007 19:56:07 +1100',), 'from': ('Testing <xxxxxxxx@xxx.org>',), 'user-agent': ('Mozilla Thunderbird 1.0.6 (Windows/20050716)',), 'x-accept-language': ('en-us, en',), 'mime-version': ('1.0',), 'to': ('Mikel Lindsaar <mikel@xxxx.net>',), 'subject': ('Re: Test reply email',), 'references': ('<473FF3B8.9020707@xxx.org> <348F04F142D69C21-291E56D292BC@xxxx.net>',), 'in-reply-to': ('<348F04F142D69C21-291E56D292BC@xxxx.net>',), 'content-type': ('text/plain; charset=US-ASCII; format=flowed',), 'content-transfer-encoding': ('7bit',)},
    attachments=[],
    from_values=EmailAddress(name='Testing', email='xxxxxxxx@xxx.org'),
    to_values=(EmailAddress(name='Mikel Lindsaar', email='mikel@xxxx.net'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)