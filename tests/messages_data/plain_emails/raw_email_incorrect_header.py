import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='',
    from_='',
    to=(),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(1900, 1, 1, 0, 0),
    date_str='',
    text='quite Delivered-To: xxx@xxx.xxx\r\nReceived: by xxx.xxx.xxx (Wostfix, from userid xxx)\r\n\t  id 0F87F333; Wed, 23 Feb 2005 16:16:17 -0600\r\nDate: Wed, 23 Feb 2005 18:20:17 -0400\r\nFrom: "xxx xxx" <xxx@xxx.xxx>\r\nMessage-ID: <4D6AA7EB.6490534@xxx.xxx>\r\nTo: xxx@xxx.com\r\nSubject: Stop adware/spyware once and for all. \r\nX-Scanned-By: MIMEDefang 2.11 (www dot roaringpenguin dot com slash mimedefang)\r\n\r\nYou are infected with: \r\nAd Ware and Spy Ware\r\n\r\nGet your free scan and removal download now, \r\nbefore it gets any worse. \r\n\r\nhttp://xxx.xxx.info?aid=3D13&?stat=3D4327kdzt\r\n\r\n\r\n\r\n\r\nno more? (you will still be infected) \r\nhttp://xxx.xxx.info/discon/?xxx@xxx.com\r\n',
    html='',
    headers={'received': ('from xxx.xxx.xxx ([xxx.xxx.xxx.xxx] verified)\r\n  by xxx.com (CommuniGate Pro SMTP 4.2.8)\r\n  with SMTP id 2532598 for xxx@xxx.com; Wed, 23 Feb 2005 17:51:49 -0500',), 'received-spf': ('softfail\r\n receiver=xxx.com; client-ip=xxx.xxx.xxx.xxx; envelope-from=xxx@xxx.xxx',)},
    attachments=[],
    from_values=None,
    to_values=(),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)