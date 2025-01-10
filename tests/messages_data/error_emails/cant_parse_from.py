import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='Meet the new MacBook Pro family. Now includes 13-inch.',
    from_='News@InsideApple.Apple.com',
    to=('karl.baum@gmail.com',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2009, 6, 11, 23, 25, 2, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=61200))),
    date_str='Thu, 11 Jun 2009 23:25:02 -0700',
    text="From one solid piece of aluminum comes a MacBook Pro that's thin and light, beautifully streamlined, and durable.\r\n",
    html='<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">\r\n<html>\r\n<head>\r\n<body>\r\nFrom one solid piece of aluminum comes a MacBook Pro that\'s thin and light, beautifully streamlined, and durable.<br><a href="http://insideapple.app</body>\r\n</html>\r\n',
    headers={'date': ('Thu, 11 Jun 2009 23:25:02 -0700',), 'from': ('Apple <News@InsideApple.Apple.com>',), 'to': ('karl.baum@gmail.com',), 'message-id': ('<7oh6b1$1clhrjk@badger-vip.apple.com>',), 'subject': ('Meet the new MacBook Pro family. Now includes 13-inch.',), 'mime-version': ('1.0',), 'content-type': ('multipart/alternative; boundary=mimepart_4b0c353551675_3d1c15b79ea5e70c1783',)},
    attachments=[],
    from_values=EmailAddress(name='Apple', email='News@InsideApple.Apple.com'),
    to_values=(EmailAddress(name='', email='karl.baum@gmail.com'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)