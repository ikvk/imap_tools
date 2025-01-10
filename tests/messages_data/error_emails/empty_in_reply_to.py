import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='illegal copy of our patient education software ',
    from_='ak@g.com',
    to=('abuser@r.ru',),
    cc=(),
    bcc=(),
    reply_to=('ak@g.com',),
    date=datetime.datetime(2009, 9, 19, 19, 49, 36, tzinfo=datetime.timezone(datetime.timedelta(seconds=14400))),
    date_str='Sat, 19 Sep 2009 19:49:36 +0400',
    text='',
    html='',
    headers={'return-path': ('<ak@g.com>', '<ak@g.com>'), 'envelope-to': ('abuser@r.ru',), 'delivery-date': ('Sat, 19 Sep 2009 21:41:40 +0400',), 'received': ('from mail-fx0-f215.google.com ([209.85.220.215]:39047)\r\n\tby mail.rg.com with esmtp \r\n\tid 1Mp3wA-0007kA-Ic\r\n\tfor <abuser@r.ru>; Sat, 19 Sep 2009 21:41:30 +0400', 'by fxm11 with SMTP id 11so1412272fxm.15\r\n        for <abuser@r.ru>; Sat, 19 Sep 2009 10:40:39 -0700 (PDT)', 'by 10.86.240.9 with SMTP id n9mr2799028fgh.70.1253375382709;\r\n        Sat, 19 Sep 2009 08:49:42 -0700 (PDT)', 'from articondell (ppp85-140-104-88.pppoe.mtu-net.ru [85.140.104.88])\r\n        by mx.google.com with ESMTPS id e11sm2485072fga.21.2009.09.19.08.49.39\r\n        (version=SSLv3 cipher=RC4-MD5);\r\n        Sat, 19 Sep 2009 08:49:40 -0700 (PDT)'), 'dkim-signature': ('v=1; a=rsa-sha256; c=relaxed/relaxed;\r\n        d=gmail.com; s=gamma;\r\n        h=domainkey-signature:received:received:from:to:subject:date\r\n         :message-id:mime-version:content-type:x-priority:x-msmail-priority\r\n         :x-mailer:importance:x-mimeole:in-reply-to;\r\n        bh=U4LmZ2XrYxpE2gzziKYLSJXvmTsl0JSdrp4OYcIw2xw=;\r\n        b=N4ZFNsnhqgG0qILwgjv0Sh0qKgSR+A5hMn60yxtSlACUDq/xQ/52pJkCuMChX0Pzxo\r\n         HaRYdiAsxyzlzmSStwtM/fAHZSNrXD0pLpeQOCi1r8ZSyQ6mKb4WgO56FFNOjCA0rLl8\r\n         NOelymNmCIYTwuYz5Dd0PthnWL0YZPU+YUEHU=',), 'domainkey-signature': ('a=rsa-sha1; c=nofws;\r\n        d=gmail.com; s=gamma;\r\n        h=from:to:subject:date:message-id:mime-version:content-type\r\n         :x-priority:x-msmail-priority:x-mailer:importance:x-mimeole\r\n         :in-reply-to;\r\n        b=ZTs05s6OpCmZp0GWYqGIv8xGM+AmM7+QL6SdaR45KgwCcN8sJH0SB4PI4QMFSW3+ZX\r\n         IdYVUGjqer/bEz7POPS8FOTCZW1QTkRcTHqVEFezAmotlc0VfLVSnnW9oRpzJ/UFQUWM\r\n         +Wn0vcObiGmrUPUJWWiNgBvuRnrJHk+nICCQI=',), 'from': ('"Andrey Kuznetsov" <ak@g.com>',), 'to': ('<abuser@r.ru>',), 'subject': ('illegal copy of our patient education software ',), 'date': ('Sat, 19 Sep 2009 19:49:36 +0400',), 'message-id': ('<F194F88AF3E341A6B2B135CC17912811@articondell>',), 'mime-version': ('1.0',), 'content-type': ('multipart/related;\r\n\tboundary="----=_NextPart_000_000A_01CA3962.51E52370"',), 'x-priority': ('3 (Normal)',), 'x-msmail-priority': ('Normal',), 'x-mailer': ('Microsoft Outlook, Build 10.0.4024',), 'importance': ('Normal',), 'x-mimeole': ('Produced By Microsoft MimeOLE V6.00.2900.5579',), 'in-reply-to': ('',), 'recivied-spf': ('(invalid) ',), 'rspam-score': ('40',), 'list-id': ('abuser@rg.com Mailing List',), 'reply-to': ('ak@g.com',)},
    attachments=[],
    from_values=EmailAddress(name='Andrey Kuznetsov', email='ak@g.com'),
    to_values=(EmailAddress(name='', email='abuser@r.ru'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(EmailAddress(name='', email='ak@g.com'),),
)