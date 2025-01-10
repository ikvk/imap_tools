import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='Mail System Error - Returned Mail',
    from_='Postmaster@ci.com',
    to=('notification+promo@blah.com',),
    cc=(),
    bcc=(),
    reply_to=('Postmaster@ci.com',),
    date=datetime.datetime(2010, 6, 29, 10, 42, 44, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=68400))),
    date_str='Tue, 29 Jun 2010 10:42:44 -0500',
    text='This Message was undeliverable due to the following reason:\r\n<u@ci.com> has restricted SMS e-mail\r\nPlease reply to <Postmaster@ci.com>\r\nif you feel this message to be in error.Hey cingularmefarida,\n\nFarida Malik thinks you should apply to join HomeRun, your place fot., San Francisco, CA, 94123, USA',
    html="<!DOCTYPE html>\n<html>\n<head>\n<title>HomeRun - Your Friend Farida Malik wants you to join run.com/o.45b0d380.gif' width='1' />\n</td>\n</tr>\n</table>\n</td>\n</tr>\n</table>\n</div>\n</body>\n</html>\n",
    headers={'return-path': ('<>',), 'x-original-to': ('notification+promo@blah.com',), 'delivered-to': ('notification+promo@blah.com',), 'received': ('from schemailmta04.ci.com (schemailmta04.ci.com [209.183.37.58])\r\n    by blah.com (Postfix) with ESMTP id 24EF419F546\r\n    for <notification+promo@blah.com>; Tue, 29 Jun 2010 15:42:46 +0000 (UTC)',), 'to': ('notification+promo@blah.com',), 'from': ('Mail Administrator <Postmaster@ci.com>',), 'reply-to': ('<Postmaster@ci.com>',), 'subject': ('Mail System Error - Returned Mail',), 'date': ('Tue, 29 Jun 2010 10:42:44 -0500',), 'message-id': ('<20100629154244.OZPA15102.schemailmta04.ci.com@schemailmta04>',), 'mime-version': ('1.0',), 'content-type': ('multipart/report;\r\n        report-type=delivery-status;\r\n        Boundary="===========================_ _= 6078796(15102)1277826164"',), 'x-cloudmark-analysis': ('v=1.0 c=1 a=q8OS1GolVHwA:10 a=ev1gGZlfZ-EA:10 a=HQ-Cukr2AAAA:8 a=qihIh-XuXL65y3o_mUgA:9 a=mUL5bUDOV_-gjcCZylcY5Lz4jjsA:4 a=iQvSWfByulMA:10 a=ni8l3qMSI1sA:10 a=WHDNLAQ519cA:10 a=Fry9e7MVxuJdODrS104A:9 a=JYo4OF_E9TqbHrUN2TvLdggtx2cA:4 a=S0jCPnXDAAAA:8 a=pXkHMj1YAAAA:8 a=5ErcFzC0N3E7OloTRA8A:9 a=cC0RL7HlXt3RrKfnpEbxHCeM-zQA:4 a=cHEBK1Z0Lu8A:10 a=p9ZeupWRHUwA:10 a=7sPVfr_AX1EA:10',)},
    attachments=[
        dict(
            filename='',
            content_id='',
            content_disposition='',
            content_type='message/rfc822',
            payload=b'Received: from schemailedgegx04.ci.com ([172.16.130.170])\n          by schemailmta04.ci.com\n          (InterMail vM.6.01.04.00 201-2131-118-20041027) with ESMTP\n          id\n <20100629154237.OZBY15102.schemailmta04.ci.com@schemailedgegx04.ci.com>\n          for <u@ci.com>; Tue, 29 Jun 2010 10:42:37 -0500\nReceived: from blah.com ([1.1.1.1])\n          by schemailedgegx04.ci.com\n          (InterMail vG.1.02.00.04 201-2136-104-104-20050323) with ESMTP\n          id <20100629154225.WEFB17009.schemailedgegx04.ci.com@blah.com>\n          for <u@ci.com>; Tue, 29 Jun 2010 10:42:25 -0500\nReceived: from blah.com (snooki [10.12.126.68])\n    by blah.com (Postfix) with ESMTP id 4BDAE19F546\n    for <u@ci.com>; Tue, 29 Jun 2010 15:42:25 +0000 (UTC)\nDKIM-Signature: v=1; a=rsa-sha256; c=simple/simple; d=blah.com;\n    s=2010; t=1277826145; bh=wC3hHAhQgApcTmwQsi2F4OJf40rbyIek/WwIuzSc3V\n    M=; h=Date:From:Reply-To:To:Message-ID:Subject:Mime-Version:\n     Content-Type:Content-Transfer-Encoding:List-Unsubscribe; b=aw+Bhd8\n    t1goZUXWBAHSrHaM1IdqhkXqF5WVMwGRYcnya4FHNw05XfpB3TTpTFda13DfhtziFRk\n    zHSfiNbMapv7Vz+D3A/9NHg5nKahSMosZVTa0BfajYWNd1aY8JUWUlxdQHxQQ4ygCBj\n    /MndJohtSm6K3gsqdIv88DNXdBGBEw=\nDate: Tue, 29 Jun 2010 15:42:25 +0000\nFrom: HomeRun <notification@blah.com>\nReply-To: HomeRun <notification+45b0d380@blah.com>\nTo: u@ci.com\nMessage-ID: <4c2a146147ac8_61ff157c4ec1652df@s.h.c.mail>\nSubject: Your Friend F M wants you to join HomeRun\nMime-Version: 1.0\nContent-Type: multipart/alternative;\n boundary="--==_mimepart_4c2a146141756_61ff157c4ec1649a8";\n charset=UTF-8\nContent-Transfer-Encoding: 7bit\nList-Unsubscribe: <mailto:unsubscribe+45b0d380@blah.com>\n\n\n\n----==_mimepart_4c2a146141756_61ff157c4ec1649a8\nDate: Tue, 29 Jun 2010 15:42:25 +0000\nMime-Version: 1.0\nContent-Type: text/plain;\n charset=UTF-8\nContent-Transfer-Encoding: base64\nContent-ID: <4c2a146145451_61ff157c4ec165040@s.h.c.mail>\n\nSGV5IGNpbmd1bGFybWVmYXJpZGEsCgpGYXJpZGEgTWFsaWsgdGhpbmtzIHlv\ndSBzaG91bGQgYXBwbHkgdG8gam9pbiBIb21lUnVuLCB5b3VyIHBsYWNlIGZv\ndC4sIFNhbiBGcmFuY2lzY28sIENBLCA5NDEyMywgVVNB\n\n\n----==_mimepart_4c2a146141756_61ff157c4ec1649a8\nDate: Tue, 29 Jun 2010 15:42:25 +0000\nMime-Version: 1.0\nContent-Type: text/html;\n charset=UTF-8\nContent-Transfer-Encoding: base64\nContent-ID: <4c2a1461468ae_61ff157c4ec165194@s.h.c.mail>\n\nPCFET0NUWVBFIGh0bWw+CjxodG1sPgo8aGVhZD4KPHRpdGxlPkhvbWVSdW4g\nLSBZb3VyIEZyaWVuZCBGYXJpZGEgTWFsaWsgd2FudHMgeW91IHRvIGpvaW4g\ncnVuLmNvbS9vLjQ1YjBkMzgwLmdpZicgd2lkdGg9JzEnIC8+CjwvdGQ+Cjwv\ndHI+CjwvdGFibGU+CjwvdGQ+CjwvdHI+CjwvdGFibGU+CjwvZGl2Pgo8L2Jv\nZHk+CjwvaHRtbD4K\n\n\n----==_mimepart_4c2a146141756_61ff157c4ec1649a8--\n',
        ),
        
        dict(
            filename='',
            content_id='4c2a146145451_61ff157c4ec165040@s.h.c.mail',
            content_disposition='',
            content_type='text/plain',
            payload=b'Hey cingularmefarida,\n\nFarida Malik thinks you should apply to join HomeRun, your place fot., San Francisco, CA, 94123, USA',
        ),
        
        dict(
            filename='',
            content_id='4c2a1461468ae_61ff157c4ec165194@s.h.c.mail',
            content_disposition='',
            content_type='text/html',
            payload=b"<!DOCTYPE html>\n<html>\n<head>\n<title>HomeRun - Your Friend Farida Malik wants you to join run.com/o.45b0d380.gif' width='1' />\n</td>\n</tr>\n</table>\n</td>\n</tr>\n</table>\n</div>\n</body>\n</html>\n",
        ),
        ],
    from_values=EmailAddress(name='Mail Administrator', email='Postmaster@ci.com'),
    to_values=(EmailAddress(name='', email='notification+promo@blah.com'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(EmailAddress(name='', email='Postmaster@ci.com'),),
)