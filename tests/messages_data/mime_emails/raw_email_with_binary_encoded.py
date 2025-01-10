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
    text='',
    html='',
    headers={'return-path': ('<email_test@me.nowhere>',), 'received': ('from omta05sl.mx.bigpond.com by me.nowhere.else with ESMTP id 632BD5758 for <mikel@me.nowhere.else>; Sun, 21 Oct 2007 19:38:21 +1000', 'from oaamta05sl.mx.bigpond.com by omta05sl.mx.bigpond.com with ESMTP id <20071021093820.HSPC16667.omta05sl.mx.bigpond.com@oaamta05sl.mx.bigpond.com> for <mikel@me.nowhere.else>; Sun, 21 Oct 2007 19:38:20 +1000', 'from mikel091a by oaamta05sl.mx.bigpond.com with SMTP id <20071021093820.JFMT24025.oaamta05sl.mx.bigpond.com@mikel091a> for <mikel@me.nowhere.else>; Sun, 21 Oct 2007 19:38:20 +1000'), 'date': ('Sun, 21 Oct 2007 19:38:13 +1000',), 'from': ('Mikel Lindsaar <email_test@me.nowhere>',), 'reply-to': ('Mikel Lindsaar <email_test@me.nowhere>',), 'to': ('mikel@me.nowhere',), 'message-id': ('<009601c813c6$19df3510$0437d30a@mikel091a>',), 'subject': ('Testing outlook', 'Another PDF'), 'mime-version': ('1.0',), 'content-type': ('multipart/alternative;\r\n  boundary=----=_Part_13069834_15179892.1376435426074',)},
    attachments=[
        dict(
            filename='2013-08-13_19-08-28-1.jpg',
            content_id='',
            content_disposition='',
            content_type='image/jpeg',
            payload=b'BINARY_CONTENT_GOES_HERE',
        ),
        ],
    from_values=EmailAddress(name='Mikel Lindsaar', email='email_test@me.nowhere'),
    to_values=(EmailAddress(name='', email='mikel@me.nowhere'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(EmailAddress(name='Mikel Lindsaar', email='email_test@me.nowhere'),),
)