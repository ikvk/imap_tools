import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='Re: We will help you refinance your home.',
    from_='abhijit.862153drinnan@datavalet.com',
    to=('cvs@bruce-guenter.dyndns.org',),
    cc=('rait@bruce-guenter.dyndns.org',),
    bcc=(),
    reply_to=('abhijit.862153drinnan@datavalet.com',),
    date=datetime.datetime(2005, 5, 6, 15, 55, 1, tzinfo=datetime.timezone(datetime.timedelta(seconds=14400))),
    date_str='Fri, 06 May 2005 15:55:01 +0400',
    text='',
    html='Hello,<p>\r\n\r\nYou have qualified for the lowest rate in years.<br>\r\nYou could get over $400,000 for as little as $500 a month.<br>\r\nLow rates are fixed no matter what.<p>\r\n\r\nPlease visit the link below to verify your information:<br>\r\n<a href="http://www.lenxzc.com/index2.php?refid=malx">Approval Form</a><p>\r\n\r\nBest Regards,<br>\r\nchianfong cuthbert, Account Manager<br>\r\nReynolds Associates, LLC<p>\r\n<p>\r\n--------------------<br>\r\nif you received this in error: <a href="http://www.lenxzc.com/r.php">re-m0-ve</a>\r\n',
    headers={'return-path': ('<hzwfrkq@hintontile.com>',), 'delivered-to': ('rait@bruce-guenter.dyndns.org',), 'received': ('(qmail 12977 invoked from network); 6 May 2005 10:58:40 -0000', 'from localhost (localhost [127.0.0.1])\r\n  by bruce-guenter.dyndns.org ([192.168.1.3]); 06 May 2005 10:58:40 -0000', 'from zak.futurequest.net ([127.0.0.1])\r\n  by localhost ([127.0.0.1])\r\n  with SMTP via TCP; 06 May 2005 10:58:40 -0000', '(qmail 2252 invoked from network); 6 May 2005 10:58:39 -0000', 'from lsne-catv-dhcp-29-115.urbanet.ch (unknown [80.238.29.115])\r\n  by zak.futurequest.net ([69.5.6.152])\r\n  with SMTP via TCP; 06 May 2005 10:58:29 -0000', 'from mail.datavalet.com (80.238.29.115)\r\n          by 80.238.29.115 (fairwayv.4) with SMTP\r\n          id <09166i58p>\r\n          (Authid: 3811297); Fri, 06 May 2005 10:52:01 -0100'), 'reply-to': ('"chianfong cuthbert" <abhijit.862153drinnan@datavalet.com>',), 'from': ('"chianfong cuthbert" <abhijit.862153drinnan@datavalet.com>',), 'to': ('cvs@bruce-guenter.dyndns.org',), 'cc': ('rait@bruce-guenter.dyndns.org',), 'subject': ('Re: We will help you refinance your home.',), 'date': ('Fri, 06 May 2005 15:55:01 +0400',), 'mime-version': ('1.0',), 'content-type': ('multipart/alternative;\r\n\tboundary="--651790_269334.01570"',), 'content-length': ('636',), 'lines': ('22',)},
    attachments=[],
    from_values=EmailAddress(name='chianfong cuthbert', email='abhijit.862153drinnan@datavalet.com'),
    to_values=(EmailAddress(name='', email='cvs@bruce-guenter.dyndns.org'),),
    cc_values=(EmailAddress(name='', email='rait@bruce-guenter.dyndns.org'),),
    bcc_values=(),
    reply_to_values=(EmailAddress(name='chianfong cuthbert', email='abhijit.862153drinnan@datavalet.com'),),
)