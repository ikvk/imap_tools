import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='PGP Comments on RTO West Release of Dec. 14',
    from_='lpeters@PACIFIER.COM',
    to=('RRGA-L@LIST.RTOWEST.ORG',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2002, 1, 10, 13, 59, 53, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=57600))),
    date_str='Thu, 10 Jan 2002 13:59:53 -0800',
    text='Attached are the comments of the Public Generating Pool.\r\n--\r\n_________________________________\r\nLon L. Peters\r\nNorthwest Economic Research, Inc.\r\n6765 S.W. Preslynn Drive\r\nPortland, Oregon 97225-2668\r\n503-203-1539 (voice)\r\n503-203-1569 (fax)\r\n503-709-5942 (mobile)\r\nlpeters@pacifier.com\r\n\r\nNOTICE:  This communication and its attachments, if any, may contain\r\nsensitive, privileged, or other confidential information.  If you are\r\nnot the intended recipient or believe that you have received this\r\ncommunication in error, please notify the sender of this\r\ncommunication and delete the copy you received from all storage\r\ndevices.  In addition, please do not print, copy, retransmit,\r\nforward, disseminate, or otherwise use this communication or its\r\nattachments, if any.  Thank you.\r\n',
    html='',
    headers={'received': ('from nahou-mscnx06p.corp.enron.com ([192.168.110.237]) by napdx-msmbx01v.corp.enron.com with Microsoft SMTPSVC(5.0.2195.2966);\r\n\t Thu, 10 Jan 2002 14:12:53 -0800', 'from NAHOU-MSMSW06P.corp.enron.com ([192.168.110.228]) by nahou-mscnx06p.corp.enron.com with Microsoft SMTPSVC(5.0.2195.2966);\r\n\t Thu, 10 Jan 2002 16:12:52 -0600', 'from mailman.enron.com (unverified) by NAHOU-MSMSW06P.corp.enron.com\r\n (Content Technologies SMTPRS 4.2.5) with ESMTP id <T585d94ff81c0a86ee487c@NAHOU-MSMSW06P.corp.enron.com>;\r\n Thu, 10 Jan 2002 16:12:47 -0600', 'from tblexch01.transmission.bpa.gov (int.transmission.bpa.gov [206.137.58.133] (may be forged))\r\n\tby mailman.enron.com (8.11.4/8.11.4/corp-1.06) with ESMTP id g0AMCB920856;\r\n\tThu, 10 Jan 2002 16:12:11 -0600 (CST)', 'from TBLLIST1 ([206.137.58.134]) by tblexch01.transmission.bpa.gov with SMTP (Microsoft Exchange Internet Mail Service Version 5.5.2650.21)\r\n\tid CRWWC3K1; Thu, 10 Jan 2002 14:11:55 -0800', 'from LIST.TRANSMISSION.BPA.GOV by LIST.TRANSMISSION.BPA.GOV\r\n          (LISTSERV-TCP/IP release 1.8c) with spool id 2458 for\r\n          RRGA-L@LIST.TRANSMISSION.BPA.GOV; Thu, 10 Jan 2002 14:13:50 -0800', 'from [207.202.136.216] (ip136.r2.d.pdx.nwlink.com [207.202.136.136])\r\n          by comet.pacifier.com (8.11.2/8.11.1) with ESMTP id g0ALxLX06696;\r\n          Thu, 10 Jan 2002 13:59:21 -0800 (PST)'), 'mime-version': ('1.0',), 'x-sender': ('lpeters@mail.pacifier.com',), 'references': ('<1168BAF252B7D41194810001028D743108913C@SERVER>',), 'content-type': ('multipart/mixed;\r\n              boundary="============_-1201422494==_============"',), 'message-id': ('<p05100307b863befdfb67@[207.202.136.216]>',), 'date': ('Thu, 10 Jan 2002 13:59:53 -0800',), 'sender': ('RTO West Regional Representatives Group <RRGA-L@LIST.RTOWEST.ORG>',), 'from': ('"Lon L. Peters" <lpeters@PACIFIER.COM>',), 'subject': ('PGP Comments on RTO West Release of Dec. 14',), 'comments': ('cc: ltopaz@gcpud.org, gary.zarker@ci.seattle.wa.us,\r\n          dgodard@gcpud.org, wdobbins@dcpud.org, drobinson@cowlitzpud.org,\r\n          bgeddes@popud.com, "Culbertson, Tim" <tculber@gcpud.org>,\r\n          kknitte@gcpud.org, paula.green@ci.seattle.wa.us,\r\n          jim.harding@ci.seattle.wa.us, ghuhta@cowlitzpud.org,\r\n          dosborn@gcpud.org, jscheel@popud.com, jim.todd@ci.seattle.wa.us,\r\n          CWAGERS@dcpud.org, ali.rodol@ci.seattle.wa.us,\r\n          kevin.clark@ci.seattle.wa.us, bessex@cowlitzpud.org,\r\n          Cindy.Wright@ci.seattle.wa.us, "Juj, Hardev" \r\n          <Hardev.Juj@ci.seattle.wa.us>,\r\n          "Conger, Kurt" <kconger@energyexpertsvcs.com>,\r\n          "Kindley, Ray" <rkindley@schwabe.com>',), 'to': ('RRGA-L@LIST.RTOWEST.ORG',), 'in-reply-to': ('<1168BAF252B7D41194810001028D743108913C@SERVER>',), 'return-path': ('owner-rrga-l@list.rtowest.org',)},
    attachments=[
        dict(
            filename='PGP_Cmts_on_12-14-01_Pkg.doc',
            content_id='p05100307b863befdfb67@[207.202.136.216].0.0',
            content_disposition='attachment',
            content_type='application/msword',
            payload=b'',
        ),
        ],
    from_values=EmailAddress(name='Lon L. Peters', email='lpeters@PACIFIER.COM'),
    to_values=(EmailAddress(name='', email='RRGA-L@LIST.RTOWEST.ORG'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)