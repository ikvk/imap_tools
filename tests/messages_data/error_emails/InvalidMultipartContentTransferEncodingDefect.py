import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='TTT: 1/20.1.UFA Depart',
    from_='bit@ufo.ru',
    to=('aaa@u6.ru', 'Serg@ufo.ru', 'isg@ggg.ru'),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2021, 4, 20, 12, 31, 24, tzinfo=datetime.timezone(datetime.timedelta(seconds=18000))),
    date_str='Tue, 20 Apr 2021 12:31:24 +0500',
    text='MVT\r\nU68925/20.VQBCE.UFA\r\nAD0706/0729 EA1029 LBD\r\nDL/0126\r\n',
    html='',
    headers={'date': ('Tue, 20 Apr 2021 12:31:24 +0500',), 'from': ('<bit@ufo.ru>',), 'subject': ('TTT: 1/20.1.UFA Depart',), 'mime-version': ('1.0',), 'message-id': ('<2104200731.1@ufo.ru>',), 'content-transfer-encoding': ('Base64',), 'to': ('<aaa@u6.ru>, <Serg@ufo.ru>, <isg@ggg.ru>',), 'content-type': ('multipart/mixed; charset="utf-8";\r\n\tboundary="96b0f72f_a01e_44f0_8595_352ca3ba6fd4"',)},
    attachments=[],
    from_values=EmailAddress(name='', email='bit@ufo.ru'),
    to_values=(EmailAddress(name='', email='aaa@u6.ru'), EmailAddress(name='', email='Serg@ufo.ru'), EmailAddress(name='', email='isg@ggg.ru')),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)