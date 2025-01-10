import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='MySurvey.com:  You have a survey waiting!  91123105',
    from_='carol@mysurvey.com',
    to=('someone@aol.com',),
    cc=(),
    bcc=(),
    reply_to=('carol@reply.mysurvey.com',),
    date=datetime.datetime(2010, 12, 15, 12, 21, 20, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=68400))),
    date_str='Wed, 15 Dec 2010 12:21:20 -0500 ',
    text="You have a survey waiting!\r\n\r\n\r\nTo take the survey:\r\n\r\n\r\n==================================================================\r\nPlease do not reply to this email, as we do not process emails sent to this address. To view FAQ's or to contact us, please go to our http://www.mysurvey.com/index.cfm?action=Main.lobbyGeneral&MyContent=contact page. \r\n==================================================================   \r\nYou received this email because you (or someone in your household) registered to be a MySurvey.com member. Being a MySurvey.com member means receiving periodic email invitations to give your opinions via e-surveys as well as being eligible for special projects and product tests. If you wish to be removed from the MySurvey.com panel, please click here to http://www.mysurvey.com/index.cfm?action=Main.lobbyGeneral&myContent=unsubscribes.\r\n==================================================================\r\n",
    html='<center>\r\nhello world\r\n</center>\r\n<IMG SRC="http://mailcenterus.mysurvey.com/gems_open_tracking.cfm?indid=99323446&cmpid=10000012106&r=9772160&rundate=15-DEC-2010+12%3a15%3a09&z=435ED3AE69D35EB44716E94814CD11A9"border="0" width="1" height="1">\r\n',
    headers={'received': ('from survey1usmta.mysurvey.com (survey1usmta.mysurvey.com [198.178.238.149])\r\n\tby mtain-dh02.r1000.mx.aol.com (Internet Inbound) with ESMTP id 35AF9380001BD\r\n\tfor <jjffddjkl161@aol.com>; Wed, 15 Dec 2010 12:22:13 -0500 (EST)', 'from 172.30.44.41 (172.30.44.57) by survey1usmta.mysurvey.com (PowerMTA(TM) v3.5r15) id h13ska0ko6cn for <jjffddjkl161@aol.com>; Wed, 15 Dec 2010 12:21:20 -0500 (envelope-from <carol-jjffddjkl161=aol.com@mysurvey.com>)'), 'from': ('=?UTF-8?B?TXlTdXJ2ZXk=?=\r\n =?UTF-8?B?LmNvbSAmIEM=?=\r\n =?UTF-8?B?YXJvbCBBZGE=?=\r\n =?UTF-8?B?bXM=?=\r\n <carol@mysurvey.com>',), 'reply-to': ('carol@reply.mysurvey.com',), 'to': ('someone@aol.com',), 'date': ('Wed, 15 Dec 2010 12:21:20 -0500 ',), 'subject': ('=?UTF-8?B?TXlTdXJ2ZXk=?=\r\n =?UTF-8?B?LmNvbTogIFk=?=\r\n =?UTF-8?B?b3UgaGF2ZSA=?=\r\n =?UTF-8?B?YSBzdXJ2ZXk=?=\r\n =?UTF-8?B?IHdhaXRpbmc=?=\r\n =?UTF-8?B?ISAg?=\r\n =?UTF-8?Q?91123105?=\r\n =?UTF-8?B??=\r\n ',), 'mime-version': ('1.0 ',), 'content-type': ('multipart/alternative;boundary="----=_Layout_Part_DC7E1BB5_1105_4DB3_BAE3_2A6208EB099A"',), 'x-aol-global-disposition': ('G',), 'x-aol-scoll-score': ('1:2:376293952:93952408  ',), 'x-aol-scoll-url_count': ('5  ',), 'x-aol-sid': ('3039ac1d41164d08f9453480',), 'x-aol-ip': ('198.178.238.149',), 'x-aol-spf': ('domain : mysurvey.com SPF : pass',)},
    attachments=[],
    from_values=EmailAddress(name='MySurvey.com & Carol Adams', email='carol@mysurvey.com'),
    to_values=(EmailAddress(name='', email='someone@aol.com'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(EmailAddress(name='', email='carol@reply.mysurvey.com'),),
)