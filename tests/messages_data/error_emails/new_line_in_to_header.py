import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='[Online Lead] Online Lead #1111111',
    from_='l@gcn-example.com',
    to=('leads@sg.dc.com', 'sag@leads.gs.ry.com', 'sn@example-hotmail.com', 'e-s-a-g-8718@app.ar.com', 'jp@t-exmaple.com', 'cc@c-l-example.com'),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2010, 10, 13, 7, 53, 4, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=61200))),
    date_str='Wed, 13 Oct 2010 07:53:04 -0700',
    text='<?xml version="1.0" encoding="UTF-8"?>\r\n<?ADF version="1.0"?><adf>\r\n  <prospect>\r\n    <requestdate>2010-10-13T07:53:04-09:00</requestdate>\r\n    ... (not important) ...',
    html='',
    headers={'delivered-to': ('e-s-a-g-8718@app.ar.com',), 'received': ('by 10.2.1.1 with SMTP id c60cs12954wel;\r\n        Wed, 13 Oct 2010 07:44:39 -0700 (PDT)', 'by 10.15.1.1 with SMTP id f12mr1139775ybe.360.1286981078364;\r\n        Wed, 13 Oct 2010 07:44:38 -0700 (PDT)', 'from services.travidiabamboo.com (services.travidiabamboo.com [72.21.1.1])\r\n        by mx.google.com with ESMTP id v33si16714378yba.88.2010.10.13.07.44.37;\r\n        Wed, 13 Oct 2010 07:44:38 -0700 (PDT)', 'from travidiabamboo.com (services [10.0.0.2])\r\n\tby services.travidiabamboo.com (Postfix) with ESMTP id A532170702;\r\n\tWed, 13 Oct 2010 07:53:04 -0700 (PDT)'), 'return-path': ('<l@gcn-example.com>',), 'received-spf': ('pass (google.com: domain of l@gcn-example.com designates 72.21.1.1 as permitted sender) client-ip=72.21.1.1;',), 'authentication-results': ('mx.google.com; spf=pass (google.com: domain of l@gcn-example.com designates 72.21.1.1 as permitted sender) smtp.mail=l@gcn-example.com',), 'date': ('Wed, 13 Oct 2010 07:53:04 -0700',), 'from': ('l@gcn-example.com',), 'to': ('leads@sg.dc.com,\r\n\t sag@leads.gs.ry.com,\r\n\t sn@example-hotmail.com,\r\n\t e-s-a-g-8718@app.ar.com,\r\n\t jp@t-exmaple.com,\r\n\t\r\n\tcc@c-l-example.com',), 'message-id': ('<4cb5c7d0a3cce_120e..fdbed2b861958562@s.t-example.com.tmail>',), 'subject': ('[Online Lead] Online Lead #1111111',), 'mime-version': ('1.0',), 'content-type': ('text/plain; charset=utf-8',)},
    attachments=[],
    from_values=EmailAddress(name='', email='l@gcn-example.com'),
    to_values=(EmailAddress(name='', email='leads@sg.dc.com'), EmailAddress(name='', email='sag@leads.gs.ry.com'), EmailAddress(name='', email='sn@example-hotmail.com'), EmailAddress(name='', email='e-s-a-g-8718@app.ar.com'), EmailAddress(name='', email='jp@t-exmaple.com'), EmailAddress(name='', email='cc@c-l-example.com')),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)