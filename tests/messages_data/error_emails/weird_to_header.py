import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='',
    from_='anonymous@i.tp.host',
    to=('user-example@aol.com', 'e-s-a-s-2200@app.ar.com'),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2010, 10, 14, 23, 25, 6, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000))),
    date_str='14 Oct 2010 23:25:06 -0400',
    text='\r\nCONTACT:\r\n\r\n\r\n\r\n\r\nCOMMENT:\r\n\r\n\r\nPAGE THEY WERE ON:\r\n\r\n',
    html='',
    headers={'delivered-to': ('e-s-a-s-2200@app.ar.com',), 'received': ('by 10.103.1.1 with SMTP id w10cs50835muo;\r\n        Thu, 14 Oct 2010 20:25:16 -0700 (PDT)', 'by 10.150.205.4 with SMTP id c4mr736200ybg.26.1287113115711;\r\n        Thu, 14 Oct 2010 20:25:15 -0700 (PDT)', 'from i.tp.host ([172.1.1.1])\r\n        by mx.google.com with ESMTP id s21si2123456.90.2010.10.14.20.25.15;\r\n        Thu, 14 Oct 2010 20:25:15 -0700 (PDT)', '(qmail 28454 invoked by uid 48); 14 Oct 2010 23:25:06 -0400'), 'return-path': ('<anonymous@i.tp.host>',), 'received-spf': ('neutral (google.com: 172.1.1.1 is neither permitted nor denied by best guess record for domain of anonymous@i.tp.host) client-ip=172.1.1.1;',), 'authentication-results': ('mx.google.com; spf=neutral (google.com: 172.1.1.1 is neither permitted nor denied by best guess record for domain of anonymous@i.tp.host) smtp.mail=anonymous@i.tp.host',), 'date': ('14 Oct 2010 23:25:06 -0400',), 'message-id': ('<20101015032506.28448.qmail@i.tp.host>',), 'from': ('anonymous@i.tp.host',), 'to': (', user-example@aol.com, e-s-a-s-2200@app.ar.com',), 'subject': ('',)},
    attachments=[],
    from_values=EmailAddress(name='', email='anonymous@i.tp.host'),
    to_values=(EmailAddress(name='', email='user-example@aol.com'), EmailAddress(name='', email='e-s-a-s-2200@app.ar.com')),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)