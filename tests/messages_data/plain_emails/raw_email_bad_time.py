import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='[0]: XXXXXXX XXXXX XXXXX !',
    from_='yusuf75thu@auracom.net',
    to=('abcdefg@AAAAAAAAA.net',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(3609, 6, 30, 15, 33, 50, tzinfo=datetime.timezone(datetime.timedelta(seconds=21600))),
    date_str='Mon, 30 Jun 3609 15:33:50 +0600',
    text='\r\nFilter2: This message has been scanned for viruses and\r\ndangerous content by MailScanner, and is\r\nbelieved to be clean.\r\n\r\n',
    html='<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">\r\n<HTML><HEAD>\r\n<META http-equiv=Content-Type content="text/html; charset=utf-8">\r\n<META content="MSHTML 6.00.2900.2180" name=GENERATOR>\r\n<STYLE></STYLE>\r\n</HEAD>\r\n<BODY bgColor=#ffffff>\r\n<br />This message has been scanned for viruses and\r\n<br />dangerous content by\r\n<a href="http://www.mailscanner.info/"><b>MailScanner</b></a>, and is\r\n<br />believed to be clean.\r\n</HTML>\r\n',
    headers={'return-path': ('<yusuf75thu@auracom.net>',), 'received': ('from murder ([unix socket])\r\n         by imap1.AAAAAAAAA.net (Cyrus v2.2.12-Invoca-RPM-2.2.12-6.fc4) with LMTPA;\r\n         Mon, 30 Jun 2008 02:34:00 -0700', 'from smtp2.BBBBBBBBBBB.org (unknown [10.254.15.30])\r\n        by imap1.AAAAAAAAA.net (Postfix) with ESMTP id 9444077D75\r\n        for <abcdefg@AAAAAAAAA.net>; Mon, 30 Jun 2008 02:34:00 -0700 (PDT)', 'from localhost (unknown [92.47.238.91])\r\n        by smtp2.BBBBBBBBBBB.org (Postfix) with ESMTP id 44D0110011\r\n        for <abcdefg@AAAAAAAAA.net>; Mon,  9 Jun 2008 12:24:02 -0700 (PDT)'), 'x-sieve': ('CMU Sieve 2.2',), 'message-id': ('<86a2019dbec6$caa86cc0$390b0485@auracom.net>',), 'from': ('"=?windows-1251?B?wPLo6u7iYQ==?=" <yusuf75thu@auracom.net>',), 'to': ('<abcdefg@AAAAAAAAA.net>',), 'subject': ('[0]: XXXXXXX XXXXX XXXXX !',), 'date': ('Mon, 30 Jun 3609 15:33:50 +0600',), 'mime-version': ('1.0',), 'content-type': ('multipart/alternative;\r\n                boundary=----=_NextPart_000_0023_08_E8CD50F3.4EF2F754',), 'x-priority': ('3',), 'x-msmail-priority': ('Normal',), 'x-mailer': ('Microsoft Outlook Express 6.00.2900.2180',), 'x-mimeole': ('Produced By Microsoft MimeOLE V6.00.2900.2180',), 'x-csi-mailscanner-information': ('Please contact the ISP for more information',), 'x-csi-mailscanner': ('Found to be clean',), 'x-csi-mailscanner-spamcheck': ('spam, ORDB-RBL',), 'x-csi-mailscanner-from': ('yusuf75thu@auracom.net',), 'x-spam-status': ('Yes',)},
    attachments=[],
    from_values=EmailAddress(name='Атиковa', email='yusuf75thu@auracom.net'),
    to_values=(EmailAddress(name='', email='abcdefg@AAAAAAAAA.net'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)