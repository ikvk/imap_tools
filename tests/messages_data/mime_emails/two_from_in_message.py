import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='Sending messages include last little bit',
    from_='tester1@test.com',
    to=('tester2@test.com',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2009, 12, 2, 22, 39, 33, tzinfo=datetime.timezone(datetime.timedelta(seconds=46800))),
    date_str='Wed, 2 Dec 2009 22:39:33 +1300',
    text="When sending email:\r\n* From Hotmail you get the ads as well.\r\n* From GMail you also get the person's signature.\r\n\r\nI'm curious, and I might do some digging tomorrow as well, to see if its\r\npossible to strip the last little bit (signature/ads) from email messages.\r\n",
    html='<div class="gmail_quote"><div class="gmail_quote"><div>When sending email:</div>* From Hotmail you get the ads as well.<div>* From GMail you also get the person&#39;s signature.</div><div><br></div><div>I\'m curious, and I might do some digging tomorrow as well, to see if its possible to strip the last little bit (signature/ads) from email messages.<br>\r\n\r\n</div></div></div>\r\n',
    headers={'return-path': ('<test@test.com>',), 'received': ('from mail-xxx.google.com (mail-xxx.google.com [0.0.0.0])\r\n\tby smtp.test.com (Postfix) with ESMTP id xxxx\r\n\tfor <tester@test.com>; Wed,  2 Dec 2009 09:39:57 +0000 (UTC)', 'by qyk6 with SMTP id 6so3112qyk.3\r\n        for <tester@test.com>; Wed, 02 Dec 2009 01:39:53 -0800 (PST)', 'by 0.0.0.0 with SMTP id xxx.000.0000000000000; Wed, \r\n\t02 Dec 2009 01:39:53 -0800 (PST)'), 'mime-version': ('1.0',), 'in-reply-to': ('<8fc5086d0912020131y377ba0ccpf8f14783cfc3014a@test.com>',), 'references': ('<8fc5086d0912020131y377ba0ccpf8f14783cfc3014a@test.com>',), 'from': ('Tester 1 <tester1@test.com>',), 'date': ('Wed, 2 Dec 2009 22:39:33 +1300',), 'message-id': ('<8fc5086d0912020139y1564ad32jb4f4209fa464f4a6@test.com>',), 'subject': ('Sending messages include last little bit',), 'to': ('tester2@test.com',), 'content-type': ('multipart/alternative; boundary=00c09fa216eb1bfc0a0479bba823',)},
    attachments=[],
    from_values=EmailAddress(name='Tester 1', email='tester1@test.com'),
    to_values=(EmailAddress(name='', email='tester2@test.com'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)