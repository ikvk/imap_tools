import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='Testing outlook',
    from_='email_test@me.nowhere',
    to=('mikel@me.nowhere',),
    cc=(),
    bcc=(),
    reply_to=('email_test@me.nowhere',),
    date=datetime.datetime(2007, 10, 21, 19, 38, 13, tzinfo=datetime.timezone(datetime.timedelta(seconds=36000))),
    date_str='Sun, 21 Oct 2007 19:38:13 +1000',
    text='Hello\r\nThis is an outlook test\r\n\r\nSo there.\r\n\r\nMe.\r\n',
    html='<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">\r\n<HTML><HEAD>\r\n<META http-equiv=Content-Type content="text/html; charset=utf-8">\r\n<META content="MSHTML 6.00.6000.16525" name=GENERATOR>\r\n<STYLE></STYLE>\r\n</HEAD>\r\n<BODY bgColor=#ffffff>\r\n<DIV><FONT face=Arial size=2>Hello</FONT></DIV>\r\n<DIV><FONT face=Arial size=2><STRONG>This is an outlook \r\ntest</STRONG></FONT></DIV>\r\n<DIV><FONT face=Arial size=2><STRONG></STRONG></FONT>&nbsp;</DIV>\r\n<DIV><FONT face=Arial size=2><STRONG>So there.</STRONG></FONT></DIV>\r\n<DIV><FONT face=Arial size=2></FONT>&nbsp;</DIV>\r\n<DIV><FONT face=Arial size=2>Me.</FONT></DIV></BODY></HTML>\r\n\r\n',
    headers={'return-path': ('<email_test@me.nowhere>',), 'received': ('from omta05sl.mx.bigpond.com by me.nowhere.else with ESMTP id 632BD5758 for <mikel@me.nowhere.else>; Sun, 21 Oct 2007 19:38:21 +1000', 'from oaamta05sl.mx.bigpond.com by omta05sl.mx.bigpond.com with ESMTP id <20071021093820.HSPC16667.omta05sl.mx.bigpond.com@oaamta05sl.mx.bigpond.com> for <mikel@me.nowhere.else>; Sun, 21 Oct 2007 19:38:20 +1000', 'from mikel091a by oaamta05sl.mx.bigpond.com with SMTP id <20071021093820.JFMT24025.oaamta05sl.mx.bigpond.com@mikel091a> for <mikel@me.nowhere.else>; Sun, 21 Oct 2007 19:38:20 +1000'), 'date': ('Sun, 21 Oct 2007 19:38:13 +1000',), 'from': ('Mikel Lindsaar <email_test@me.nowhere>',), 'reply-to': ('Mikel Lindsaar <email_test@me.nowhere>',), 'to': ('mikel@me.nowhere',), 'message-id': ('<009601c813c6$19df3510$0437d30a@mikel091a>',), 'subject': ('Testing outlook',), 'mime-version': ('1.0',), 'content-type': ('multipart/alternative; boundary="----=_NextPart_000_0093_01C81419.EB75E850"',), 'x-get_mail_default': ('mikel@me.nowhere.else',), 'x-priority': ('3',), 'x-original-to': ('mikel@me.nowhere',), 'x-mailer': ('Microsoft Outlook Express 6.00.2900.3138',), 'delivered-to': ('mikel@me.nowhere',), 'x-mimeole': ('Produced By Microsoft MimeOLE V6.00.2900.3138',), 'x-msmail-priority': ('Normal',)},
    attachments=[],
    from_values=EmailAddress(name='Mikel Lindsaar', email='email_test@me.nowhere'),
    to_values=(EmailAddress(name='', email='mikel@me.nowhere'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(EmailAddress(name='Mikel Lindsaar', email='email_test@me.nowhere'),),
)