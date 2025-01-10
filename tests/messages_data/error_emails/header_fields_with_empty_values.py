import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='Testmail',
    from_='jorn@prikkprikkprikk.no',
    to=('aftest@adfontesmedier.no',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2009, 10, 30, 20, 7, 42, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))),
    date_str='Fri, 30 Oct 2009 20:07:42 +0100',
    text='\r\n\r\n--\r\nJørn Støylen -- http://www.prikkprikkprikk.no\r\n924 38 051 -- jorn@prikkprikkprikk.no\r\n\r\n',
    html='',
    headers={'received': ('from mx01.medieveven.no (192.168.42.42) by epost.vartland.no\r\n (192.168.73.7) with Microsoft SMTP Server id 8.1.393.1; Fri, 30 Oct 2009\r\n 20:08:07 +0100', 'from woodward.joyent.us ([8.12.42.230])  by mx01.medieveven.no with\r\n ESMTP; 30 Oct 2009 20:11:23 +0100', 'from [10.0.0.5] (ti0083a340-0282.bb.online.no [88.89.59.28])\tby\r\n woodward.joyent.us (Postfix) with ESMTPSA id EC35240C85\tfor\r\n <aftest@adfontesmedier.no>; Fri, 30 Oct 2009 19:07:44 +0000 (GMT)'), 'from': ('=?iso-8859-1?Q?J=F8rn_St=F8ylen?= <jorn@prikkprikkprikk.no>',), 'to': ('AF Test <aftest@adfontesmedier.no>',), 'date': ('Fri, 30 Oct 2009 20:07:42 +0100',), 'subject': ('Testmail',), 'thread-topic': ('Testmail',), 'thread-index': ('AcpZlFLF/Y9EfcC0QZKKEuUFm2Snqw==',), 'message-id': ('<4FDC124A-1FC4-4B29-8502-E459BD9AB397@prikkprikkprikk.no>',), 'accept-language': ('nb-NO',), 'x-ms-exchange-organization-authas': ('Anonymous',), 'x-ms-exchange-organization-authsource': ('epost.vartland.no',), 'x-ms-has-attach': ('',), 'x-ms-tnef-correlator': ('',), 'x-ironport-anti-spam-filtered': ('true',), 'x-ironport-av': ('E=Sophos;i="4.44,655,1249250400";    d="scan\'208";a="2439461"',), 'x-ironport-anti-spam-result': ('AvMBAPfV6koIDCrmhWdsb2JhbACbVgEBAQoLChoDxH2EPQQ',), 'content-type': ('text/plain; charset="iso-8859-1"',), 'content-transfer-encoding': ('quoted-printable',), 'mime-version': ('1.0',)},
    attachments=[],
    from_values=EmailAddress(name='Jørn Støylen', email='jorn@prikkprikkprikk.no'),
    to_values=(EmailAddress(name='AF Test', email='aftest@adfontesmedier.no'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)