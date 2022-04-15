import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='40% OFF holiday patterns and fabric!',
    from_='enews@Free-Quilting.com',
    to=('someone@live.com',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(1900, 1, 1, 0, 0),
    date_str='Wed, 15 Dec 2010    59:10 -0500',
    text='',
    html='',
    headers={'x-message-delivery': ('Vj0xLjE7dXM9MDtsPTA7YT0xO0Q9MTtTQ0w9MA==',), 'x-message-status': ('n',), 'x-sid-pra': ('enews@Free-Quilting.com',), 'x-auth-result': ('NONE',), 'x-message-info': ('JGTYoYF78jHCcITVD+zs6u3ahcolNfp0m61kNO2SBMwKZtwdSoGZLR+eV3xtqv3QU2mvP3b1AtESP6eCYbaI4dABkTSkMMCjZGPGH3Q01dsRSddQ0kCWDw==',), 'received': ('from drg.drgnetwork.com ([63.76.155.39]) by col0-mc2-f14.Col0.hotmail.com with Microsoft SMTPSVC(6.0.3790.4675);\r\n\t Tue, 14 Dec 2010 22:59:10 -0800', 'from SFGAS1.DRGNETWORK.COM (sfgas1.drgnetwork.com [63.76.155.11])\r\n\tby drg.drgnetwork.com (8.13.8/8.13.8) with ESMTP id oBF6xAuc018214\r\n\tfor <someone@live.com>; Wed, 15 Dec 2010 00:59:10 -0600'), 'message-id': ('<201012150659.oBF6xAuc018214@drg.drgnetwork.com>',), 'sender': ('enews@Free-Quilting.com',), 'date': ('Wed, 15 Dec 2010    59:10 -0500',), 'from': ('"Free-Quilting.com" <enews@Free-Quilting.com>',), 'mime-version': ('1.0',), 'to': ('<someone@live.com>',), 'cc': ('',), 'subject': ('40% OFF holiday patterns and fabric!',), 'content-type': ('multipart/alternative; boundary="--PART.BOUNDARY.0001"',), 'return-path': ('bounces@strategicfulfillment.com',), 'x-originalarrivaltime': ('15 Dec 2010 06:59:10.0647 (UTC) FILETIME=[93232C70:01CB9C25]',)},
    attachments=[],
    from_values=EmailAddress(name='Free-Quilting.com', email='enews@Free-Quilting.com'),
    to_values=(EmailAddress(name='', email='someone@live.com'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)