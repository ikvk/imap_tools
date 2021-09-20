import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='/home/svn/public/minebox revision 214',
    from_='tim@powerupdev.comconcierge',
    to=('tim@powerupdev.comconcierge', '@powerupdev.com'),
    cc=(),
    bcc=(),
    reply_to=('tim@powerupdev.comconcierge', '@powerupdev.com'),
    date=datetime.datetime(2007, 10, 22, 23, 45, 23, tzinfo=datetime.timezone.utc),
    date_str='Mon, 22 Oct 2007 23:45:23 +0000 (UTC)',
    text='<p><b>recordkick</b> 2007-10-22 23:45:23 +0000 (Mon, 22 Oct 2007)</p><p>test\r\nsubversion<br>\r\n</p><hr noshade><pre><font color=\\"gray\\">Modified:\r\ntrunk/README\r\n===================================================================\r\n--- trunk/README\\t2007-10-22\r\n23:41:34 UTC (rev 213)\r\n+++ trunk/README\\t2007-10-22 23:45:23 UTC (rev 214)\r\n@@ -1,5 +1,5 @@\r\n == Welcome\r\nto Rails\r\n-Test\r\n+Tedst\r\n Rails is a web-application and persistence framework that includes everything\r\n needed\r\nto create database-backed web-applications according to the\r\n Model-View-Control pattern of separation. This pattern\r\nsplits the view (also\r\n\r\n</font>\r\n</pre>\r\n',
    html='',
    headers={'delivered-to': ('tim@powerupdev.com',), 'return-path': ('<www-data@mangaverde.net>',), 'to': ('tim@powerupdev.com concierge@powerupdev.com',), 'from': ('tim@powerupdev.com concierge@powerupdev.com',), 'subject': ('/home/svn/public/minebox revision 214',), 'reply-to': ('tim@powerupdev.com concierge@powerupdev.com',), 'message-id': ('<20071022234523.5BD8E86D2@mangaverde.net>',), 'date': ('Mon, 22 Oct 2007 23:45:23 +0000 (UTC)',)},
    attachments=[],
    from_values=EmailAddress('', 'tim@powerupdev.comconcierge', 'tim@powerupdev.comconcierge'),
    to_values=(EmailAddress('', 'tim@powerupdev.comconcierge', 'tim@powerupdev.comconcierge'), EmailAddress('', '@powerupdev.com', '@powerupdev.com')),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(EmailAddress('', 'tim@powerupdev.comconcierge', 'tim@powerupdev.comconcierge'), EmailAddress('', '@powerupdev.com', '@powerupdev.com')),
)