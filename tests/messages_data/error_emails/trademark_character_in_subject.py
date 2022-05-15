import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='GA.comô has a lead for you',
    from_='j@yahoo-example.com',
    to=('c@ra-example.com', 'e-r-w-a-4462@app.ar.com', 'leads@ga-example.com'),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2010, 10, 12, 16, 21, 5),
    date_str='Tue, 12 Oct 2010 16:21:05 H0500',
    text='Body Text - not important',
    html='',
    headers={'delivered-to': ('e-r-w-a-4462@app.ar.com',), 'received': ('by 10.1.1.1 with SMTP id w10cs10896muo;\r\n        Tue, 12 Oct 2010 13:20:24 -0700 (PDT)', 'by 10.2.1.5 with SMTP id bk15mr6105827qab.89.1286914824124;\r\n        Tue, 12 Oct 2010 13:20:24 -0700 (PDT)', 'from mail.ga-example.com (mail.ga-example.com [64.1.2.3])\r\n        by mx.google.com with ESMTP id 13si112341247qcd.23.2010.10.12.13.20.23;\r\n        Tue, 12 Oct 2010 13:20:24 -0700 (PDT)', 'from GAWWW03 by ga-example.com (MDaemon PRO v11.0.3)\r\n\twith ESMTP id md50004804310.msg\r\n\tfor <e-r-w-a-4462@app.ar.com>; Tue, 12 Oct 2010 16:21:05 -0400'), 'return-path': ('<j@yahoo-example.com>',), 'received-spf': ('neutral (google.com: 64.1.2.3 is neither permitted nor denied by best guess record for domain of j@yahoo-example.com) client-ip=64.1.2.3;',), 'authentication-results': ('mx.google.com; spf=neutral (google.com: 64.1.2.3 is neither permitted nor denied by best guess record for domain of j@yahoo-example.com) smtp.mail=j@yahoo-example.com',), 'x-mdav-processed': ('mail.ga-example.com, Tue, 12 Oct 2010 16:21:07 -0400',), 'x-spam-processed': ('mail.ga-example.com, Tue, 12 Oct 2010 16:21:06 -0400',), 'x-spam-checker-version': ('SpamAssassin 3.2.5 (2008-06-10) on\r\n\tMAIL02.VD-example.com',), 'x-spam-level': ('',), 'x-spam-status': ('No, score=-1.1 required=5.0 tests=BAYES_00,DATE_IN_PAST_03_06,\r\n\tFORGED_YAHOO_RCVD,INVALID_DATE,NO_RELAYS,SUBJECT_NEEDS_ENCODING\r\n\tshortcircuit=no autolearn=no version=3.2.5',), 'x-mdremoteip': ('192.168.254.73',), 'x-return-path': ('j@yahoo-example.com',), 'x-envelope-from': ('j@yahoo-example.com',), 'x-mdaemon-deliver-to': ('e-r-w-a-4462@app.ar.com',), 'date': ('Tue, 12 Oct 2010 16:21:05 H0500',), 'subject': ('GA.com\udcc3\udcb4 has a lead for you',), 'to': ('c@ra-example.com,e-r-w-a-4462@app.ar.com,leads@ga-example.com',), 'mime-version': ('1.0',), 'content-type': ('text/plain; charset=iso-8859-1',), 'from': ('j@yahoo-example.com',), 'message-id': ('<MDAEMON-F201010121621.AA2105420md50000198258@ga-example.com>',)},
    attachments=[],
    from_values=EmailAddress(name='', email='j@yahoo-example.com'),
    to_values=(EmailAddress(name='', email='c@ra-example.com'), EmailAddress(name='', email='e-r-w-a-4462@app.ar.com'), EmailAddress(name='', email='leads@ga-example.com')),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)