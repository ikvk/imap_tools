import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='Nicolas Fouché has accepted your invitation to Gmail',
    from_='gmail-noreply@google.com',
    to=('a.b@gmail.com',),
    cc=(),
    bcc=(),
    reply_to=('x.y@gmail.com',),
    date=datetime.datetime(2005, 6, 28, 1, 2, 11, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=61200))),
    date_str='Tue, 28 Jun 2005 01:02:11 -0700',
    text='Nicolas Fouché has accepted your invitation to Gmail and has chosen the \r\nbrand new address x.y@gmail.com. Be one of the first to email Nicolas \r\nat this new Gmail address--just hit reply and send Nicolas a message. \r\nx.y@gmail.com has also been automatically added to your contact list \r\nso you can stay in touch with Gmail. \r\n\r\n\r\nThanks, \r\n\r\nThe Gmail Team\r\n',
    html='<html>\r\n<font face="Arial, Helvetica, sans-serif">\r\n<p>Nicolas Fouché has accepted your invitation to Gmail and has\r\n  chosen the brand new address x.y@gmail.com. Be one of the first to email \r\n  Nicolas at this new Gmail address--just hit reply and send \r\n  Nicolas a message. x.y@gmail.com has also been automatically added to\r\n  your contact list so you can stay in touch with Gmail.\r\n</p>\r\n<p><br>\r\n  Thanks, </p>\r\n<p> The Gmail Team</p>\r\n</font>\r\n</html>\r\n',
    headers={'x-gmail-received': ('220984aec4c4885e060987be043c9363cbef8551',), 'received': ('by 10.36.47.16; Tue, 28 Jun 2005 01:02:11 -0700 (PDT)',), 'message-id': ('<89d7557c0506280102495d555f@mail.gmail.com>',), 'date': ('Tue, 28 Jun 2005 01:02:11 -0700',), 'from': ('Gmail Team <gmail-noreply@google.com>',), 'reply-to': ('x.y@gmail.com',), 'to': ('=?ISO-8859-1?Q?Nicolas_Fouch=E9?= <a.b@gmail.com>',), 'subject': ('=?ISO-8859-1?Q?Nicolas_Fouch=E9_has_accepted_your_invitation_to_Gmail?=',), 'mime-version': ('1.0',), 'content-type': ('multipart/alternative; \r\n\tboundary="----=_Part_976_15222032.1119945731186"',)},
    attachments=[],
    from_values=EmailAddress(name='Gmail Team', email='gmail-noreply@google.com'),
    to_values=(EmailAddress(name='Nicolas Fouché', email='a.b@gmail.com'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(EmailAddress(name='', email='x.y@gmail.com'),),
)