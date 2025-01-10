import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='Testing 123',
    from_='test@lindsaar.net',
    to=('smith@gmail.com', 'Mikel@Lindsaar', 'raasdnil@gmail.com', 'tom@gmail.com'),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2008, 11, 22, 15, 4, 59, tzinfo=datetime.timezone(datetime.timedelta(seconds=39600))),
    date_str='Sat, 22 Nov 2008 15:04:59 +1100',
    text='Plain email.\r\n\r\nHope it works well!\r\n\r\nMikel\r\n',
    html='',
    headers={'delivered-to': ('raasdnil@gmail.com',), 'received': ('by 10.140.178.13 with SMTP id a13cs354079rvf;\r\n        Fri, 21 Nov 2008 20:05:05 -0800 (PST)', 'by 10.151.44.15 with SMTP id w15mr2254748ybj.98.1227326704711;\r\n        Fri, 21 Nov 2008 20:05:04 -0800 (PST)', 'from mail11.tpgi.com.au (mail11.tpgi.com.au [203.12.160.161])\r\n        by mx.google.com with ESMTP id 10si5117885gxk.81.2008.11.21.20.05.03;\r\n        Fri, 21 Nov 2008 20:05:04 -0800 (PST)', 'from [192.0.0.253] (60-241-138-146.static.tpgi.com.au [60.0.0.146])\r\n\tby mail11.tpgi.com.au (envelope-from test@lindsaar.net) (8.14.3/8.14.3) with ESMTP id mAM44xew022221\r\n\tfor <raasdnil@gmail.com>; Sat, 22 Nov 2008 15:05:01 +1100'), 'return-path': ('<test@lindsaar.net>',), 'received-spf': ('neutral (google.com: 203.12.160.161 is neither permitted nor denied by domain of test@lindsaar.net) client-ip=203.12.160.161;',), 'authentication-results': ('mx.google.com; spf=neutral (google.com: 203.12.160.161 is neither permitted nor denied by domain of test@lindsaar.net) smtp.mail=test@lindsaar.net',), 'x-tpg-junk-status': ('Message not scanned',), 'x-tpg-antivirus': ('Passed',), 'message-id': ('<6B7EC235-5B17-4CA8-B2B8-39290DEB43A3@test.lindsaar.net>',), 'from': ('Mikel Lindsaar <test@lindsaar.net>, jack@lindsar.com',), 'to': ('smith@gmail.com, Mikel@Lindsaar <raasdnil@gmail.com>, tom@gmail.com',), 'content-type': ('text/plain; charset=US-ASCII; format=flowed',), 'content-transfer-encoding': ('7bit',), 'mime-version': ('1.0 (Apple Message framework v929.2)',), 'subject': ('Testing 123',), 'date': ('Sat, 22 Nov 2008 15:04:59 +1100',), 'x-mailer': ('Apple Mail (2.929.2)',)},
    attachments=[],
    from_values=EmailAddress(name='Mikel Lindsaar', email='test@lindsaar.net'),
    to_values=(EmailAddress(name='', email='smith@gmail.com'), EmailAddress(name='', email='Mikel@Lindsaar'), EmailAddress(name='', email='raasdnil@gmail.com'), EmailAddress(name='', email='tom@gmail.com')),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)