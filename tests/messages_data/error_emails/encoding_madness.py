import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='eBay Bid - 2008 Ford Super Duty F-350 DRW King Ranch Crew Cab 4x4 (156) - Stock# XXXX',
    from_='no-reply@crm.el-example.org',
    to=('e-f5f4@app.ar-example.com',),
    cc=(),
    bcc=(),
    reply_to=('',),
    date=datetime.datetime(2010, 9, 22, 2, 30, 53, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=68400))),
    date_str='Wed, 22 Sep 2010 02:30:53 -0500',
    text='Body Text',
    html='',
    headers={'delivered-to': ('e-f5f4@app.ar-example.com',), 'received': ('by 10.2.1.1 with SMTP id p21cs62610wem;\r\n        Wed, 22 Sep 2010 00:30:55 -0700 (PDT)', 'by 10.15.2.1 with SMTP id p24mr499372ybh.380.1285140655013;\r\n        Wed, 22 Sep 2010 00:30:55 -0700 (PDT)', 'from aquila.el-example.org ([174.1.8.2])\r\n        by mx.google.com with ESMTP id a6si11272839ybo.18.2010.09.22.00.30.54;\r\n        Wed, 22 Sep 2010 00:30:54 -0700 (PDT)', 'from aquila.el-example.org (localhost [127.0.0.1])\r\n\tby aquila.el-example.org (8.14.2/8.14.2) with ESMTP id o8M7UrfD018673\r\n\tfor <e-f5f4@app.ar-example.com>; Wed, 22 Sep 2010 02:30:54 -0500 (CDT)\r\n\t(envelope-from production@aquila.el-example.org)', '(from production@localhost)\r\n\tby aquila.el-example.org (8.14.2/8.14.2/Submit) id o8M7Urh3018672;\r\n\tWed, 22 Sep 2010 02:30:53 -0500 (CDT)\r\n\t(envelope-from production)'), 'return-path': ('<production@aquila.el-example.org>',), 'received-spf': ('neutral (google.com: 174.1.8.2 is neither permitted nor denied by best guess record for domain of production@aquila.el-example.org) client-ip=174.1.8.2;',), 'authentication-results': ('mx.google.com; spf=neutral (google.com: 174.1.8.2 is neither permitted nor denied by best guess record for domain of production@aquila.el-example.org) smtp.mail=production@aquila.el-example.org',), 'message-id': ('<201009220730.o8M7Urh3018672@aquila.el-example.org>',), 'mime-version': ('1.0',), 'content-disposition': ('inline',), 'content-transfer-encoding': ('quoted-printable',), 'content-type': ('text/plain',), 'x-mailer': ('MIME::Lite 3.027 (F2.74; T1.28; A2.04; B3.07; Q3.07)',), 'date': ('Wed, 22 Sep 2010 02:30:53 -0500',), 'from': ('no-reply@crm.el-example.org',), 'to': ('e-f5f4@app.ar-example.com',), 'reply-to': ('"KLAUS- H\udcc3\udc84NSCHEL" <>',), 'subject': ('eBay Bid - 2008 Ford Super Duty F-350 DRW King Ranch Crew Cab 4x4 (156) - Stock# XXXX',)},
    attachments=[],
    from_values=EmailAddress(name='', email='no-reply@crm.el-example.org'),
    to_values=(EmailAddress(name='', email='e-f5f4@app.ar-example.com'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(EmailAddress(name='KLAUS- HÄNSCHEL', email=''),),
)