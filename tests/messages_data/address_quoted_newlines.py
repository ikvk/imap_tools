import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='Daily',
    from_='status@sender.com',
    to=('my.name@domain.com', 'other.name@domain.com'),
    cc=('third.name@domain.com', 'quoted-mailing-list-one@domain.com', 'quoted-mailing-list-two@domain.com'),
    bcc=('my.name@domain.com', 'list1-one-name@domain.com', 'list2-second-name@domain.com'),
    reply_to=(),
    date=datetime.datetime(2020, 11, 1, 14, 49, 7, tzinfo=datetime.timezone(datetime.timedelta(-1, 57600))),
    date_str='Mon, 01 Nov 2020 14:49:07 -0800 (PST)',
    text='Daily Data: D09.ZPH (Averaged data)\nEmail generated: 10/11/2020 00:04:03.765\nEmail sent: 10/11/2020 00:49:03.125',
    html='',
    headers={'message-id': ('<5fa9c763>',), 'date': ('Mon, 01 Nov 2020 14:49:07 -0800 (PST)',), 'mime-version': ('1.0',), 'from': ('"Sender" <status@sender.com>',), 'to': ('My Name <my.name@domain.com>, Other Name\r\n    <other.name@domain.com>',), 'cc': ('Third Name <third.name@domain.com>, "Quoted Mailing List\r\n One" <quoted-mailing-list-one@domain.com>, "Quoted\r\n Mailing List Two" <quoted-mailing-list-two@domain.com>',), 'bcc': ('My Name <my.name@domain.com>, Mailing List One - One Name\r\n    <list1-one-name@domain.com>, Mailing List Two - Second Name\r\n    <list2-second-name@domain.com>',), 'subject': ('Daily',), 'content-type': ('multipart/mixed; boundary=--boundary_20_d4727d16-8454-4fa4-9da0-950a95b2c962',)},
    attachments=[
        dict(
            filename='D09.ZPH.txt',
            content_id='',
            content_disposition='',
            content_type='application/octet-stream',
            payload=b'12',
        ),
        ],
    from_values=EmailAddress('Sender', 'status@sender.com', 'Sender <status@sender.com>'),
    to_values=(EmailAddress('My Name', 'my.name@domain.com', 'My Name <my.name@domain.com>'), EmailAddress('Other Name', 'other.name@domain.com', 'Other Name <other.name@domain.com>')),
    cc_values=(EmailAddress('Third Name', 'third.name@domain.com', 'Third Name <third.name@domain.com>'), EmailAddress('Quoted Mailing List One', 'quoted-mailing-list-one@domain.com', 'Quoted Mailing List One <quoted-mailing-list-one@domain.com>'), EmailAddress('Quoted Mailing List Two', 'quoted-mailing-list-two@domain.com', 'Quoted Mailing List Two <quoted-mailing-list-two@domain.com>')),
    bcc_values=(EmailAddress('My Name', 'my.name@domain.com', 'My Name <my.name@domain.com>'), EmailAddress('Mailing List One - One Name', 'list1-one-name@domain.com', 'Mailing List One - One Name <list1-one-name@domain.com>'), EmailAddress('Mailing List Two - Second Name', 'list2-second-name@domain.com', 'Mailing List Two - Second Name <list2-second-name@domain.com>')),
    reply_to_values=(),
)