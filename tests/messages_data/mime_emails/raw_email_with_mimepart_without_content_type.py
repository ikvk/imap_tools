import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='Warning: could not send message for past 1 day',
    from_='MAILER-DAEMON@antivirus.uqam.ca',
    to=('roor32@gmail.com',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2006, 10, 20, 4, 28, 33, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000))),
    date_str='Fri, 20 Oct 2006 04:28:33 -0400 (EDT)',
    text="    **********************************************\r\n    **      THIS IS A WARNING MESSAGE ONLY      **\r\n    **  YOU DO NOT NEED TO RESEND YOUR MESSAGE  **\r\n    **********************************************\r\n\r\nThe original message was received at Thu, 19 Oct 2006 01:23:47 -0400 (EDT)\r\nfrom py-out-1112.google.com [64.233.166.178]\r\n\r\n   ----- Transcript of session follows -----\r\n<larose.julie@courrier.uqam.ca>... Deferred\r\nWarning: message still undelivered after 1 day\r\nWill keep trying until message is 5 days old\r\nSalut,\r\nje ne suis pas sur de m'adresser a la bonne personne.\r\nMais si jamais tu me reconnais :p, peux-tu repondre a ce mail ?\r\nMerci.\r\nRoger\r\n",
    html='',
    headers={'x-gmail-received': ('b2c98353cc39d93e4204831226f778c200d28109',), 'delivered-to': ('roor32@gmail.com',), 'received': ('by 10.64.10.4 with SMTP id 4cs594808qbj;\r\n        Fri, 20 Oct 2006 01:53:34 -0700 (PDT)', 'by 10.65.224.11 with SMTP id b11mr149813qbr;\r\n        Fri, 20 Oct 2006 01:53:34 -0700 (PDT)', 'from anis.telecom.uqam.ca (anis.telecom.uqam.ca [132.208.250.6])\r\n        by mx.google.com with ESMTP id e13si1575402qbe.2006.10.20.01.53.34;\r\n        Fri, 20 Oct 2006 01:53:34 -0700 (PDT)', 'from anis4.telecom.uqam.ca (anis4.telecom.uqam.ca [132.208.250.236])\r\n\tby sortant.uqam.ca (8.13.6/8.12.1) with SMTP id k9K8SIwA023763\r\n\tfor <roor32@gmail.com>; Fri, 20 Oct 2006 04:28:33 -0400 (EDT)', 'from antivirus.uqam.ca ([127.0.0.1])\r\n by anis4.telecom.uqam.ca (SAVSMTP 3.1.1.32) with SMTP id M2006102004283404041\r\n for <roor32@gmail.com>; Fri, 20 Oct 2006 04:28:34 -0400', 'from localhost (localhost)\r\n\tby antivirus.uqam.ca (8.13.6/8.12.1) id k9JMDbg4005560;\r\n\tFri, 20 Oct 2006 04:28:33 -0400 (EDT)'), 'return-path': ('<>',), 'received-spf': ('pass (google.com: best guess record for domain of anis.telecom.uqam.ca designates 132.208.250.6 as permitted sender)',), 'date': ('Fri, 20 Oct 2006 04:28:33 -0400 (EDT)',), 'from': ('Mail Delivery Subsystem <MAILER-DAEMON@antivirus.uqam.ca>',), 'message-id': ('<200610200828.k9JMDbg4005560@antivirus.uqam.ca>',), 'to': ('<roor32@gmail.com>',), 'mime-version': ('1.0',), 'content-type': ('multipart/report; report-type=delivery-status;\r\n\tboundary="k9JMDbg4005560.1161332913/antivirus.uqam.ca"',), 'subject': ('Warning: could not send message for past 1 day',), 'auto-submitted': ('auto-generated (warning-timeout)',)},
    attachments=[
        dict(
            filename='',
            content_id='',
            content_disposition='',
            content_type='message/rfc822',
            payload=b'Return-Path: <roor32@gmail.com>\nReceived: from py-out-1112.google.com (py-out-1112.google.com\n [64.233.166.178])\n\tby intrant.uqam.ca (8.13.6/8.12.2/uqam-filtres) with SMTP id k9J5Ni8o007263\n\tfor <larose.julie@courrier.uqam.ca>; Thu, 19 Oct 2006 01:23:47 -0400 (EDT)\nX-UQAM-Spam-Filter: Filtre-Uqam re:  abuse@uqam.ca\nReceived: by py-out-1112.google.com with SMTP id t32so610221pyc\n        for <larose.julie@courrier.uqam.ca>;\n Wed, 18 Oct 2006 22:23:33 -0700 (PDT)\nDomainKey-Signature: a=rsa-sha1; q=dns; c=nofws;\n        s=beta; d=gmail.com;\n        h=received:message-id:date:from:to:subject:mime-version:content-type:content-transfer-encoding:content-disposition;\n        b=Fwt0k1kaMU+1kM1iTG0q4Xf94p9alSohgM7QQN0CSjfBYUUhT+J4Y6+ZWotaaSffV3gX86RE/n97n0yQ/33EgYKIifuEpa0hi2mg3KTmcDqlCjiDfih58Z998GEFfbhu0he2jsoB+k6AgVRFPwP6LMRi6T66vr2f7IOAmX2IHiU=\nReceived: by 10.65.241.20 with SMTP id t20mr15391984qbr;\n        Wed, 18 Oct 2006 15:10:03 -0700 (PDT)\nReceived: by 10.64.10.4 with HTTP; Wed, 18 Oct 2006 15:10:03 -0700 (PDT)\nMessage-ID: <89d7557c0610181510r6fa5ebd8n66a7deec71ade118@mail.gmail.com>\nDate: Wed, 18 Oct 2006 18:10:03 -0400\nFrom: "=?ISO-8859-1?Q?RogE9?=" <roor32@gmail.com>\nTo: larose.julie@courrier.uqam.ca\nSubject: Est-ce toi ?\nMIME-Version: 1.0\nContent-Type: text/plain; charset=ISO-8859-1; format=flowed\nContent-Transfer-Encoding: 7bit\nContent-Disposition: inline\n\nSalut,\nje ne suis pas sur de m\'adresser a la bonne personne.\nMais si jamais tu me reconnais :p, peux-tu repondre a ce mail ?\nMerci.\nRoger\n',
        ),
        ],
    from_values=EmailAddress(name='Mail Delivery Subsystem', email='MAILER-DAEMON@antivirus.uqam.ca'),
    to_values=(EmailAddress(name='', email='roor32@gmail.com'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)