import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='まみむめもまみむめもまみむめもまみむめもまみむめもまみむめもまみむめもまみむめもまみむめもまみむめも',
    from_='mikel@test.lindsaar.net',
    to=('raasdnil@gmail.com',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2009, 10, 30, 19, 11, 2, tzinfo=datetime.timezone(datetime.timedelta(seconds=39600))),
    date_str='Fri, 30 Oct 2009 19:11:02 +1100',
    text='',
    html='',
    headers={'delivered-to': ('raasdnil@gmail.com',), 'received': ('by 10.231.12.67 with SMTP id w3cs164325ibw;\r\n        Fri, 30 Oct 2009 01:11:12 -0700 (PDT)', 'by 10.150.44.2 with SMTP id r2mr2367210ybr.77.1256890271939;\r\n        Fri, 30 Oct 2009 01:11:11 -0700 (PDT)', 'from mx1.test.lindsaar.net.au (mx1.test.lindsaar.net.au [210.14.110.240])\r\n        by mx.google.com with ESMTP id 25si7923673gxk.34.2009.10.30.01.11.11;\r\n        Fri, 30 Oct 2009 01:11:11 -0700 (PDT)', 'from [192.168.4.253] (60-241-138-146.static.tpgi.com.au [60.241.138.146])\r\n\t(using TLSv1 with cipher AES128-SHA (128/128 bits))\r\n\t(No client certificate requested)\r\n\t(Authenticated sender: mikel)\r\n\tby mx1.test.lindsaar.net.au (Postfix) with ESMTPSA id 5C0186DD4CD\r\n\tfor <raasdnil@gmail.com>; Fri, 30 Oct 2009 19:11:08 +1100 (EST)'), 'return-path': ('<mikel@test.lindsaar.net>',), 'received-spf': ('neutral (google.com: 210.14.110.240 is neither permitted nor denied by domain of mikel@test.lindsaar.net) client-ip=210.14.110.240;',), 'authentication-results': ('mx.google.com; spf=neutral (google.com: 210.14.110.240 is neither permitted nor denied by domain of mikel@test.lindsaar.net) smtp.mail=mikel@test.lindsaar.net',), 'subject': ('=?utf-8?B?44G+44G/44KA44KB44KC44G+44G/44KA44KB44KC44G+44G/44KA?=\r\n =?utf-8?B?44KB44KC44G+44G/44KA44KB44KC44G+44G/44KA44KB44KC44G+?=\r\n =?utf-8?B?44G/44KA44KB44KC44G+44G/44KA44KB44KC44G+44G/44KA44KB?=\r\n =?utf-8?B?44KC44G+44G/44KA44KB44KC44G+44G/44KA44KB44KC?=',), 'from': ('Mikel Lindsaar <mikel@test.lindsaar.net>',), 'content-type': ('multipart/mixed; boundary=Apple-Mail-6--589811753',), 'message-id': ('<60A112A8-F26C-4E23-95B8-4EB9F139D6A0@test.lindsaar.net>',), 'date': ('Fri, 30 Oct 2009 19:11:02 +1100',), 'to': ('Mikel Lindsaar <raasdnil@gmail.com>',), 'mime-version': ('1.0 (Apple Message framework v1076)',), 'x-mailer': ('Apple Mail (2.1076)',)},
    attachments=[
        dict(
            filename='かきくけこかきくけこかきくけこかきくけこかきくけこ.txt',
            content_id='',
            content_disposition='attachment',
            content_type='text/plain',
            payload=b'this is the data\r\n',
        ),
        ],
    from_values=EmailAddress(name='Mikel Lindsaar', email='mikel@test.lindsaar.net'),
    to_values=(EmailAddress(name='Mikel Lindsaar', email='raasdnil@gmail.com'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)