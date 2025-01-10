import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='[skynet-help][60666] How are intermediate files handled in SkyNet?',
    from_='noreply@rubyforge.org',
    to=('noreply@rubyforge.org',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2008, 9, 22, 15, 6, 28, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000))),
    date_str='Mon, 22 Sep 2008 15:06:28 -0400 (EDT)',
    text='Testing, testing, 123.',
    html='',
    headers={'delivered-to': ('xxx@xxx.com',), 'received': ('by 10.67.31.8 with SMTP id i8cs1195ugj;\r\n        Mon, 22 Sep 2008 13:45:18 -0700 (PDT)', 'by 10.100.207.5 with SMTP id e5mr3483815ang.104.1222110393505;\r\n        Mon, 22 Sep 2008 12:06:33 -0700 (PDT)', 'from rubyforge.org (rubyforge.org [205.234.109.19])\r\n        by mx.google.com with ESMTP id c2si899474ana.10.2008.09.22.12.06.28;\r\n        Mon, 22 Sep 2008 12:06:33 -0700 (PDT)', 'by rubyforge.org (Postfix, from userid 502)\r\n\tid 8FB1518581AC; Mon, 22 Sep 2008 15:06:28 -0400 (EDT)'), 'return-path': ('<noreply@rubyforge.org>',), 'received-spf': ('pass (google.com: best guess record for domain of noreply@rubyforge.org designates 205.234.109.19 as permitted sender) client-ip=205.234.109.19;',), 'authentication-results': ('mx.google.com; spf=pass (google.com: best guess record for domain of noreply@rubyforge.org designates 205.234.109.19 as permitted sender) smtp.mail=noreply@rubyforge.org',), 'to': ('noreply@rubyforge.org',), 'from': ('Sandy M. <noreply@rubyforge.org> ',), 'subject': ('[skynet-help][60666] How are intermediate files handled in SkyNet?',), 'content-type': ('text/plain; charset=UTF-8',), 'message-id': ('<20080922190628.8FB1518581AC@rubyforge.org>',), 'date': ('Mon, 22 Sep 2008 15:06:28 -0400 (EDT)',)},
    attachments=[],
    from_values=EmailAddress(name='Sandy M.', email='noreply@rubyforge.org'),
    to_values=(EmailAddress(name='', email='noreply@rubyforge.org'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)