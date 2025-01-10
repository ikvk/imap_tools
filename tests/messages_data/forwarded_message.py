import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='статус',
    from_='i.kor@company.ru',
    to=('jessica.schmidt@uni.de', 'я你Rabea.Bartölke@uni.de'),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2017, 10, 12, 9, 41, 56, tzinfo=datetime.timezone(datetime.timedelta(seconds=18000))),
    date_str='Thu, 12 Oct 2017 09:41:56 +0500',
    text='\r\nНовый заказ №28922 http://group.company.ru/ru/order/28922/process/\r\nСоздал: \r\nКлиент Ковчег (Гусев Дмитрий)\r\n\r\nСегменты:\r\n\r\n- Москва - Тель-Авив, some-889, 15.03.2018, эконом: (15 взр.)\r\n\r\n- Тель-Авив - Москва, some-890, 22.03.2018, эконом: (15 взр.)',
    html='\r\n\r\n    <!DOCTYPE html PUBLIC \'-//W3C//DTD XHTML 1.0 Strict//EN\' \'http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\'>\r\n    <html xmlns=\'http://www.w3.org/1999/xhtml\' lang=\'ru-ru\'\r\n          xml:lang=\'en-us\'>\r\n    <head>\r\n        <meta content="text/html; charset=utf-8" http-equiv="Content-Type">\r\n        \r\n    </head>\r\n\r\n    <body id=\'body\'>\r\n    \r\n    \r\n        \r\n        <a href="http://group.company.ru/ru/order/28922/process/">\r\n            \r\n            Новый заказ №28922\r\n        </a>\r\n\r\n    </body>\r\n    </html>\r\n\r\n',
    headers={'subject': ('=?UTF-8?B?0YHRgtCw0YLRg9GB?=',), 'to': ('Jessica Schmidt <jessica.schmidt@uni.de>,\r\n\t=?iso-8859-1?Q?Rabea=2EBart=F6lke=40uni=2Ede?= <\udcd1\udc8f\udce4\udcbd\udca0Rabea.Bart\udcc3\udcb6lke@uni.de>',), 'from': ('i.kor@company.ru',), 'message-id': ('<2405271c-86ac-0a65-e50c-d1ebccfcc644@company.ru>',), 'date': ('Thu, 12 Oct 2017 09:41:56 +0500',), 'mime-version': ('1.0',), 'in-reply-to': ('<20171011085432.15374.20485@web.hades.company>',), 'content-type': ('multipart/mixed;\r\n boundary="------------BF90926EC9DF73443A6B8F28"',), 'content-language': ('ru',)},
    attachments=[
        dict(
            filename='',
            content_id='',
            content_disposition='attachment',
            content_type='message/rfc822',
            payload=b'Content-Type: multipart/alternative;\n boundary="===============3693132879591888836=="\nMIME-Version: 1.0\nSubject: =?UTF-8?B?0YHRgtCw0YLRg9GB?=    \nFrom: group@company.ru\nTo: group@company.ru\nDate: Wed, 11 Oct 2017 08:54:32 -0000\nMessage-ID: <20171011085432.15374.20485@web.hades.company>\n\n--===============3693132879591888836==\nContent-Type: text/plain; charset="utf-8"\nMIME-Version: 1.0\nContent-Transfer-Encoding: quoted-printable\n\n=D0=9D=D0=BE=D0=B2=D1=8B=D0=B9 =D0=B7=D0=B0=D0=BA=D0=B0=D0=B7 =E2=84=9628=\n922 http://group.company.ru/ru/order/28922/process/\n=D0=A1=D0=BE=D0=B7=D0=B4=D0=B0=D0=BB:=20\n=D0=9A=D0=BB=D0=B8=D0=B5=D0=BD=D1=82 =D0=9A=D0=BE=D0=B2=D1=87=D0=B5=D0=B3=\n (=D0=93=D1=83=D1=81=D0=B5=D0=B2 =D0=94=D0=BC=D0=B8=D1=82=D1=80=D0=B8=D0=B9=\n)\n\n=D0=A1=D0=B5=D0=B3=D0=BC=D0=B5=D0=BD=D1=82=D1=8B:\n\n- =D0=9C=D0=BE=D1=81=D0=BA=D0=B2=D0=B0 - =D0=A2=D0=B5=D0=BB=D1=8C-=D0=90=D0=\n=B2=D0=B8=D0=B2, some-889, 15.03.2018, =D1=8D=D0=BA=D0=BE=D0=BD=D0=BE=D0=BC=\n: (15 =D0=B2=D0=B7=D1=80.)\n\n- =D0=A2=D0=B5=D0=BB=D1=8C-=D0=90=D0=B2=D0=B8=D0=B2 - =D0=9C=D0=BE=D1=81=D0=\n=BA=D0=B2=D0=B0, some-890, 22.03.2018, =D1=8D=D0=BA=D0=BE=D0=BD=D0=BE=D0=BC=\n: (15 =D0=B2=D0=B7=D1=80.)\n--===============3693132879591888836==\nContent-Type: text/html; charset="utf-8"\nMIME-Version: 1.0\nContent-Transfer-Encoding: quoted-printable\n\n\n\n    <!DOCTYPE html PUBLIC \'-//W3C//DTD XHTML 1.0 Strict//EN\' \'http://www.=\nw3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\'>\n    <html xmlns=3D\'http://www.w3.org/1999/xhtml\' lang=3D\'ru-ru\'\n          xml:lang=3D\'en-us\'>\n    <head>\n        <meta content=3D"text/html; charset=3DUTF-8" http-equiv=3D"Conten=\nt-Type">\n       =20\n    </head>\n\n    <body id=3D\'body\'>\n   =20\n   =20\n       =20\n        <a href=3D"http://group.company.ru/ru/order/28922/process/">\n           =20\n            =D0=9D=D0=BE=D0=B2=D1=8B=D0=B9 =D0=B7=D0=B0=D0=BA=D0=B0=D0=B7=\n =E2=84=9628922\n        </a>\n\n    </body>\n    </html>\n\n\n--===============3693132879591888836==--\n',
        ),
        ],
    from_values=EmailAddress(name='', email='i.kor@company.ru'),
    to_values=(EmailAddress(name='Jessica Schmidt', email='jessica.schmidt@uni.de'), EmailAddress(name='Rabea.Bartölke@uni.de', email='я你Rabea.Bartölke@uni.de')),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)