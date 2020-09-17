import datetime

"""
attachment_2_base64.eml
    Непонятно почему get_content_type не может получить content-type, в файле он есть
    Из за этого 2е вложение воспринимается как msg.text, хотя в файле его нет
    Возможно это из за наличия дефекта MissingHeaderBodySeparatorDefect
    ...\python\Python36-32\Lib\email\message.py 
    def get_content_type(self): 
        ...
        value = self.get('content-type', missing) -> None -> return self.get_default_type() -> text/plain
"""

MESSAGE_ATTRIBUTES = {

    # ===
    'simple': dict(
        subject='Соберите всю почту в этот ящик',
        from_='hello@yandex.ru',
        to=(),
        cc=(),
        bcc=(),
        reply_to=('foma@company.ru', 'petr@company.ru'),
        date=datetime.datetime(1900, 1, 1, 0, 0),
        date_str='',
        text='',
        html="""<html><head><meta http-equiv="content-type" content="text/html; charset=UTF-8"></head><body bgcolor="#ffffff" text="#000000"><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Соберите письма из других почтовых ящиков в Яндекс.Почте</title><font color="#000000" face="Arial"> Здравствуйте!<br><br> Если у Вас уже есть почтовые ящики, куда приходят письма, Вам будет удобнее хранить и читать все письма в одном ящике.<br><br><table cellpadding="0" cellspacing="0"><tbody><tr><td valign="top">
<a href="https://mail.yandex.ru/neo2/#setup/collectors"><img src="cid:collector.jpg@parts.yandex.ru" alt="Сборщик писем" width="135" border="0" height="100"></a>
</td><td valign="top"> <font color="#000000" face="Arial"> В Яндекс.Почту можно скопировать всю переписку и адреса собеседников из ваших старых ящиков. С ящиками ничего не случится – они продолжат работать и принимать письма, а на новый адрес в Яндекс.Почте будут приходить копии этих писем.<br><br>Чтобы собрать всю почту и адреса в один ящик —
<a href="https://mail.yandex.ru/neo2/#setup/collectors">
настройте сбор почты</a>. Для этого введите адрес ящика и пароль от него.<br><br>
<a href="https://mail.yandex.ru/neo2/#setup/collectors">
<font size="5">Настроить сбор почты</font></a></font></td></tr></tbody></table></font>
</body></html>""",
        headers={'MIME-Version': ('1.0',), 'From': ('=?utf-8?b?0K/QvdC00LXQutGB?= <hello@yandex.ru>',),
                 'Content-Type': ('multipart/related; boundary="===============1696383123=="',), 'Reply-To': (
                '=?UTF-8?B?0L/RgNC40LLQtdGC?= <foma@company.ru>,\r\n =?UTF-8?B?0L/QvtC60LA=?= <petr@company.ru>',),
                 'Message-Id': ('<20110815165837.A26162B2802A@yaback1.mail.yandex.net>',), 'Subject': (
                '=?utf-8?b?0KHQvtCx0LXRgNC40YLQtSDQstGB0Y4g0L/QvtGH0YLRgyDQsiDRjdGC0L4=?=\r\n =?utf-8?b?0YIg0Y/RidC40Lo=?=',)},
        attachments=[
            dict(
                filename='collector.jpg',
                content_id='collector.jpg@parts.yandex.ru',
                content_disposition='attachment',
                content_type='image/jpeg',
                payload=b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x02\x00\x00d\x00d\x00\x00\xff\xec\x00\x11Ducky\x00\x01\x00\x04\x00\x00\x00F\x00\x00\xff\xee\x00\x0eAdobe\x00d\xc0\x00\x00\x00\x01\xff\xdb\x00\x84\x00\x04\x03\x03\x03\x03\x03\x04\x03\x03\x04\x06\x04\x03\x04\x06\x07\x05\x04\x04\x05\x07\x08\x06\x06\x07\x06\x06\x08\n\x08\t\t\t\t\x08\n\n\x0c\x0c\x0c\x0c\x0c\n\x0c\x0c\r\r\x0c\x0c\x11\x11\x11\x11\x11\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x01\x04\x05\x05\x08\x07\x08\x0f\n\n\x0f\x14\x0e\x0e\x0e\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\xff\xc0\x00\x11\x08\x00d\x00\x87\x03\x01\x11\x00\x02\x11\x01\x03\x11\x01\xff\xc4\x00\xba\x00\x00\x01\x04\x03\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x04\x05\x06\x01\x02\x08\x07\t\x01\x00\x01\x05\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05\x06\x07\x10\x00\x01\x03\x03\x02\x02\x05\t\x01\n\x0b\t\x00\x00\x00\x00\x01\x02\x03\x04\x00\x11\x05\x12\x06!1AQ"\x13\x07aq\x81\x91\xa12\x14\x15\x08\xb1\xd1Bbr\x92\xa2#3s\xd3\xc1\xe1\x82\xb2\xc2CSc\xb3\xc3\x16R\xd2\x83\x93$D%E\x18\x11\x00\x02\x01\x02\x01\x08\x06\x06\n\x02\x03\x01\x00\x00\x00\x00\x00\x01\x02\x11\x03\x04!1AQ\x91\x12R\x05aq\x81\xa1\xb12\xf0\xc1\xd1"\x13\x15\xe1Bbr\x82\xb2\xc23\x06\x16#$\xa2s4\x14\xff\xda\x00\x0c\x03\x01\x00\x02\x11\x03\x11\x00?\x00\xef\xea\x00(\x00\xa0\r\x1cy\xa6\x8biuiB\x9dV\x86\xc2\x88\x1a\x95bl:\xcd\x81\xa5\xa0\xa97\x98\xde\x90@\xa0\r\\Z\x1aB\x9cp\x84\xb6\x80T\xa5\x1e@\x0e$\xd2\xa4\xdb\xa2\x11\xba*\xb3)RV\x90\xa4\x9b\xa5B\xe0\x8eD\x1aF\xa8*fh\x00\xa0\x04b\xca\x8f5\x84I\x8a\xe0u\x85\xdfC\x89\xe4lH>\xa2)\x13O0\xe9A\xc5\xd1\xaa1jQ\xa1@\x05\x00\x14\x00P\x01@\x05\x00\x14\x00P\x04V\xe2%\xbcp\x94\x13\x7f\x84~<\x85\x1e\xa6\xday\x05\xc5z\x11\xa8\xd3\xe1\x9c\x9e\xcf\x9a\x9a\xd3]\xc4\xad0\x80(\x01\xbc\xe4\x07aIm^\xea\xdaZM\xb9\xd8\xa4\x8a\x92\xdb\xa4\x93\xe9\x19qV-t\x1ac\x15\xab\x1b\rW\xb9,6o\xe7H\xa7^T\x9c\xba\xd8\xdb.\xb0\x8fR\x1d\xd4$\xa6\t\xb0\'\xab\x8f\n\x00\x8f\xc1B\xf9v\x1e\x1424\xad\xb6\x93\xacZ\xdd\xb5v\x95\xc3\xceM2\n\x89"{\xf3\xdf\xb8\xe5\xd2H\xd3\xc8\x02\x80\n\x00\x87\xce\xe7Q\x89T(l\xa0=\x95\xc9\xbc#\xc1\x8f\xd6x\x15\xb8\xabq\xd0\xda{J\xb7E2R\xa7[,Y\xb3\xbfV\xfc\xb1U~\x9d$\xc5<\xae\x14\x00P\x01@\x05\x00#.:e\xc5~*\xfd\xc7\xdbSJ\xbf\x11e\x82\x0f\xdbJ\x9d\x18\xe8\xca\x8d0\x8c\xa3\xdd\x84-IS\xe8\x03\xbe\xd2og\x08\xd4G\x93\x9d#\x11\xb5\\\x82\xa1@\xf27\xb5\x02\x1a\xb8\x9dhR/m@\x8b\xf9\xc5\xa9S\xa3\x11\xaa\xa1\x9e\x19D\xe2\xe1j\x1aO\xc3\xb5py\x83\xa7\xf8\xaak\xff\x00\xb9.\xb6Eg\xc9\x1e\xa4>J\x92\xb4\xa5hPR\x14\x01J\x81\xb8 \xf2 \xd4\x04\xc6h\x027!\x9b\x81\x8fBT\xb7C\x8b2\x11\x0c4\xd1\nY}\xc1\xa8#\x98\xb1\t:\xcd\xfa)R\xadi\xa0M\xe4Be\xfcE\xdb\xb8_\x8a2\xd6\xe2\xbe\x11hC\xa1\xa0\x16\xad+\x17\xd7k\xdfM\xfb>zktM\xe8\x89f6%(\xefh\xf6\x13\x839\x88\x0f\xe3\xa3.k(\x97\x96B\x9c\xc6\xc6R\xd2\x1d}\x08Gx\xa2\x84\xde\xea\tO\x15[\x95&\xf2\xdaD\xa1&\x9bK"\xce=\xefS\xdfw\x1cu\xe9\xd7\xe4\xb5\xedN\x18y\xa7\x87\xb9\x07w\xa6\xea\xdc\x1b\xd5\xd2\xbf\x96\xc3Y\xc4aR\x7fW\xdd\xa0\x85:\xb1\xc4\xf16O\xac\xfa*Z{\xf2r\xecF\xde:\x1f\xfc\xf6akK\xf7\xa5\xea=8\x13s\xd4*\xd9\x88f\x80!wz3k\xdb\x19_\xf4\xd4\x9f\x85\xcf":\xdd\xc7\xbcP\x97\x07~\xd0\xd6\x94\x94\xa8(\x10\xbd:\x0f\x0e\x9a\x8e\xe6\xf6\xeb\xdd\xceZ\xc2\xbbj\xec~"\xack\x97\xa8\xe3\x98\xdfW\xbb\xe6NS\x0e$3\x11\x88\xcc\xba\x88Y\x946\xd9\xd0\xea%8\x96\x83\xe0(\xa8\xa1m\x93~\n\xd2zEd\xc3\x1b7(\xd71\xd9_\xe4xxZ\x9b\x8dj\xb3t{Q\xe9\xdbk\xc4\xad\xdb\x1f%\xb80\xb2\xa78\xe9aa\xe8j\x7f\xf4\x8bB$%F\xc0\xaa\xe6\xc1hU\xbc\xf5\xabg\xcd4\xf4:\xf63\xcfp\xca\xae\xe2\x7fU\xa6\xba\x99+\x8c\xf1Wr\xc8rlW\x14\x15(b\x1c1\xdf\xe0\x00\x96\xdfx\x03\x85\x16)\xd5q\xd5\xc6\x96M\xa6\xfa\x8b\x96\xd2mW5QOk\xc5\xfd\xc3\x07\x1a\xeey\xe5\xad\xd7\x8c\\n]\xf5\x83`\xa2\x85\x14>\x9b\x1e\x82\x94\x94\x9f=.=|+\xb77s-\xd6\xbbL\x1f\x8b%\tKJ\xdd\xf1\xa3\xf0%7&\xf4\xccG\xcbl\xfc\x8e6S\xec\xc7\xc9Ka\xe2\xd0Q\xba\xd9\x92\xd3\xc9\x01V\xe7\xd9#\x85GZ\xc6\x0f\xa7\xdau\x16\x12q\x9eO\xa8\xfcQ=\xb5<S\xc9\xc5\x89!\xb9c\xe2\x94\xdc\xf7T5(\x85)\x0bzBJ|\x80\x06\xc5\xbc\xb5w\x10\xa9%MQ\xf01\xad\xb7O\xc4\xfcY\x19\x1b\xc4\xcd\xcd\x9a\xc3\xee\x07e\xbe\x96\xa1\x98\x12KL4\x84\xa5(Iiv\x00\x81~\xcd\xb9\xde\xb3\xed]w,\xcao>R~O\'{vR\xe3K\xb3x\xa9m}\xf1\xb8\xb1R\xa4dQ9\xd7\\\x8f(\xc2i.\xa8\xa9\xa1\x1e\x14&\xd3\xdd\xe9\xbd\xb4\x82\x9e]|j|\x14w\xee4\xf3o%\xdc\x8dnn\xd4-\xdbk?\xc3r}nR~\xc2\xdf\x91\xf1\'s\xb1\x92\xc7\xb2\xcc\xa0&\xe5#\x85Kx$]\x01\x94\x85\x90\x81\xc8\\\xac\x03aL\xc5\xc9\xc5%\x1d2*\xc2)\xc5WSc=\xb3&fGs\xc3rK\xcbt\x06\xa7\xe5\x1c%D\xdd\xe7\xddRB\xfa\xb5Y\x00y\xabR\xcf\xbb\x85\xb8\xf8\xa7\x15\xe2\xcc\x14\xab\x88\x87B\x9c\xbc\x11\x13>k\xf2\xb1;\xb9\xd7\x15uK\xc8\xb7\x05\xa5~\x0cf\x9bM\xaf\xe4R\xcdd\xdf\xfd\xb9\xf4\xe4\xf5\x1d-\xbc\xcb\xa2>,n\xac\xd4\xbcw\xcb\xf7c/(\xe6\xb1\x902\xcc\xc0\x92\xa5\x15\x16\xa1kDV\x1aJI\xb0\x1a\x92T:kNxx\xbcM\xabif\x8cS\xed\xa5L\xeb8\x99\xc7\x05zM\xe4r\xc9\xd9_ar\xcfo\xdd\xd8\xcch\x10Q84\xf3\xf8U"{\x9aR\xa5)\xe7Kl6\xe6\xa2.\x15\xa8\xad\\*\x966I\\\x92\x86l\xb4\xdbD3\r)F\xe47\xb2\xd25\x97Nb\x9b\xf4\xdb\xe2~\xe7\x91+#\x83t7+h\xc0t\xc5\xc60\xd3Hm\xe2\xe3\xaf9\xa5z\xc5\xae\xa7\t\xd4\xadF\xddUK\x04\xdc\x9c\xa2\xbc\xb1:\xfeob2P\x9b\xc9r\xe5[\xd4\x92H\xebT\x8b\x0bzO\x9c\xd5\xf3\x93\x0e\x9a\x00\xcd\x00|\xc0\xf1\xb3j/hx\xb7\xb9\xf6\xebh\rE\x9a\xb7\xdc\x80\x10,\x90\x99\t\xf8\x96\x02\x7f\x16\xe1>\x8a\xe6\xef\xc7rO\xa1\x9e\xa1\x81\xbd\xf1\xad\xc5\xf1\xc2\x9f\x89d\xf1G\xb9\xed\xac\xb229\x9c\x0ey?\xaa\xdc8\x86]_\xedP\x1bp\x8fF\xa7+r\xd3\xad\xc4\xf8\xa3\xe0y\x8c\xa1\xf0\xf1\x92\x87\x14d\xb62\xc9\x8fe\xb6\xf7T8\xeb\xf7\x1f\x12\xa3(z\x96?\x9cjI\xf9\x97j\x1d\x17\x93a@\xc9\xb5m\x99%\xabv\x86\x0etey\x15\x12J\xd3\xec\xa7s\x1c\xb2o]\xb8>\xe3\x12\xea\xa3\xba\xba_\xe7~\xd2\xe3?\xf4\x91\xbc1Z\xad\xdb8\xbbz\x19Q\xa8c\xe4\x87\xa6\xb3\xa7\xb1\xe5\x9f\xdc~1\x17\x8e\x96\xbe]9\xc2;_\x1a\xfa\x90G\x03`f\xab\xed5{\x14\xfd\xe5\xd5\x1f\xcabA\xd2+\xefK\xd65\xc3\xe8F\xd6\xcf\x84\xf0\xd3\x8fu\xb1\xe7]\xd1\xfd*\xc8\xc2\x7f\xe5\xeb\xaf\x89?\xf1\xff\x00\xdb\x83\xfbU\xf1er1\xbe=\xf7\x12x\xbb\',\xeaI\xe4u\xbe\x18Mi\xf2\xcf=~\xd4\x9e\xca\x9a|\xf9\xe4Q\xd5n\xda\xda\x97\xb4\x9c\xcb-\t\xdd\xa8O\xf5x\xf8\x04\x8e\xae\xd2\xd2?\xcb\xaa\x98\x8c\xb3\xb6\xbbFV\x91}\x08\xb7\xec\xd8\xe5\x9c\x9eE\xd5\x02\x0c\x1cdX\xda\xbf\r\xc4\x05\x91\xe7\xed\xd6\xbf\x97\x07mqJOfC\x9f\xc3\xaa\xdeo\x86\x11[[eD\xbdm\xb3\r\xf5\x1e\xcc\xdc\x94\xd9\xeb\xf2\xa4Iq@\xfeKB\xb3\x1cw\xf7c\xc54tS\x96\xe4&\xf5%\xdc\x86\xf9\x08\xcbS8\x9cA\x1d\xb7\xbeY\x05I\x1cx\x00f=\xedX\xbdm\xd8\x92x\xcb\x974A>\xe5\x90\xc6\xbb\x1a`\xad[\xe3\x97\x8b^\xc6#\xe2\xa6k\xe5x\xed\xc5\x92B\xac\xb6B`\xc4\xfcf\x1b\x08H\x1f\xf1d~msw\xe7L\xbe\x99>\x96kr\xfb_\x1b\x11Mm/[-_J\xbbHC\xc2\xc2\x94\xe2=\xedy\x07n.9w,\x03\xe5\xe0\xa5\x8f5I\x81\x86\xe5\x8a\xe9\x91\xbb\xce\xefV\xf4\x92\xfa\xb4\x82\xec\xcb.\xfc\x87Q_\x8d\xaa\xd1\xcb\x99\xa0\x02\x808\xb7\xeb\x87m*\x16Wlo\xd8\xe9\xe0Ra\xc9 }\xf4e\xf7\x88$\xfe\x12\\P\xfeMd\xe3a\xef\'\xadP\xec\xf9\x15\xff\x00\xf15\xa6\x12R\xecy\xfc;\xca\xdf\x86\xd3[^\xd3\xdb\xee\x95]X\x1c\xb3\xf8\xe5\x9e\xa8\xf2\x16T\xd7\xa3D\x84\xfa\xa9\xf8i\xd6\x10\x96\xa7M\xb9\x0c.\x7fk\xe0c\xa3%\x9byl\x96C\xd5e\xa1,n\x1c,\x9bX*j\x02\xad\xd0^mI\xfbmZ\x17U)\xd0\xcc\xe6\xa8\xda\xeb*y\xd8\x89g\x1f\x98\x86mf\xce\xe0\x8d\xa7\xc8\xbf\xd3\x0f\xe7R\xe3\xb2\xc6\x0f]\xaf\xcb#\x17\x11\xfb\x97:\x9f\xe9d\xd3\xba\x1ec\xc2\x80y9\xf2\xcfdu\x13PG\xc9\x0fM\x0c\xe9ly\'\xf7?TE\x94\xda[\xc2Np\x1fzT\xb0\x0f\x99\x12\x7f\xde\xab\x98\xc7\x97\xb1~S\x05\xba[\xafL\xbfP\x9e1\xb4\xb7\xb4r\xca\xb0\xed";7?\xdeJl\x1a\xcc\xc2\xff\x00\xe5\x8f\xa6\x92\xe7#\xc9b\x1f\x89\xff\x00\xc6Eg\x08\xdf\x7f\x8f\xc54\xaerR\xd2\xadn\x07\xe2\xe7\x97=\xa0V\x8f.\xc9\n\xfd\x99\xbd\xb5\xf6\x9a<\xf7.&Q\xd5(Gb^\xc2FY\x12w6p\xa7\x8a\xbb\xb8\xf1\x91\xe7^\xb2G\xadb\xa9\xdf\xfd\xe5\xd1\x16W\xc4:Z\x97\xa6\x83\xd0\xe0:\x98XM\xd3\x96 \x04\xae[\xe9J\x8fJ"$ \x7f\x86kc\x13\xee\xc2\xd4uB\xbb[ff\x125\x9c\xde\xb9SbH\xa0\xe4c)\x18\x1d\xb9\x8aM\xfb\xd3\x01\x94*\xdf\xdaJJ\x12}\xaf\x1a\xaf\x85U\xbfo\xec\xefKb/\xe3\xa5\xfe\xbc\xfe\xd3\xa6\xd7BN9nV\xf8\x88\xb5\x80#A\x13\xb2Nu\x046\xae\xe1\xbf\xcdl\xd5\x8c;\xdd\xb1v|M.\xfa\xbf\x02\x0c_\xefZ\x86\x88F\xbd\xdfI\xe5^*\xbf#(\xde\xdc\xdbm\\\xcc\xcdJ\x13\x1fG3w\x16]\x00\xff\x00)\xe6\xff\x00&\xb9\xacKmn\xe9\x95\x16\xdc\xac\xe9\xff\x00\x8e\xc1F\xb7\xa5\x9a\x11r;/\xc2\xcc\x0bX=\xb2\xd2\x1bH\tXKM~\xc62{\xa4\xfa\xc8R\xbd5\xb4\xd6\xeaQZ\x11\x91\x8a\xb8\xe5,\xb9\xf3\xbe\xb7\x95\x97q\xd7\xd7\xe9\xa6\x94\xcc\xd0\x01@\x1eA\xf55\xb4\x93\xbb\xbc\x1e\xce\xb2\x96\xcb\x92\xb1iNN8\x02\xe4\x18\xf7\x0e\x1fCj]T\xc5\xc6\xb6\xeb\xab)\xb5\xc9\xee\xeeb\x14^i\xa7\x1d\xb9\xbb\xe8q\x8f\x84\x19\x17d\xe07\x06/W\xe9\x8cX\xd9\x06\x87O}\rJ\x8e\xe1\xf3\xf6Z\xaa\x18\x7f,\xe3\xdb\xeb-\xff\x00\'\xb6\xe7f\x174\xd2\x9d\xb1=\xc7-\x94\x0fc\xe0\xe4\x9bW\xb8\xe49@\xf9\x03\x88Q\xf6V\xc5\xdc\xb1o\xb4\xc1r\xde\x92|I=\xa8a\xbb\xa4\x04\xe4\xf3\xed\x13`\xa9rT<\xd2\xe1\x03\xf6\x8a~+-\xabo\xa2\xe2\xf5\x98\x98\x85\xfeW\xd3\x1f\xd1\xf4\x0e>1)\x8b\xe1"uX\x8f\x81?\x93\x19uR\x1eHzhgE\x87\xfd\xa9\xfd\xcf\xd5\x11\xcc\x99\xa1\xad\xb8\xf9*\xb9[\xd2\xb4\xfe1\xd4?\xa5Vq\xcf?\xdd\xfd&\r\xdc\x96\x9f\xe3\xf5\x98n[L\xec,\x9b\xcbW\xfd\xccP\x90O\xdf!e\xc3\xecER\xb3\x93\r\x03W\x92C\xfcV\xd6\xb4\xfb\xf2z\xc8}\xbc\xf2\x03\xd86\n\xac\x19j\x00P\xe9\xbbq\xdcx\xfbMh\xe0\xd5,\xfe\x15\xde\xd1/4\x96\xfe2]7%\xddQ\xde\xdf\x90\xdc\xac\xfc\x97Tn\xdb\xf9v\x9b\xe3\xc0\x94\xc7Kd\x8f\xcc5B\xe6[\xd3\xeaK\xbc\x8f\x15\xe5\xa6\xb9z\xcb^K"\x88\xfe\x16\xca:\xec\xf4\xd4:\xe7\x0ez\xe6\x15\x91\x7f?z+_\x1c\xff\x00\xca\xd7\nKbE>^\xbd\xd8\xbdm\xcb\xbd\xb2\'\'!\xaf\xf5<&u\x0e\xe6\x1fv\xabt\x04DB\xdc\xff\x00)5\x1d\x8c\x92\x9c\xb8m\xfefO\x8a[\xca\xd48\xa4\xbd\xa3\\b\x82\xd9\xdc\x92\xb5v\xfb\x88xVW\xf8o\xd8\xb9\xeduT\xfb\xbe\xe6\x16\x11\xe2m\xfa\x8a\xb7\xde\xfd\xfb\xb2]\x10E?\x03\x10\xee\xff\x00\x1b\xee\xc2{\xc8\xb8&P\xdct\x9fw\xbeY\x01\xb1\xebZ=U\x87f?\x13\x10\xb5EW\xd3\xb0\xed\xac\xa5g\x01\xff\x00d\xa9\xf8c\x95\xf8\x1d\xcb\x12* \xc1b\x1b_\xab\x8e\xd2ZO\x99\t\x02\xfe\xca\xd3n\xae\xa7))oI\xbdb\xe9\xbd\xbb\\\xeeyu_\x87\xb2\x90h\x1a\x00\xcd\x003\xcb"#\x98\xb9\xcd\xcfo\xbe\x82\xb8\xee\xa6K?\xed\xb4Pu\xa7\xa3\x98\xb8\xa4\x96l\xa3\xed\xb6\xa4\x9a\xcfS\xe7&\xd9\xd9\x19-\xaf\x9e\x91\x92\x8d\x94\x8c\xbck\xff\x00\x14\x84\xc7(s\xbc\x0cK\t!$\xf2\xbaV\x84\xab\xd7\\\xa5\xaecn\xdc\xebG\x9a\x87w\x8d\xc3O\x13i\xdb\xc8\xbd\xea\xed\xce[\x16\xac\x81\xc2\xa7\x13\xf3\x06C\x89d\xb0\x9749k\x02J\r\xb9\xf0\x06\xd5ms\x9bJ\n;\xaf"\xa6\x83\n\x1c\x8e\xeca\x18\xef*\xc5SOa\xbeq\xe9\xb9\x89\xd3$\xb79\xb6\xcc\xc0\xce\xa4\xad\xb5\xf0[lwJ7\x1dg\x95:|\xee\xd4\xad\xc6;\xaf\xddm\xe8\xd2\xa8V\xbb\xfcv\xf4\xa7\xbd\xbd\x1c\xd4\xd3\xd3\xed\x12uy@v\x88\x13\x1b\xb6\xd9KI\x90\x9d\x0b\xfd)i\nn\xe8\xe3\xc2\xf7\xe9\xa8c\xce-(\xc5n\xbc\x9dF\x8c9E\xd8\xc1\xc7yeT\xd3\xad?P\xb2\xe6\xe4\x1d\xc77\x00\xbe\x9dM\xb8\xe3\x8bV\x85i!kI\xb0\xf4\x0bS\xb1\x1c\xea\xdd\xc4\xfd\xd7\x95SF\xaa\x19\xf7?\x8e\xdd\x9c\x1cT\xa3\x96\xba\xf4\x98\x97/!#k;\x80C\x9a_z@\x91\xdf\x94\x92\x8b\x04-\x16#\x9d\xfbU\x17\xcd\xed|%\n<\x8b\xa0\xd2\xc0rk\x98e\x04\xda{\xbdz\xd3\xf5\tCVV,\xe4J*\nm\xb3p\x94\xa4\xde\xc9\x8f\xdc\x0eg\xd3V\xad\xf3\xeb1\x8d7^\x8dZ\x08\xa5\xc9.\xca\xee\xfb\x92\xce\xde\x9d!\x88N_\x1e\xf2\x1e[\x89Z\xc2\xe6?p\x08\xbb\xb2\x90\xe2\x1b<O\xdek\xe3U\xe3\xce\xac\xa9\xb98\xbc\xad=\x82\\\xe4wf\x97\xbd\x1d:\xc9\xec\xd6O!\x93\xc2B\xc2\xc7\xb3H\x8c\xe4u8\xa5\x90u7\x1c\xb4H\x16<\xc8o\xa6\xa6\xb9\xcf\xedNN[\xb2\xca\xfa\x06Z\xe47m\xc5-\xe8\xe4T\xd3\xa8b\xb4\xe5\x9f\xc9\xbb8\xc8i!\xc6\x96\xd0I\n$\x17BR\xa3\xc3\xc9\xab\xd7G\xcf\xec\xa8\xcd(\xcb\xdf\xa6\xad\x04\xb3\xe4\x97%v\x13\xdeT\x82\xe9\x14m\xac\xebp\x8cF\xe53\xad\xd9\xce\xe4\x1fr\xcb\x01JRV\x1bH\x1f\x83\xa8z\xa9\xd7\xff\x00\x90Z\xb8\xa2\x94e\xee\xaah*\xc7\x90]_Z>m\xe7\x9c\x9a\xf0\x1b\x0e\xf6\xcf\xdej\x9f\xb8\xe4\xa2k\xd9\x89\xc9:\xe2\xa5CJ\xdd%\x0c\xa4\x85\x91\xc1+X&\xddT\xdc\x173\xb4\xe6\xe2\x93\xac\xcdLf\x1a\xe7\xc0J\xaa\x90\x8f\xd3&vq\xb5t\x07\x1c\x04\xf0\xe0/\xe4\xa0\x0cj7)\xd2x[\x8f\x0bq\xf4\xd0)\xb5\x02\r2\x8d\x97\xb1\x93Y\x06\xc5\xc6\x1d@\'\xa3R\x08\xa4y\x87A\xd2H\xe0%\xe5]\x00\r7\xd0\x02}B\xd5\xe6S\xf35\xd2z\xacs\t+.\xe7\xdfi@\xe9&\xdfv\xa2\xca;!\x81\x96"\xc0\xad>\xb1\xf6\xd1A2\x1b|\xdd)$w\x88\x1d<\xc5\x14b:\x08\xaf?\x1d\x0e%\x85Jm\x0e\xae\xeaCZ\x92\x14\xa0\x9ed\x03\xc4\xda\x8d\xc9g\xa0o,\xc6\x9f=\x8a\xea\xdce2\xd0\xa7[\xb7x\x84\xa8\x12\x82x\x8b\x8e\x8b\xd28Ih\x1c\xa5\x16g\xe6\xed&\xff\x00\xa5\x04\xf9TM&\xeb`\xda59\xb6\xff\x00\xb6O\x0e\x17\x17\xa4\xdc`\x9a7Ns\xa9w\xbf.\xc9\xfb\x94n\xb1E[\xcc\xbf~\xc9U\xc7+\nZ\x06A\xcbyyJ\xe0\n\xfc\xd4\xe4\x86:\x16\xbf\x0f\xe4I\x99\xbdv\xf3.)A*\xc8\xc4$\x9e]\x97R\xaf\xe0\xadN\\\xbf\xd8\x8fY\x9f\x8fiX\x9fS;g\x9d\xc7Mw\xe7\x9c\x00\x00r\x1dg\xd6o@\x19\xa0\x02\x80\x13\x90\xda\x9d\x8e\xebI\xf7\x96\x85$_\x95\xc8\xb5\x02\xac\xe7\xcew#-\xbe\xc2\xcd\xd6\x07hp\x1ck\xcc\xafd\x9b\xebg\xa8\xc3,P\xcd\xd8\xee{\xc9A#\xa3\x95\xbe\xdab\x92$\xa0\xd1\xc6dp\xba~\xcf\xbbORA\xba$\x19wW\xba\x07\x94\xda\x9d\xbc\x86\xd0\xabnD>\xden\x1c\xd6\xd0\x14\xec\x18\xae\xcb\tO5!\xb7P\x1cH\xb0\xe9AU]\xb0\xd3\x83Z\xdd\n\xd7*\xa4\x9a\xd0\x86\x10\x9c\xc9c]\xc8\xccKZ\xe5\xc8^=\xd7\x91mJ\xff\x00\xabZ\xae\x808q\t!"\xa4\x9a\x8c\xe8\xb4-\xee\xe1\xb1\x94\xa3W\xd5\xdeH\xaf5\x98rS\x90\x98\x8a\xe3n*J\xdal|8u\xf44\xd3(p\x82\xde\xa0\n\x89W_*\x85Y\x86v\xf4k\xc9\x9fX\xf7zo6\xbd^\xa2{\x1a\xac\x94\x88,;:)\x8f,\x82\x1diCM\x94\t\x17\x02\xe6\xd7\x1cj\x9d\xc5\x18\xc9\xa4\xea\x8b\x10m\xc5U\x12H\x12\r\xbb \x0f)\xa8]5\x92\xe5\x1d\xa3\xe2Q\xc6\xc0\xf9\x01\xbdF\xdcGe\x17k\xe35\xdc%\x16\xeb&\x95J#Ze\xdf\xc2\xf4\xc8_\x88\x1bi$$\x7f\xe4c\x93et$\x95\x1f`\xad~V\xe2\xf1\x11\xa1\x95\xcc\x94\x96\x1eu\xd4w(\x1co]\xf1\xe7fh\x00\xe8\xa0\x02\x80\n\x00\xf9\xe18G\xef\xd4T\xe1+\xb9\xd4\x9b\xf4\x82k\xcb\xb1\x15\xf8\xb2\xebg\xac\xd9Kqu\x0cKm\xac( )`t\xa4^\xab\xd5\x92\xd1\t\xad\xa6\xc5\xae\xd2\x89\x1c=\xd3Bl\x1aF\x03\x08\xb8"17\xe5\xc0\xda\x96\xafX\xda#S\x8fes\x1b\x97\xf0ES\x1bmM!\xc1\xcc6\xb2\x14\xa1k\xdb\x89\x03\x9d9\\{\xb4\xaeA\xae\n\xb5\x13{\x17\x19\xf7\xddqX\xf2\xb7\x9eS+t\xdc\xdc\xaa)\xd4\xd1\xe0~\xf4\xff\x00\x1d9]\x92T\xaej\xf7\xe7\x11\xdb\x8b\xf4\xd4!3\x05\x1eJ\x9d\xef\xe1\x90\xeb\xcf|J\xdcC\x85\x0b\x0f\x04\x84k\x0bJ\x81I\xd24\xf04\xb1\xbd(\xe6z)\x98\x1d\xb8\xbd\x02\xf1\xa1*+M\xc7\x8a\xc6\x96ZN\x94\x80\xbb\xd8yI\xb95\x1c\xa7\xbc\xea\xc9c\x14\x95\x12\x1c\x06\xde\xb5\x96\x9b[\x91\xbdF\xd8\xea!V\xd9_+\x12I\xe3{S[\x17 \xf5\xa6\x1c\x1f\xd5\x92\x0f\x98Sj#\x92.\xde\x16\xc7y>!m\x93\xdd\x10>=\xbb\x9b\x82x!d\xfd\x95\xb5\xc9\x9dqQ\xed\xf029\xac\xbf\xd6\x9fW\xac\xed\x8a\xf4S\xcd\x82\x80\n\x00(\x00\xa0\x0f\x02\x95\xf4\xcf\x1d\xd7\x96\xe3y\xd1\xa1JQJU\x11:\x85\xc9<Oxo\xea\x15\xce]\xe4\x91\x9c\x9c\xb7\x9eW\xa8\xe9\xa1\xcfe\x14\x96\xe2\xda ~\x99\xdd\xb1\x03>\x80\x0f!\xf0\xc4}\x8b\x15\x17\xc8!\xc6\xf6\x0e\xf9\xfc\xb8;\xc4\xbf\xf9\x99\xe1\xff\x00\xbai^x\xea\xfd\xe57\xe4\x11\xe3{\x07\xff\x00`\x97\x02\xda&\xaf\xa6\xc9\xe9\xf72\xac\x13\xfb\x03\xfc.R|\x82<O`\xef\xec\x12\xe1[Y\xa9\xfap\xca\x11\xa7\xe6m[\xa6\xed\x1b\x7f\x89K\xf2\x08\xf1=\x82|\xfe\\+i\xaa\xbe\x9c2\x9alrM\x10:;\xa5[\xd4\x17G\xc8#\xc4\xf6\t\xf3\xe9p\xad\xa6\x87\xe9\xb3&x\x8c\x93\x02\xff\x00\xdc\x92}\xaeQ\xf2\x18\xf11\x7f\xb0K\x85m\x0f\xfek\xcb\x1eyV\x7f\xe4\x9f\xdeQ\xf2\x08q0\xfe\xc1.\x15\xb4Q\xbf\xa6\xac\x80\x1cr\xac\xfaYW\xef)~A\x0e&5\xf3\xf9p\xa1\xc3\x7fM\xf3Rx\xe5\x98\x03\xf6\n\xfd\xe5\x1f!\x87\x13\xd8\'\xcf\xa5\xc29G\xd3\xac\xbb\xf6\xb2\xcc[\xaf\xb8_\xef(\xfe\xbf\x0e&7\xe7\xb2\xe1\xef,\x9bO\xc1D\xed\xcc\xee?8\xeeQ/.\x03\x8au,\xb6\xc9N\xa5)\xb57\xc5Ef\xc3\xb5\xd5W0\x9c\xa2\x18{\x8ajU\xa1S\x13\xcd\xa5z\xdb\x83\x8d*z\xddn\x98a@\x05\x00\x14\x00P\x06\x0fE\x00f\x80\x0e4\x00P\x01@\x05\x00\x14\x00P\x01@\x05\x00\x14\x00P\x01@\x05\x00\x14\x01\xff\xd9'
            ),
        ],
        from_values={'email': 'hello@yandex.ru', 'name': 'Яндекс', 'full': 'Яндекс <hello@yandex.ru>'},
        to_values=(),
        cc_values=(),
        bcc_values=(),
        reply_to_values=({'email': 'foma@company.ru', 'full': 'привет <foma@company.ru>', 'name': 'привет'},
                         {'email': 'petr@company.ru', 'full': 'пока <petr@company.ru>', 'name': 'пока'}),
    ),

    # ===
    'attachment_8bit': dict(
        subject='S19 IZM A7-342',
        from_='k1@yandex.ru',
        to=('rasp@wat.aero',),
        cc=('aa@com.ru', 'mm@com.ru'),
        bcc=('hello@yandex-team.ru',),
        reply_to=(),
        date=datetime.datetime(2019, 2, 7, 13, 18, 20,
                               tzinfo=datetime.timezone(datetime.timedelta(hours=5, minutes=0))),
        date_str='Thu, 7 Feb 2019 13:18:20 +0500',
        text="""SCR

/
S19
07FEB
wat

-- 
отдел расписания
тел. (343) 072-00-00 (вн.18-59)
e-mail: e.sp@com.ru

""".replace('\n', '\r\n'),
        html="""<html>
  <head>

    <meta http-equiv="content-type" content="text/html; charset=windows-1251">
  </head>
  <body text="#000000" bgcolor="#FFFFFF">
    <p>SCR<br>
    </p>
    <div class="moz-forward-container">/<br>
      S19<br>
      07FEB<br>
      wat<br></div>
    <pre class="moz-signature" cols="72">-- 
отдел расписания
тел. (343) 072-00-00 (вн.18-59)
e-mail: <a class="moz-txt-link-abbreviated" href="mailto:e.sp@com.ru">e.sp@com.ru</a></pre>
  </body>
</html>
""".replace('\n', '\r\n'),
        headers={'To': ('=?UTF-8?B?0KLQrtCc0JXQndCs?= <rasp@wat.aero>',), 'MIME-Version': ('1.0',),
                 'X-Forwarded-Message-Id': ('<1333139463.20190207083243@com.ru>',),
                 'Date': ('Thu, 7 Feb 2019 13:18:20 +0500',), 'References': ('<1333139463.20190207083243@com.ru>',),
                 'Return-Path': ('e.sp@com.ru',), 'Received': (
                'from m101.com.ru (LHLO m101.com.ru) (92.233.222.111) by m101.com.ru\r\n with LMTP; Thu, 7 Feb 2019 13:18:22 +0500 (YEKT)',
                'from localhost (localhost [127.0.0.1])\r\n\tby m101.com.ru (Postfix) with ESMTP id 9A9181170B7;\r\n\tThu,  7 Feb 2019 13:18:22 +0500 (YEKT)',
                'from m101.com.ru ([127.0.0.1])\r\n\tby localhost (m101.com.ru [127.0.0.1]) (amavisd-new, port 10026)\r\n\twith ESMTP id Q3OLc4gNDjjO; Thu,  7 Feb 2019 13:18:22 +0500 (YEKT)',
                'from [192.168.104.100] (kom-420-1.hades.company [192.168.104.100])\r\n\tby m101.com.ru (Postfix) with ESMTPSA id DC7BB1170A1;\r\n\tThu,  7 Feb 2019 13:18:21 +0500 (YEKT)'),
                 'Cc': ('aa@com.ru, mm@com.ru',), 'Bcc': (
                '=?utf-8?b?0JrQvtC80LDQvdC00LAg0K/QvdC00LXQutGBLtCf0L7Rh9GC0Ys=?=\r\n\t<hello@yandex-team.ru>',),
                 'From': ('=?utf-8?B?0JrQsNGD0LrQuNC9INCS0LvQsNC00LjQvNC40YA=?= <k1@yandex.ru>',),
                 'Content-Type': ('multipart/mixed;\r\n boundary="------------FFFBFD561B1FF33B4E5E7050"',),
                 'Subject': ('S19 IZM A7-342',), 'X-Virus-Scanned': ('amavisd-new at m101.com.ru',),
                 'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0) Gecko/20100101\r\n Thunderbird/60.5.0',),
                 'Message-ID': ('<2ffd4cec-d312-60da-72f3-5b6e4406fddf@com.ru>',), 'Content-Language': ('ru',),
                 'In-Reply-To': ('<1333139463.20190207083243@com.ru>',)},
        attachments=[
            dict(
                filename='Message01.eml',
                content_id='',
                content_disposition='attachment',
                content_type='message/rfc822',
                payload=b'Return-Path: a.pl@com.ru\nReceived: from m101.com.ru (LHLO m101.com.ru) (92.233.222.111) by m101.com.ru\n with LMTP; Thu, 7 Feb 2019 08:29:46 +0500 (YEKT)\nReceived: from localhost (localhost [127.0.0.1])\n\tby m101.com.ru (Postfix) with ESMTP id 5C11A78A70;\n\tThu,  7 Feb 2019 08:29:46 +0500 (YEKT)\nX-Virus-Scanned: amavisd-new at m101.com.ru\nReceived: from m101.com.ru ([127.0.0.1])\n\tby localhost (m101.com.ru [127.0.0.1]) (amavisd-new, port 10026)\n\twith ESMTP id qPDszqYc1_Us; Thu,  7 Feb 2019 08:29:46 +0500 (YEKT)\nReceived: from [192.168.104.53] (kom-419-31.hades.company [192.168.104.53])\n\tby m101.com.ru (Postfix) with ESMTPSA id 29D6C78A67\n\tfor <a.nov@company.ru>; Thu,  7 Feb 2019 08:29:46 +0500 (YEKT)\nSubject: S19 IZM A7-342\nReferences: <4a598974-6731-c4f3-0efa-2f1e2b044f08@com.ru>\nTo: Alla Nov <a.nov@company.ru>\nFrom: =?utf-8?B?0JrQsNGD0LrQuNC9INCS0LvQsNC00LjQvNC40YA=?= <k1@yandex.ru>\nX-Forwarded-Message-Id: <4a598974-6731-c4f3-0efa-2f1e2b044f08@com.ru>\nMessage-ID: <09ccd226-f9e9-77e0-e456-3490e024d16e@com.ru>\nDate: Thu, 7 Feb 2019 08:29:45 +0500\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0) Gecko/20100101\n Thunderbird/60.4.0\nMIME-Version: 1.0\nIn-Reply-To: <4a598974-6731-c4f3-0efa-2f1e2b044f08@com.ru>\nContent-Type: multipart/alternative;\n boundary="------------CC10C5F7DB2594C21A5E2BDB"\nContent-Language: ru\n\n--------------CC10C5F7DB2594C21A5E2BDB\nContent-Type: text/plain; charset=utf-8; format=flowed\nContent-Transfer-Encoding: 8bit\n\n\xd0\x94\xd0\xbe\xd0\xb1\xd1\x80\xd1\x8b\xd0\xb9\xc2\xa0\xd0\xb4\xd0\xb5\xd0\xbd\xd1\x8c,\xc2\xa0\xd1\x83\xd0\xb2\xd0\xb0\xd0\xb6\xd0\xb0\xd0\xb5\xd0\xbc\xd1\x8b\xd0\xb5\xc2\xa0\xd0\xba\xd0\xbe\xd0\xbb\xd0\xbb\xd0\xb5\xd0\xb3\xd0\xb8!\n\n\n\n\n-------- \xd0\x9f\xd0\xb5\xd1\x80\xd0\xb5\xd0\xbd\xd0\xb0\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xbe\xd0\xb5 \xd1\x81\xd0\xbe\xd0\xbe\xd0\xb1\xd1\x89\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 --------\n\xd0\xa2\xd0\xb5\xd0\xbc\xd0\xb0: \t\xd0\x92\xd0\xb2\xd0\xbe\xd0\xb4 \xd1\x80\xd0\xb5\xd0\xb9\xd1\x81\xd0\xbe\xd0\xb2 \xd0\xa2\xd0\xae\xd0\x9c, \xd0\xa7\xd0\x9b\xd0\x91, \xd0\x9e\xd0\x9c\xd0\xa1 \xd0\xbd\xd0\xb0 \xd0\x9b\xd0\xb5\xd1\x82\xd0\xbe 2019\n\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0: \tFri, 7 Dec 2018 08:23:21 +0500\n\xd0\x9e\xd1\x82: \t\xd0\x9f\xd0\xbb\xd1\x91\xd1\x82\xd0\xba\xd0\xb8\xd0\xbd\xd0\xb0 <a.pl@com.ru>\n\xd0\x9a\xd0\xbe\xd0\xbc\xd1\x83: \t\xd0\x91\xd0\xb5\xd0\xbb\xd0\xbe\xd0\xb1\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4\xd0\xbe\xd0\xb2\xd0\xb0 \xd0\x9e.\xd0\x9d. <schedule@com.ru>\n\n\n\n\xd0\x94\xd0\xbe\xd0\xb1\xd1\x80\xd1\x8b\xd0\xb9\xc2\xa0\xd0\xb4\xd0\xb5\xd0\xbd\xd1\x8c,\xc2\xa0\xd1\x83\xd0\xb2\xd0\xb0\xd0\xb6\xd0\xb0\xd0\xb5\xd0\xbc\xd1\x8b\xd0\xb5\xc2\xa0\xd0\xba\xd0\xbe\xd0\xbb\xd0\xbb\xd0\xb5\xd0\xb3\xd0\xb8!\n\n\xd0\x9f\xd1\x80\xd0\xbe\xd1\x88\xd1\x83 \xd0\xb2\xd0\xb2\xd0\xb5\xd1\x81\xd1\x82\xd0\xb8 \xd1\x80\xd0\xb5\xd0\xb9\xd1\x81 \xd0\xbd\xd0\xb0 \xd0\xbf\xd0\xb5\xd1\x80\xd0\xb8\xd0\xbe\xd0\xb4 \xd0\xbb\xd0\xb5\xd1\x82\xd0\xbd\xd0\xb5\xd0\xb9 \xd0\xbd\xd0\xb0\xd0\xb2\xd0\xb8\xd0\xb3\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8\n\n*\xd0\x94\xd0\x9c\xd0\x94-\xd0\xa2\xd0\xae\xd0\x9c-\xd0\x94\xd0\x9c\xd0\x94 \xc2\xa0 \xd0\xa36-341/342*\xc2\xa0 \xd1\x82\xd0\xb8\xd0\xbf \xd0\x92\xd0\xa1 \xd0\x90320\n\n\xd0\x92\xd0\x92 \xd0\xb8\xd0\xb7 \xd0\x94\xd0\x9c\xd0\x94 23:00 LT. \xd0\x92\xd0\x92 \xd0\xb8\xd0\xb7 \xd0\xa2\xd0\xae\xd0\x9c 06:45 LT\n\n\xd0\xb8\xd1\x81\xd0\xba\xd0\xbb\xd1\x8e\xd1\x87\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xbf\xd0\xb5\xd1\x80\xd0\xb8\xd0\xbe\xd0\xb4 \xd1\x81 25/05/19 \xd0\xbf\xd0\xbe 13/10/19\n\n\xd0\x92\xd0\x92 \xd0\xb8\xd0\xb7 \xd0\x94\xd0\x9c\xd0\x94 \xd0\xb2 00:50 LT\n\n\xd0\x92\xd0\x92 \xd0\xb8\xd0\xb7 \xd0\xa2\xd0\xae\xd0\x9c \xd0\xbe\xd1\x81\xd1\x82\xd0\xb0\xd0\xb5\xd1\x82\xd1\x81\xd1\x8f \xd0\xb1\xd0\xb5\xd0\xb7 \xd0\xb8\xd0\xb7\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f\n\n----------------------------------------\n\n*\xd0\x94\xd0\x9c\xd0\x94-\xd0\x9e\xd0\x9c\xd0\xa1-\xd0\x94\xd0\x9c\xd0\x94 \xc2\xa0 \xd0\xa36-387/388*\xc2\xa0 \xd1\x82\xd0\xb8\xd0\xbf \xd0\x92\xd0\xa1 \xd0\x90321\n\n\xd0\x92\xd0\x92 \xd0\xb8\xd0\xb7 \xd0\x94\xd0\x9c\xd0\x94 \xd0\xb2 23:15. \xd0\x92\xd0\x92 \xd0\xb8\xd0\xb7 \xd0\x9e\xd0\x9c\xd0\xa1 06:30 LT\n\n----------------------------------------\n\n*\xd0\x94\xd0\x9c\xd0\x94-\xd0\xa7\xd0\x9b\xd0\x91-\xd0\x94\xd0\x9c\xd0\x94 \xc2\xa0 \xd0\xa36-610/609*\xc2\xa0 \xd1\x82\xd0\xb8\xd0\xbf \xd0\x92\xd0\xa1 \xd0\x90320\n\n\xd0\x92\xd0\x92 \xd0\xb8\xd0\xb7 \xd0\x94\xd0\x9c\xd0\x94 \xd0\xb2 23:30. \xd0\x92\xd0\x92 \xd0\xb8\xd0\xb7 \xd0\xa7\xd0\x9b\xd0\x91 06:40 LT\n\n\n\n--------------CC10C5F7DB2594C21A5E2BDB\nContent-Type: text/html; charset=utf-8\nContent-Transfer-Encoding: 8bit\n\n<html>\n  <head>\n\n    <meta http-equiv="content-type" content="text/html; charset=UTF-8">\n  </head>\n  <body smarttemplateinserted="true">\n    <div id="smartTemplate4-template">\xd0\x94\xd0\xbe\xd0\xb1\xd1\x80\xd1\x8b\xd0\xb9\xc2\xa0\xd0\xb4\xd0\xb5\xd0\xbd\xd1\x8c,\xc2\xa0\xd1\x83\xd0\xb2\xd0\xb0\xd0\xb6\xd0\xb0\xd0\xb5\xd0\xbc\xd1\x8b\xd0\xb5\xc2\xa0\xd0\xba\xd0\xbe\xd0\xbb\xd0\xbb\xd0\xb5\xd0\xb3\xd0\xb8!\n      <p>\xc2\xa0</p>\n    </div>\n    <br>\n    <div class="moz-forward-container"><br>\n      <br>\n      -------- \xd0\x9f\xd0\xb5\xd1\x80\xd0\xb5\xd0\xbd\xd0\xb0\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xbe\xd0\xb5 \xd1\x81\xd0\xbe\xd0\xbe\xd0\xb1\xd1\x89\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 --------\n      <table class="moz-email-headers-table" cellspacing="0"\n        cellpadding="0" border="0">\n        <tbody>\n          <tr>\n            <th valign="BASELINE" nowrap="nowrap" align="RIGHT">\xd0\xa2\xd0\xb5\xd0\xbc\xd0\xb0: </th>\n            <td>\xd0\x92\xd0\xb2\xd0\xbe\xd0\xb4 \xd1\x80\xd0\xb5\xd0\xb9\xd1\x81\xd0\xbe\xd0\xb2 \xd0\xa2\xd0\xae\xd0\x9c, \xd0\xa7\xd0\x9b\xd0\x91, \xd0\x9e\xd0\x9c\xd0\xa1 \xd0\xbd\xd0\xb0 \xd0\x9b\xd0\xb5\xd1\x82\xd0\xbe 2019</td>\n          </tr>\n          <tr>\n            <th valign="BASELINE" nowrap="nowrap" align="RIGHT">\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0: </th>\n            <td>Fri, 7 Dec 2018 08:23:21 +0500</td>\n          </tr>\n          <tr>\n            <th valign="BASELINE" nowrap="nowrap" align="RIGHT">\xd0\x9e\xd1\x82: </th>\n            <td>1 <a class="moz-txt-link-rfc2396E" href="mailto:a.pl@com.ru">&lt;a.pl@com.ru&gt;</a></td>\n          </tr>\n          <tr>\n            <th valign="BASELINE" nowrap="nowrap" align="RIGHT">\xd0\x9a\xd0\xbe\xd0\xbc\xd1\x83: </th>\n            <td>2 <a class="moz-txt-link-rfc2396E" href="mailto:schedule@com.ru">&lt;schedule@com.ru&gt;</a></td>\n          </tr>\n        </tbody>\n      </table>\n      <br>\n      <br>\n      <meta http-equiv="content-type" content="text/html; charset=UTF-8">\n      <div id="smartTemplate4-template">\xd0\x94\xd0\xbe\xd0\xb1\xd1\x80\xd1\x8b\xd0\xb9\xc2\xa0\xd0\xb4\xd0\xb5\xd0\xbd\xd1\x8c,\xc2\xa0\xd1\x83\xd0\xb2\xd0\xb0\xd0\xb6\xd0\xb0\xd0\xb5\xd0\xbc\xd1\x8b\xd0\xb5\xc2\xa0\xd0\xba\xd0\xbe\xd0\xbb\xd0\xbb\xd0\xb5\xd0\xb3\xd0\xb8!\n        <p>\xd0\x9f\xd1\x80\xd0\xbe\xd1\x88\xd1\x83 \xd0\xb2\xd0\xb2\xd0\xb5\xd1\x81\xd1\x82\xd0\xb8 \xd1\x80\xd0\xb5\xd0\xb9\xd1\x81 \xd0\xbd\xd0\xb0 \xd0\xbf\xd0\xb5\xd1\x80\xd0\xb8\xd0\xbe\xd0\xb4 \xd0\xbb\xd0\xb5\xd1\x82\xd0\xbd\xd0\xb5\xd0\xb9 \xd0\xbd\xd0\xb0\xd0\xb2\xd0\xb8\xd0\xb3\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8 <br>\n        </p>\n        <p>\xc2\xa0 \xd1\x82\xd0\xb8\xd0\xbf \xd0\x92\xd0\xa1 \xd0\x90320<br>\n        </p>\n        <p>\xd0\x92\xd0\x92 \xd0\xb8\xd0\xb7 \xd0\x94\xd0\x9c\xd0\x94 23:00 LT. \xd0\x92\xd0\x92 \xd0\xb8\xd0\xb7 \xd0\xa2\xd0\xae\xd0\x9c 06:45 LT</p>\n        <p>\xd0\xb8\xd1\x81\xd0\xba\xd0\xbb\xd1\x8e\xd1\x87\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xbf\xd0\xb5\xd1\x80\xd0\xb8\xd0\xbe\xd0\xb4 \xd1\x81 25/05/19 \xd0\xbf\xd0\xbe 13/10/19 <br>\n        </p>\n        <p>\xd0\x92\xd0\x92 \xd0\xb8\xd0\xb7 \xd0\x94\xd0\x9c\xd0\x94 \xd0\xb2 00:50 LT<br>\n        </p>\n        <p>\xd0\x92\xd0\x92 \xd0\xb8\xd0\xb7 \xd0\xa2\xd0\xae\xd0\x9c \xd0\xbe\xd1\x81\xd1\x82\xd0\xb0\xd0\xb5\xd1\x82\xd1\x81\xd1\x8f \xd0\xb1\xd0\xb5\xd0\xb7 \xd0\xb8\xd0\xb7\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f <br>\n        </p>\n        <p>----------------------------------------</p>\n        <p>\xc2\xa0 \xd1\x82\xd0\xb8\xd0\xbf \xd0\x92\xd0\xa1 \xd0\x90321</p>\n        <p>\xd0\x92\xd0\x92 \xd0\xb8\xd0\xb7 \xd0\x94\xd0\x9c\xd0\x94 \xd0\xb2 23:15. \xd0\x92\xd0\x92 \xd0\xb8\xd0\xb7 \xd0\x9e\xd0\x9c\xd0\xa1 06:30 LT <br>\n        </p>\n        <p>----------------------------------------</p>\n        <p>\xc2\xa0 \xd1\x82\xd0\xb8\xd0\xbf \xd0\x92\xd0\xa1 \xd0\x90320</p>\n        <p>\xd0\x92\xd0\x92 \xd0\xb8\xd0\xb7 \xd0\x94\xd0\x9c\xd0\x94 \xd0\xb2 23:30. \xd0\x92\xd0\x92 \xd0\xb8\xd0\xb7 \xd0\xa7\xd0\x9b\xd0\x91 06:40 LT </p>\n      </div>\n      <br>\n    </div>\n  </body>\n</html>\n\n--------------CC10C5F7DB2594C21A5E2BDB--\n\n'
            ),
        ],
        from_values={'email': 'k1@yandex.ru', 'name': 'Каукин Владимир', 'full': 'Каукин Владимир <k1@yandex.ru>'},
        to_values=({'email': 'rasp@wat.aero', 'name': 'ТЮМЕНЬ', 'full': 'ТЮМЕНЬ <rasp@wat.aero>'},),
        cc_values=({'email': 'aa@com.ru', 'name': '', 'full': 'aa@com.ru'},
                   {'email': 'mm@com.ru', 'name': '', 'full': 'mm@com.ru'}),
        bcc_values=({'email': 'hello@yandex-team.ru', 'name': 'Команда Яндекс.Почты',
                     'full': 'Команда Яндекс.Почты <hello@yandex-team.ru>'},),
        reply_to_values=(),
    ),

    # ===
    'attachment_7bit': dict(
        subject='статус',
        from_='i.kor@company.ru',
        to=('jessica.schmidt@uni.de', 'я你Rabea.Bartölke@uni.de'),
        cc=(),
        bcc=(),
        reply_to=(),
        date=datetime.datetime(2017, 10, 12, 9, 41, 56,
                               tzinfo=datetime.timezone(datetime.timedelta(hours=5, minutes=0))),
        date_str='Thu, 12 Oct 2017 09:41:56 +0500',
        text="""
""".replace('\n', '\r\n'),
        html="""

    <!DOCTYPE html PUBLIC '-//W3C//DTD XHTML 1.0 Strict//EN' 'http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd'>
    <html xmlns='http://www.w3.org/1999/xhtml' lang='ru-ru'
          xml:lang='en-us'>
    <head>
        <meta content="text/html; charset=UTF-8" http-equiv="Content-Type">
        
    </head>

    <body id='body'>
    
    
        
        <a href="http://group.company.ru/ru/order/28922/process/">
            
            Новый заказ №28922
        </a><br>

        
        Создал:
        
            Клиент Ковчег
            (Гусев Дмитрий)
        <br><br>
        
        Сегменты: <br>
        <ul>
            
                <li>Москва - Тель-Авив, some-889, 15.03.2018, эконом: (15 взр.)</li>
            
                <li>Тель-Авив - Москва, some-890, 22.03.2018, эконом: (15 взр.)</li>
            
        </ul><br>
        
        
    

    </body>
    </html>

""".replace('\n', '\r\n'),
        headers={'Message-ID': ('<2405271c-86ac-0a65-e50c-d1ebccfcc644@company.ru>',),
                 'References': ('<20171011085432.15374.20485@web.hades.company>',), 'To': (
                'Jessica Schmidt <jessica.schmidt@uni.de>,\r\n\t=?iso-8859-1?Q?Rabea=2EBart=F6lke=40uni=2Ede?= <\udcd1\udc8f\udce4\udcbd\udca0Rabea.Bart\udcc3\udcb6lke@uni.de>',),
                 'Content-Type': ('multipart/mixed;\r\n boundary="------------BF90926EC9DF73443A6B8F28"',),
                 'X-Spam-Score': ('-2.898',), 'From': ('i.kor@company.ru',), 'Content-Language': ('ru',),
                 'Date': ('Thu, 12 Oct 2017 09:41:56 +0500',),
                 'In-Reply-To': ('<20171011085432.15374.20485@web.hades.company>',), 'X-Spam-Flag': ('NO',),
                 'Return-Path': ('i.kor@company.ru',),
                 'User-Agent': ('Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101\r\n Thunderbird/52.4.0',),
                 'X-Forwarded-Message-Id': ('<20171011085432.15374.20485@web.hades.company>',),
                 'X-Virus-Scanned': ('amavisd-new at m101.comp.ru',), 'Subject': ('=?UTF-8?B?0YHRgtCw0YLRg9GB?=    ',),
                 'MIME-Version': ('1.0',), 'Received': (
                'from m101.comp.ru (LHLO m101.comp.ru) (192.168.99.101) by m101.comp.ru\r\n with LMTP; Thu, 12 Oct 2017 09:41:57 +0500 (YEKT)',
                'from localhost (localhost [127.0.0.1])\r\n\tby m101.comp.ru (Postfix) with ESMTP id 555275B43;\r\n\tThu, 12 Oct 2017 09:41:57 +0500 (YEKT)',
                'from m101.comp.ru ([127.0.0.1])\r\n\tby localhost (m101.comp.ru [127.0.0.1]) (amavisd-new, port 10032)\r\n\twith ESMTP id rY6SAtl4piy1; Thu, 12 Oct 2017 09:41:56 +0500 (YEKT)',
                'from localhost (localhost [127.0.0.1])\r\n\tby m101.comp.ru (Postfix) with ESMTP id C8F0F5B4B;\r\n\tThu, 12 Oct 2017 09:41:56 +0500 (YEKT)',
                'from m101.comp.ru ([127.0.0.1])\r\n\tby localhost (m101.comp.ru [127.0.0.1]) (amavisd-new, port 10026)\r\n\twith ESMTP id kq2wE_i9_8EK; Thu, 12 Oct 2017 09:41:56 +0500 (YEKT)',
                'from [192.168.104.80] (notebook26.hades.company [192.168.104.80])\r\n\tby m101.comp.ru (Postfix) with ESMTPSA id 9563A5B44\r\n\tfor <user@company.ru>; Thu, 12 Oct 2017 09:41:56 +0500 (YEKT)'),
                 'X-Spam-Status': (
                     'No, score=-2.898 required=6.6 tests=[ALL_TRUSTED=-1,\r\n\tBAYES_00=-1.9, HTML_MESSAGE=0.001, URIBL_BLOCKED=0.001]\r\n\tautolearn=ham autolearn_force=no',),
                 'X-Spam-Level': ('',)},
        attachments=[
            dict(
                filename='Contract 25 04 2020.docx',
                content_id='',
                content_disposition='attachment',
                content_type='message/rfc822',
                payload=b'Return-Path: group@company.ru\nReceived: from m101.comp.ru (LHLO m101.comp.ru) (192.168.99.101) by\n m101.comp.ru\n with LMTP; Wed, 11 Oct 2017 13:54:33 +0500 (YEKT)\nReceived: from localhost (localhost [127.0.0.1])\n\tby m101.comp.ru (Postfix) with ESMTP id 04BDE6E3;\n\tWed, 11 Oct 2017 13:54:33 +0500 (YEKT)\nX-Spam-Flag: NO\nX-Spam-Score: -2.899\nX-Spam-Level: \nX-Spam-Status: No, score=-2.899 required=6.6 tests=[ALL_TRUSTED=-1,\n\tBAYES_00=-1.9, HTML_MESSAGE=0.001, RP_MATCHES_RCVD=-0.001,\n\tURIBL_BLOCKED=0.001] autolearn=ham autolearn_force=no\nReceived: from m101.comp.ru ([127.0.0.1])\n\tby localhost (m101.comp.ru [127.0.0.1]) (amavisd-new, port 10032)\n\twith ESMTP id 3N3XVuSw23lT; Wed, 11 Oct 2017 13:54:32 +0500 (YEKT)\nReceived: from localhost (localhost [127.0.0.1])\n\tby m101.comp.ru (Postfix) with ESMTP id 83DB56E6;\n\tWed, 11 Oct 2017 13:54:32 +0500 (YEKT)\nX-Virus-Scanned: amavisd-new at m101.comp.ru\nReceived: from m101.comp.ru ([127.0.0.1])\n\tby localhost (m101.comp.ru [127.0.0.1]) (amavisd-new, port 10026)\n\twith ESMTP id ylUz-3bpEY_5; Wed, 11 Oct 2017 13:54:32 +0500 (YEKT)\nReceived: from web.hades.company (s192-168-99-108.some.ru [192.168.99.108])\n\tby m101.comp.ru (Postfix) with ESMTPSA id 5AE656E3;\n\tWed, 11 Oct 2017 13:54:32 +0500 (YEKT)\nContent-Type: multipart/alternative;\n boundary="===============3693132879591888836=="\nMIME-Version: 1.0\nSubject: =?UTF-8?B?0YHRgtCw0YLRg9GB?=    \nFrom: group@company.ru\nTo: group@company.ru\nDate: Wed, 11 Oct 2017 08:54:32 -0000\nMessage-ID: <20171011085432.15374.20485@web.hades.company>\n\n--===============3693132879591888836==\nContent-Type: text/plain; charset="utf-8"\nMIME-Version: 1.0\nContent-Transfer-Encoding: quoted-printable\n\n=D0=9D=D0=BE=D0=B2=D1=8B=D0=B9 =D0=B7=D0=B0=D0=BA=D0=B0=D0=B7 =E2=84=9628=\n922 http://group.company.ru/ru/order/28922/process/\n=D0=A1=D0=BE=D0=B7=D0=B4=D0=B0=D0=BB:=20\n=D0=9A=D0=BB=D0=B8=D0=B5=D0=BD=D1=82 =D0=9A=D0=BE=D0=B2=D1=87=D0=B5=D0=B3=\n (=D0=93=D1=83=D1=81=D0=B5=D0=B2 =D0=94=D0=BC=D0=B8=D1=82=D1=80=D0=B8=D0=B9=\n)\n\n=D0=A1=D0=B5=D0=B3=D0=BC=D0=B5=D0=BD=D1=82=D1=8B:\n\n- =D0=9C=D0=BE=D1=81=D0=BA=D0=B2=D0=B0 - =D0=A2=D0=B5=D0=BB=D1=8C-=D0=90=D0=\n=B2=D0=B8=D0=B2, some-889, 15.03.2018, =D1=8D=D0=BA=D0=BE=D0=BD=D0=BE=D0=BC=\n: (15 =D0=B2=D0=B7=D1=80.)\n\n- =D0=A2=D0=B5=D0=BB=D1=8C-=D0=90=D0=B2=D0=B8=D0=B2 - =D0=9C=D0=BE=D1=81=D0=\n=BA=D0=B2=D0=B0, some-890, 22.03.2018, =D1=8D=D0=BA=D0=BE=D0=BD=D0=BE=D0=BC=\n: (15 =D0=B2=D0=B7=D1=80.)\n--===============3693132879591888836==\nContent-Type: text/html; charset="utf-8"\nMIME-Version: 1.0\nContent-Transfer-Encoding: quoted-printable\n\n\n\n    <!DOCTYPE html PUBLIC \'-//W3C//DTD XHTML 1.0 Strict//EN\' \'http://www.=\nw3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\'>\n    <html xmlns=3D\'http://www.w3.org/1999/xhtml\' lang=3D\'ru-ru\'\n          xml:lang=3D\'en-us\'>\n    <head>\n        <meta content=3D"text/html; charset=3DUTF-8" http-equiv=3D"Conten=\nt-Type">\n       =20\n    </head>\n\n    <body id=3D\'body\'>\n   =20\n   =20\n       =20\n        <a href=3D"http://group.company.ru/ru/order/28922/process/">\n           =20\n            =D0=9D=D0=BE=D0=B2=D1=8B=D0=B9 =D0=B7=D0=B0=D0=BA=D0=B0=D0=B7=\n =E2=84=9628922\n        </a><br>\n\n       =20\n        =D0=A1=D0=BE=D0=B7=D0=B4=D0=B0=D0=BB:\n       =20\n            =D0=9A=D0=BB=D0=B8=D0=B5=D0=BD=D1=82 =D0=9A=D0=BE=D0=B2=D1=87=\n=D0=B5=D0=B3\n            (=D0=93=D1=83=D1=81=D0=B5=D0=B2 =D0=94=D0=BC=D0=B8=D1=82=D1=80=\n=D0=B8=D0=B9)\n        <br><br>\n       =20\n        =D0=A1=D0=B5=D0=B3=D0=BC=D0=B5=D0=BD=D1=82=D1=8B: <br>\n        <ul>\n           =20\n                <li>=D0=9C=D0=BE=D1=81=D0=BA=D0=B2=D0=B0 - =D0=A2=D0=B5=D0=\n=BB=D1=8C-=D0=90=D0=B2=D0=B8=D0=B2, some-889, 15.03.2018, =D1=8D=D0=BA=D0=BE=\n=D0=BD=D0=BE=D0=BC: (15 =D0=B2=D0=B7=D1=80.)</li>\n           =20\n                <li>=D0=A2=D0=B5=D0=BB=D1=8C-=D0=90=D0=B2=D0=B8=D0=B2 - =D0=\n=9C=D0=BE=D1=81=D0=BA=D0=B2=D0=B0, some-890, 22.03.2018, =D1=8D=D0=BA=D0=BE=\n=D0=BD=D0=BE=D0=BC: (15 =D0=B2=D0=B7=D1=80.)</li>\n           =20\n        </ul><br>\n       =20\n       =20\n   =20\n\n    </body>\n    </html>\n\n\n--===============3693132879591888836==--\n'
            ),
        ],
        from_values={'email': 'i.kor@company.ru', 'name': '', 'full': 'i.kor@company.ru'},
        to_values=({'email': 'jessica.schmidt@uni.de', 'name': 'Jessica Schmidt',
                    'full': 'Jessica Schmidt <jessica.schmidt@uni.de>'},
                   {'email': 'я你Rabea.Bartölke@uni.de', 'name': 'Rabea.Bartölke@uni.de',
                    'full': 'Rabea.Bartölke@uni.de <я你Rabea.Bartölke@uni.de>'}),
        cc_values=(),
        bcc_values=(),
        reply_to_values=(),
    ),

    # ===
    'attachment_2_base64': dict(
        subject='eml attachments ',
        from_='kaukinvk@yandex.ru',
        to=('imap.tools@ya.ru',),
        cc=(),
        bcc=(),
        reply_to=(),
        date=datetime.datetime(2019, 5, 1, 12, 20, 29,
                               tzinfo=datetime.timezone(datetime.timedelta(hours=5, minutes=0))),
        date_str='Wed, 01 May 2019 12:20:29 +0500',
        text="""UmVjZWl2ZWQ6IGZyb20gbXhmcm9udDJnLm1haWwueWFuZGV4Lm5ldCAoWzEyNy4wLjAuMV0pDQoJ
YnkgbXhmcm9udDJnLm1haWwueWFuZGV4Lm5ldCB3aXRoIExNVFAgaWQgU09ObW5QYjENCglmb3Ig
PEthdWtpblZLQHlhbmRleC5ydT47IFN1biwgMjggQXByIDIwMTkgMTQ6MzI6MzcgKzAzMDANClJl
Y2VpdmVkOiBmcm9tIG91dC0zLnNtdHAuZ2l0aHViLmNvbSAob3V0LTMuc210cC5naXRodWIuY29t
IFsxOTIuMzAuMjUyLjE5NF0pDQoJYnkgbXhmcm9udDJnLm1haWwueWFuZGV4Lm5ldCAobndzbXRw
L1lhbmRleCkgd2l0aCBFU01UUFMgaWQgSXhHMDdMUnRqYi1XYXJtNGVYVzsNCglTdW4sIDI4IEFw
ciAyMDE5IDE0OjMyOjM2ICswMzAwDQoJKHVzaW5nIFRMU3YxLjIgd2l0aCBjaXBoZXIgRUNESEUt
UlNBLUFFUzEyOC1HQ00tU0hBMjU2ICgxMjgvMTI4IGJpdHMpKQ0KCShDbGllbnQgY2VydGlmaWNh
dGUgbm90IHByZXNlbnQpDQpSZXR1cm4tUGF0aDogbm9yZXBseUBnaXRodWIuY29tDQpYLVlhbmRl
eC1Gcm9udDogbXhmcm9udDJnLm1haWwueWFuZGV4Lm5ldA0KWC1ZYW5kZXgtVGltZU1hcms6IDE1
NTY0NTExNTYuMTUzDQpBdXRoZW50aWNhdGlvbi1SZXN1bHRzOiBteGZyb250MmcubWFpbC55YW5k
ZXgubmV0OyBzcGY9cGFzcyAobXhmcm9udDJnLm1haWwueWFuZGV4Lm5ldDogZG9tYWluIG9mIGdp
dGh1Yi5jb20gZGVzaWduYXRlcyAxOTIuMzAuMjUyLjE5NCBhcyBwZXJtaXR0ZWQgc2VuZGVyLCBy
dWxlPVtpcDQ6MTkyLjMwLjI1Mi4wLzIyXSkgc210cC5tYWlsPW5vcmVwbHlAZ2l0aHViLmNvbTsg
ZGtpbT1wYXNzIGhlYWRlci5pPUBnaXRodWIuY29tDQpYLVlhbmRleC1TcGFtOiAyDQpYLVlhbmRl
eC1Gd2Q6IE9UTTRPVE00TWpjMk9UVTNOVFUzTlRZeU15dzVOek01TVRFMk1UYzVOekkwTVRBeE9U
TXcNCkRhdGU6IFN1biwgMjggQXByIDIwMTkgMDQ6MzI6MzUgLTA3MDANCkRLSU0tU2lnbmF0dXJl
OiB2PTE7IGE9cnNhLXNoYTI1NjsgYz1yZWxheGVkL3JlbGF4ZWQ7IGQ9Z2l0aHViLmNvbTsNCglz
PXBmMjAxNDsgdD0xNTU2NDUxMTU1Ow0KCWJoPUZzUlBVS24zYmV1cHQyUDNRQjM2VXpmVkVTVkNs
TDA3VFZJTm5UWDBuQmc9Ow0KCWg9RGF0ZTpGcm9tOlJlcGx5LVRvOlRvOkNjOlN1YmplY3Q6TGlz
dC1JRDpMaXN0LUFyY2hpdmU6TGlzdC1Qb3N0Og0KCSBMaXN0LVVuc3Vic2NyaWJlOkZyb207DQoJ
Yj1iemZRcnYyNW8wSXBaS2lJcmNHZ0x6RHZNMlZMZllmaWN6anFTUFBUMFJkM3UzRDY2YXd3bHhh
VkVIV3FwRTZkYw0KCSA4RVRSMCtBM2tOMVYzeGxvOUV0bGduMzExMDVnM09RRkcwakJNVGR5bWRh
WEEvaHU4SHJqcjRXZjFrckFHcXVIcHENCgkgZ0pvRjRDaHVNdVVoTDU1NGhndUFtc1daMUJtemNq
SDZ2VlNhMFpFVT0NCkZyb206IEJ1ZGR5IFJpa2FyZCA8bm90aWZpY2F0aW9uc0BnaXRodWIuY29t
Pg0KUmVwbHktVG86IGlrdmsvaW1hcF90b29scyA8cmVwbHkrQUFWNk4yWjVaTVZZUFZWTUpCWEVa
RTUyMkxBNUhFVkJOSEhCVUhBUEpVQHJlcGx5LmdpdGh1Yi5jb20+DQpUbzogaWt2ay9pbWFwX3Rv
b2xzIDxpbWFwX3Rvb2xzQG5vcmVwbHkuZ2l0aHViLmNvbT4NCkNjOiBTdWJzY3JpYmVkIDxzdWJz
Y3JpYmVkQG5vcmVwbHkuZ2l0aHViLmNvbT4NCk1lc3NhZ2UtSUQ6IDxpa3ZrL2ltYXBfdG9vbHMv
aXNzdWVzLzRAZ2l0aHViLmNvbT4NClN1YmplY3Q6IFtpa3ZrL2ltYXBfdG9vbHNdIGRvZXMgbm90
IGV4dHJhY3QgYXR0YWNoZWQgRU1MIGZpbGVzICgjNCkNCk1pbWUtVmVyc2lvbjogMS4wDQpDb250
ZW50LVR5cGU6IG11bHRpcGFydC9hbHRlcm5hdGl2ZTsNCiBib3VuZGFyeT0iLS09PV9taW1lcGFy
dF81Y2M1OGY1Mzc1NDJfNDllYjNmYmE0MGNjZDk2MDMwODRiZSI7DQogY2hhcnNldD1VVEYtOA0K
Q29udGVudC1UcmFuc2Zlci1FbmNvZGluZzogN2JpdA0KUHJlY2VkZW5jZTogbGlzdA0KWC1HaXRI
dWItU2VuZGVyOiBUcHlvS25pZw0KWC1HaXRIdWItUmVjaXBpZW50OiBpa3ZrDQpYLUdpdEh1Yi1S
ZWFzb246IHN1YnNjcmliZWQNCkxpc3QtSUQ6IGlrdmsvaW1hcF90b29scyA8aW1hcF90b29scy5p
a3ZrLmdpdGh1Yi5jb20+DQpMaXN0LUFyY2hpdmU6IGh0dHBzOi8vZ2l0aHViLmNvbS9pa3ZrL2lt
YXBfdG9vbHMNCkxpc3QtUG9zdDogPG1haWx0bzpyZXBseStBQVY2TjJaNVpNVllQVlZNSkJYRVpF
NTIyTEE1SEVWQk5ISEJVSEFQSlVAcmVwbHkuZ2l0aHViLmNvbT4NCkxpc3QtVW5zdWJzY3JpYmU6
IDxtYWlsdG86dW5zdWIrQUFWNk4yWjVaTVZZUFZWTUpCWEVaRTUyMkxBNUhFVkJOSEhCVUhBUEpV
QHJlcGx5LmdpdGh1Yi5jb20+LA0KIDxodHRwczovL2dpdGh1Yi5jb20vbm90aWZpY2F0aW9ucy91
bnN1YnNjcmliZS9BQVY2TjI0UkpZR0dRQkk1UEtNR1RLM1BTV0ROSEFOQ05GU000SEk2SlFVQT4N
ClgtQXV0by1SZXNwb25zZS1TdXBwcmVzczogQWxsDQpYLUdpdEh1Yi1SZWNpcGllbnQtQWRkcmVz
czogS2F1a2luVktAeWFuZGV4LnJ1DQpYLVlhbmRleC1Gb3J3YXJkOiBlZmI0MmQ3NmVkZjdkNTU1
NjExMmYzZGFjMDk5NDA2ZQ0KDQoNCi0tLS09PV9taW1lcGFydF81Y2M1OGY1Mzc1NDJfNDllYjNm
YmE0MGNjZDk2MDMwODRiZQ0KQ29udGVudC1UeXBlOiB0ZXh0L3BsYWluOw0KIGNoYXJzZXQ9VVRG
LTgNCkNvbnRlbnQtVHJhbnNmZXItRW5jb2Rpbmc6IDdiaXQNCg0KQXMgLkVNTCBmaWxlcyBoYXZl
IHRoZXNlIGhlYWRlcnM6DQoNCmAtLTAwMDAwMDAwMDAwMDk0ODA5MTA1ODc4ZGFhYzANCkNvbnRl
bnQtVHlwZTogbWVzc2FnZS9yZmM4MjI7IG5hbWU9IlRvdGFsbHkgbGVnaXQgZW1haWwgKDIpLmVt
bCINCkNvbnRlbnQtRGlzcG9zaXRpb246IGF0dGFjaG1lbnQ7IGZpbGVuYW1lPSJUb3RhbGx5IGxl
Z2l0IGVtYWlsICgyKS5lbWwiDQpDb250ZW50LVRyYW5zZmVyLUVuY29kaW5nOiBiYXNlNjQNCkNv
bnRlbnQtSUQ6IDxmX2p2MGFwcHJiMD4NClgtQXR0YWNobWVudC1JZDogZl9qdjBhcHByYjANCg0K
TUlNRS1WZXJzaW9uOiAxLjANCkRhdGU6IEZyaSwgMjUgSmFuIDIwMTkgMTA6Mzc6NDcgLTA4MDAN
Ck1lc3NhZ2UtSUQ6IDxDQUtLWHozTzVxRm9UaTY4THM0UUNxWnpRSzhtNm1BU3ltVFo5aWI2eXNu
QlRPd3dKT2dAbWFpbC5nbWFpbC5jb20+DQpTdWJqZWN0OiBUb3RhbGx5IGxlZ2l0IGVtYWlsDQpG
cm9tOiBSRURBQ1RFRCA8UkVEQUNURURARE9NQUlOLkNPTT4NClRvOiBSRURBQ1RFRCA8UkVEQUNU
RURARE9NQUlOLkNPTT4NCkNvbnRlbnQtVHlwZTogbXVsdGlwYXJ0L2FsdGVybmF0aXZlOyBib3Vu
ZGFyeT0iMDAwMDAwMDAwMDAwYTMwYmI2MDU4MDRjOWZmMiINCg0KLS0wMDAwMDAwMDAwMDBhMzBi
YjYwNTgwNGM5ZmYyDQpDb250ZW50LVR5cGU6IHRleHQvcGxhaW47IGNoYXJzZXQ9IlVURi04Ig0K
Q29udGVudC1UcmFuc2Zlci1FbmNvZGluZzogcXVvdGVkLXByaW50YWJsZWANCg0KaW1hcC10b29s
cyBkb2VzIG5vdCByZXR1cm4gdGhpcyBhcyBhbiBhdHRhY2htZW50IGFuZCBjb21wbGV0ZWx5IGRp
c3JlZ2FyZHMgdGhlIGF0dGFjaG1lbnQgaXRzZWxmIGFsb25nIHdpdGggdGhlIGZpbGVuYW1lLiAN
Cg0KLS0gDQpZb3UgYXJlIHJlY2VpdmluZyB0aGlzIGJlY2F1c2UgeW91IGFyZSBzdWJzY3JpYmVk
IHRvIHRoaXMgdGhyZWFkLg0KUmVwbHkgdG8gdGhpcyBlbWFpbCBkaXJlY3RseSBvciB2aWV3IGl0
IG9uIEdpdEh1YjoNCmh0dHBzOi8vZ2l0aHViLmNvbS9pa3ZrL2ltYXBfdG9vbHMvaXNzdWVzLzQN
Ci0tLS09PV9taW1lcGFydF81Y2M1OGY1Mzc1NDJfNDllYjNmYmE0MGNjZDk2MDMwODRiZQ0KQ29u
dGVudC1UeXBlOiB0ZXh0L2h0bWw7DQogY2hhcnNldD1VVEYtOA0KQ29udGVudC1UcmFuc2Zlci1F
bmNvZGluZzogN2JpdA0KDQo8cD5BcyAuRU1MIGZpbGVzIGhhdmUgdGhlc2UgaGVhZGVyczo8L3A+
DQo8cD5gLS0wMDAwMDAwMDAwMDA5NDgwOTEwNTg3OGRhYWMwPGJyPg0KQ29udGVudC1UeXBlOiBt
ZXNzYWdlL3JmYzgyMjsgbmFtZT0iVG90YWxseSBsZWdpdCBlbWFpbCAoMikuZW1sIjxicj4NCkNv
bnRlbnQtRGlzcG9zaXRpb246IGF0dGFjaG1lbnQ7IGZpbGVuYW1lPSJUb3RhbGx5IGxlZ2l0IGVt
YWlsICgyKS5lbWwiPGJyPg0KQ29udGVudC1UcmFuc2Zlci1FbmNvZGluZzogYmFzZTY0PGJyPg0K
Q29udGVudC1JRDogJmx0O2ZfanYwYXBwcmIwJmd0Ozxicj4NClgtQXR0YWNobWVudC1JZDogZl9q
djBhcHByYjA8L3A+DQo8cD5NSU1FLVZlcnNpb246IDEuMDxicj4NCkRhdGU6IEZyaSwgMjUgSmFu
IDIwMTkgMTA6Mzc6NDcgLTA4MDA8YnI+DQpNZXNzYWdlLUlEOiA8YSBocmVmPSJtYWlsdG86Q0FL
S1h6M081cUZvVGk2OExzNFFDcVp6UUs4bTZtQVN5bVRaOWliNnlzbkJUT3d3Sk9nQG1haWwuZ21h
aWwuY29tIj5DQUtLWHozTzVxRm9UaTY4THM0UUNxWnpRSzhtNm1BU3ltVFo5aWI2eXNuQlRPd3dK
T2dAbWFpbC5nbWFpbC5jb208L2E+PGJyPg0KU3ViamVjdDogVG90YWxseSBsZWdpdCBlbWFpbDxi
cj4NCkZyb206IFJFREFDVEVEIDxhIGhyZWY9Im1haWx0bzpSRURBQ1RFREBET01BSU4uQ09NIj5S
RURBQ1RFREBET01BSU4uQ09NPC9hPjxicj4NClRvOiBSRURBQ1RFRCA8YSBocmVmPSJtYWlsdG86
UkVEQUNURURARE9NQUlOLkNPTSI+UkVEQUNURURARE9NQUlOLkNPTTwvYT48YnI+DQpDb250ZW50
LVR5cGU6IG11bHRpcGFydC9hbHRlcm5hdGl2ZTsgYm91bmRhcnk9IjAwMDAwMDAwMDAwMGEzMGJi
NjA1ODA0YzlmZjIiPC9wPg0KPHA+LS0wMDAwMDAwMDAwMDBhMzBiYjYwNTgwNGM5ZmYyPGJyPg0K
Q29udGVudC1UeXBlOiB0ZXh0L3BsYWluOyBjaGFyc2V0PSJVVEYtOCI8YnI+DQpDb250ZW50LVRy
YW5zZmVyLUVuY29kaW5nOiBxdW90ZWQtcHJpbnRhYmxlYDwvcD4NCjxwPmltYXAtdG9vbHMgZG9l
cyBub3QgcmV0dXJuIHRoaXMgYXMgYW4gYXR0YWNobWVudCBhbmQgY29tcGxldGVseSBkaXNyZWdh
cmRzIHRoZSBhdHRhY2htZW50IGl0c2VsZiBhbG9uZyB3aXRoIHRoZSBmaWxlbmFtZS48L3A+DQoN
CjxwIHN0eWxlPSJmb250LXNpemU6c21hbGw7LXdlYmtpdC10ZXh0LXNpemUtYWRqdXN0Om5vbmU7
Y29sb3I6IzY2NjsiPiZtZGFzaDs8YnIgLz5Zb3UgYXJlIHJlY2VpdmluZyB0aGlzIGJlY2F1c2Ug
eW91IGFyZSBzdWJzY3JpYmVkIHRvIHRoaXMgdGhyZWFkLjxiciAvPlJlcGx5IHRvIHRoaXMgZW1h
aWwgZGlyZWN0bHksIDxhIGhyZWY9Imh0dHBzOi8vZ2l0aHViLmNvbS9pa3ZrL2ltYXBfdG9vbHMv
aXNzdWVzLzQiPnZpZXcgaXQgb24gR2l0SHViPC9hPiwgb3IgPGEgaHJlZj0iaHR0cHM6Ly9naXRo
dWIuY29tL25vdGlmaWNhdGlvbnMvdW5zdWJzY3JpYmUtYXV0aC9BQVY2TjJaRDJQNU1XMzMzMjJH
REFGVFBTV0ROSEFOQ05GU000SEk2SlFVQSI+bXV0ZSB0aGUgdGhyZWFkPC9hPi48aW1nIHNyYz0i
aHR0cHM6Ly9naXRodWIuY29tL25vdGlmaWNhdGlvbnMvYmVhY29uL0FBVjZOMjdKRUI0U0JDRTNW
SUxQTzZMUFNXRE5IQU5DTkZTTTRISTZKUVVBLmdpZiIgaGVpZ2h0PSIxIiB3aWR0aD0iMSIgYWx0
PSIiIC8+PC9wPg0KPHNjcmlwdCB0eXBlPSJhcHBsaWNhdGlvbi9qc29uIiBkYXRhLXNjb3BlPSJp
bmJveG1hcmt1cCI+eyJhcGlfdmVyc2lvbiI6IjEuMCIsInB1Ymxpc2hlciI6eyJhcGlfa2V5Ijoi
MDVkZGU1MGYxZDFhMzg0ZGQ3ODc2N2M1NTQ5M2U0YmIiLCJuYW1lIjoiR2l0SHViIn0sImVudGl0
eSI6eyJleHRlcm5hbF9rZXkiOiJnaXRodWIvaWt2ay9pbWFwX3Rvb2xzIiwidGl0bGUiOiJpa3Zr
L2ltYXBfdG9vbHMiLCJzdWJ0aXRsZSI6IkdpdEh1YiByZXBvc2l0b3J5IiwibWFpbl9pbWFnZV91
cmwiOiJodHRwczovL2dpdGh1Yi5naXRodWJhc3NldHMuY29tL2ltYWdlcy9lbWFpbC9tZXNzYWdl
X2NhcmRzL2hlYWRlci5wbmciLCJhdmF0YXJfaW1hZ2VfdXJsIjoiaHR0cHM6Ly9naXRodWIuZ2l0
aHViYXNzZXRzLmNvbS9pbWFnZXMvZW1haWwvbWVzc2FnZV9jYXJkcy9hdmF0YXIucG5nIiwiYWN0
aW9uIjp7Im5hbWUiOiJPcGVuIGluIEdpdEh1YiIsInVybCI6Imh0dHBzOi8vZ2l0aHViLmNvbS9p
a3ZrL2ltYXBfdG9vbHMifX0sInVwZGF0ZXMiOnsic25pcHBldHMiOlt7Imljb24iOiJERVNDUklQ
VElPTiIsIm1lc3NhZ2UiOiJkb2VzIG5vdCBleHRyYWN0IGF0dGFjaGVkIEVNTCBmaWxlcyAoIzQp
In1dLCJhY3Rpb24iOnsibmFtZSI6IlZpZXcgSXNzdWUiLCJ1cmwiOiJodHRwczovL2dpdGh1Yi5j
b20vaWt2ay9pbWFwX3Rvb2xzL2lzc3Vlcy80In19fTwvc2NyaXB0Pg0KPHNjcmlwdCB0eXBlPSJh
cHBsaWNhdGlvbi9sZCtqc29uIj5bDQp7DQoiQGNvbnRleHQiOiAiaHR0cDovL3NjaGVtYS5vcmci
LA0KIkB0eXBlIjogIkVtYWlsTWVzc2FnZSIsDQoicG90ZW50aWFsQWN0aW9uIjogew0KIkB0eXBl
IjogIlZpZXdBY3Rpb24iLA0KInRhcmdldCI6ICJodHRwczovL2dpdGh1Yi5jb20vaWt2ay9pbWFw
X3Rvb2xzL2lzc3Vlcy80IiwNCiJ1cmwiOiAiaHR0cHM6Ly9naXRodWIuY29tL2lrdmsvaW1hcF90
b29scy9pc3N1ZXMvNCIsDQoibmFtZSI6ICJWaWV3IElzc3VlIg0KfSwNCiJkZXNjcmlwdGlvbiI6
ICJWaWV3IHRoaXMgSXNzdWUgb24gR2l0SHViIiwNCiJwdWJsaXNoZXIiOiB7DQoiQHR5cGUiOiAi
T3JnYW5pemF0aW9uIiwNCiJuYW1lIjogIkdpdEh1YiIsDQoidXJsIjogImh0dHBzOi8vZ2l0aHVi
LmNvbSINCn0NCn0NCl08L3NjcmlwdD4NCi0tLS09PV9taW1lcGFydF81Y2M1OGY1Mzc1NDJfNDll
YjNmYmE0MGNjZDk2MDMwODRiZS0tDQo=""".replace('\n', '\r\n'),
        html='<div>two attach</div>',
        headers={'X-Yandex-Internal': ('1',), 'Received': (
            'from mxback2g.mail.yandex.net ([127.0.0.1])\r\n\tby mxback2g.mail.yandex.net with LMTP id GCaAmtYs;\r\n\tWed, 1 May 2019 10:20:30 +0300',
            'from mxback2g.mail.yandex.net (localhost.localdomain [127.0.0.1])\r\n\tby mxback2g.mail.yandex.net (Yandex) with ESMTP id C4C9426E11B7;\r\n\tWed,  1 May 2019 10:20:30 +0300 (MSK)',
            'from localhost (localhost [::1])\r\n\tby mxback2g.mail.yandex.net (nwsmtp/Yandex) with ESMTP id HIJe2M7myP-KThSAlHL;\r\n\tWed, 01 May 2019 10:20:29 +0300',
            'by myt5-262fb1897c00.qloud-c.yandex.net with HTTP;\r\n\tWed, 01 May 2019 10:20:29 +0300'),
                 'X-Yandex-Spam': ('1',), 'Return-Path': ('kaukinvk@yandex.ru',), 'X-Yandex-Sender-Uid': ('52494202',),
                 'Envelope-From': ('kaukinvk@yandex.ru',),
                 'Message-Id': ('<8872861556695229@myt5-262fb1897c00.qloud-c.yandex.net>',),
                 'X-Yandex-TimeMark': ('1556695229.976',), 'To': ('imap.tools@ya.ru',), 'MIME-Version': ('1.0',),
                 'Authentication-Results': ('mxback2g.mail.yandex.net; dkim=pass header.i=@yandex.ru',),
                 'X-Yandex-Forward': ('d910e166fb8fe03380632bd988c8b67f',),
                 'X-Mailer': ('Yamail [ http://yandex.ru ] 5.0',), 'X-Yandex-Front': ('mxback2g.mail.yandex.net',),
                 'Subject': ('eml attachments ',), 'DKIM-Signature': (
                'v=1; a=rsa-sha256; c=relaxed/relaxed; d=yandex.ru; s=mail; t=1556695230;\r\n\tbh=Zmx9VIRnyRQRflnyRn1kpGYLdyO5YBC6/Wu9orXmTDk=;\r\n\th=Message-Id:Date:Subject:To:From;\r\n\tb=AM6LCew9Mz4XSIF78liQrYp4Kyg9RonJDizzaCNBRs5bOwla7bFphFQMIIYfmneJw\r\n\t 51WhDeo5L9ahRqG27no2kwmOggZ+Do99qY8oReCFObnfnaII6V2ZIvogKFXEfjHTB0\r\n\t bZlslZahe65zi1+xD7PnpeSWv8aYLZBgPuNJgA10=',),
                 'From': ('=?utf-8?B?0JrQsNGD0LrQuNC9INCS0LvQsNC00LjQvNC40YA=?= <kaukinvk@yandex.ru>',),
                 'Date': ('Wed, 01 May 2019 12:20:29 +0500',), 'Content-Type': (
                'multipart/mixed;\r\n\tboundary="----==--bound.887287.myt5-262fb1897c00.qloud-c.yandex.net"',)},
        attachments=[
            dict(
                filename='yandex_email.eml',
                content_id='',
                content_disposition='attachment',
                content_type='message/rfc822',
                payload=b'Received: from mxfront2g.mail.yandex.net ([127.0.0.1])\r\n\tby mxfront2g.mail.yandex.net with LMTP id SONmnPb1\r\n\tfor <KaukinVK@yandex.ru>; Sun, 28 Apr 2019 14:32:37 +0300\r\nReceived: from out-3.smtp.github.com (out-3.smtp.github.com [192.30.252.194])\r\n\tby mxfront2g.mail.yandex.net (nwsmtp/Yandex) with ESMTPS id IxG07LRtjb-Warm4eXW;\r\n\tSun, 28 Apr 2019 14:32:36 +0300\r\n\t(using TLSv1.2 with cipher ECDHE-RSA-AES128-GCM-SHA256 (128/128 bits))\r\n\t(Client certificate not present)\r\nReturn-Path: noreply@github.com\r\nX-Yandex-Front: mxfront2g.mail.yandex.net\r\nX-Yandex-TimeMark: 1556451156.153\r\nAuthentication-Results: mxfront2g.mail.yandex.net; spf=pass (mxfront2g.mail.yandex.net: domain of github.com designates 192.30.252.194 as permitted sender, rule=[ip4:192.30.252.0/22]) smtp.mail=noreply@github.com; dkim=pass header.i=@github.com\r\nX-Yandex-Spam: 2\r\nX-Yandex-Fwd: OTM4OTM4Mjc2OTU3NTU3NTYyMyw5NzM5MTE2MTc5NzI0MTAxOTMw\r\nDate: Sun, 28 Apr 2019 04:32:35 -0700\r\nDKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed; d=github.com;\r\n\ts=pf2014; t=1556451155;\r\n\tbh=FsRPUKn3beupt2P3QB36UzfVESVClL07TVINnTX0nBg=;\r\n\th=Date:From:Reply-To:To:Cc:Subject:List-ID:List-Archive:List-Post:\r\n\t List-Unsubscribe:From;\r\n\tb=bzfQrv25o0IpZKiIrcGgLzDvM2VLfYficzjqSPPT0Rd3u3D66awwlxaVEHWqpE6dc\r\n\t 8ETR0+A3kN1V3xlo9Etlgn31105g3OQFG0jBMTdymdaXA/hu8Hrjr4Wf1krAGquHpq\r\n\t gJoF4ChuMuUhL554hguAmsWZ1BmzcjH6vVSa0ZEU=\r\nFrom: Buddy Rikard <notifications@github.com>\r\nReply-To: ikvk/imap_tools <reply+AAV6N2Z5ZMVYPVVMJBXEZE522LA5HEVBNHHBUHAPJU@reply.github.com>\r\nTo: ikvk/imap_tools <imap_tools@noreply.github.com>\r\nCc: Subscribed <subscribed@noreply.github.com>\r\nMessage-ID: <ikvk/imap_tools/issues/4@github.com>\r\nSubject: [ikvk/imap_tools] does not extract attached EML files (#4)\r\nMime-Version: 1.0\r\nContent-Type: multipart/alternative;\r\n boundary="--==_mimepart_5cc58f537542_49eb3fba40ccd9603084be";\r\n charset=UTF-8\r\nContent-Transfer-Encoding: 7bit\r\nPrecedence: list\r\nX-GitHub-Sender: TpyoKnig\r\nX-GitHub-Recipient: ikvk\r\nX-GitHub-Reason: subscribed\r\nList-ID: ikvk/imap_tools <imap_tools.ikvk.github.com>\r\nList-Archive: https://github.com/ikvk/imap_tools\r\nList-Post: <mailto:reply+AAV6N2Z5ZMVYPVVMJBXEZE522LA5HEVBNHHBUHAPJU@reply.github.com>\r\nList-Unsubscribe: <mailto:unsub+AAV6N2Z5ZMVYPVVMJBXEZE522LA5HEVBNHHBUHAPJU@reply.github.com>,\r\n <https://github.com/notifications/unsubscribe/AAV6N24RJYGGQBI5PKMGTK3PSWDNHANCNFSM4HI6JQUA>\r\nX-Auto-Response-Suppress: All\r\nX-GitHub-Recipient-Address: KaukinVK@yandex.ru\r\nX-Yandex-Forward: efb42d76edf7d5556112f3dac099406e\r\n\r\n\r\n----==_mimepart_5cc58f537542_49eb3fba40ccd9603084be\r\nContent-Type: text/plain;\r\n charset=UTF-8\r\nContent-Transfer-Encoding: 7bit\r\n\r\nAs .EML files have these headers:\r\n\r\n`--00000000000094809105878daac0\r\nContent-Type: message/rfc822; name="Totally legit email (2).eml"\r\nContent-Disposition: attachment; filename="Totally legit email (2).eml"\r\nContent-Transfer-Encoding: base64\r\nContent-ID: <f_jv0apprb0>\r\nX-Attachment-Id: f_jv0apprb0\r\n\r\nMIME-Version: 1.0\r\nDate: Fri, 25 Jan 2019 10:37:47 -0800\r\nMessage-ID: <CAKKXz3O5qFoTi68Ls4QCqZzQK8m6mASymTZ9ib6ysnBTOwwJOg@mail.gmail.com>\r\nSubject: Totally legit email\r\nFrom: REDACTED <REDACTED@DOMAIN.COM>\r\nTo: REDACTED <REDACTED@DOMAIN.COM>\r\nContent-Type: multipart/alternative; boundary="000000000000a30bb605804c9ff2"\r\n\r\n--000000000000a30bb605804c9ff2\r\nContent-Type: text/plain; charset="UTF-8"\r\nContent-Transfer-Encoding: quoted-printable`\r\n\r\nimap-tools does not return this as an attachment and completely disregards the attachment itself along with the filename. \r\n\r\n-- \r\nYou are receiving this because you are subscribed to this thread.\r\nReply to this email directly or view it on GitHub:\r\nhttps://github.com/ikvk/imap_tools/issues/4\r\n----==_mimepart_5cc58f537542_49eb3fba40ccd9603084be\r\nContent-Type: text/html;\r\n charset=UTF-8\r\nContent-Transfer-Encoding: 7bit\r\n\r\n<p>As .EML files have these headers:</p>\r\n<p>`--00000000000094809105878daac0<br>\r\nContent-Type: message/rfc822; name="Totally legit email (2).eml"<br>\r\nContent-Disposition: attachment; filename="Totally legit email (2).eml"<br>\r\nContent-Transfer-Encoding: base64<br>\r\nContent-ID: &lt;f_jv0apprb0&gt;<br>\r\nX-Attachment-Id: f_jv0apprb0</p>\r\n<p>MIME-Version: 1.0<br>\r\nDate: Fri, 25 Jan 2019 10:37:47 -0800<br>\r\nMessage-ID: <a href="mailto:CAKKXz3O5qFoTi68Ls4QCqZzQK8m6mASymTZ9ib6ysnBTOwwJOg@mail.gmail.com">CAKKXz3O5qFoTi68Ls4QCqZzQK8m6mASymTZ9ib6ysnBTOwwJOg@mail.gmail.com</a><br>\r\nSubject: Totally legit email<br>\r\nFrom: REDACTED <a href="mailto:REDACTED@DOMAIN.COM">REDACTED@DOMAIN.COM</a><br>\r\nTo: REDACTED <a href="mailto:REDACTED@DOMAIN.COM">REDACTED@DOMAIN.COM</a><br>\r\nContent-Type: multipart/alternative; boundary="000000000000a30bb605804c9ff2"</p>\r\n<p>--000000000000a30bb605804c9ff2<br>\r\nContent-Type: text/plain; charset="UTF-8"<br>\r\nContent-Transfer-Encoding: quoted-printable`</p>\r\n<p>imap-tools does not return this as an attachment and completely disregards the attachment itself along with the filename.</p>\r\n\r\n<p style="font-size:small;-webkit-text-size-adjust:none;color:#666;">&mdash;<br />You are receiving this because you are subscribed to this thread.<br />Reply to this email directly, <a href="https://github.com/ikvk/imap_tools/issues/4">view it on GitHub</a>, or <a href="https://github.com/notifications/unsubscribe-auth/AAV6N2ZD2P5MW33322GDAFTPSWDNHANCNFSM4HI6JQUA">mute the thread</a>.<img src="https://github.com/notifications/beacon/AAV6N27JEB4SBCE3VILPO6LPSWDNHANCNFSM4HI6JQUA.gif" height="1" width="1" alt="" /></p>\r\n<script type="application/json" data-scope="inboxmarkup">{"api_version":"1.0","publisher":{"api_key":"05dde50f1d1a384dd78767c55493e4bb","name":"GitHub"},"entity":{"external_key":"github/ikvk/imap_tools","title":"ikvk/imap_tools","subtitle":"GitHub repository","main_image_url":"https://github.githubassets.com/images/email/message_cards/header.png","avatar_image_url":"https://github.githubassets.com/images/email/message_cards/avatar.png","action":{"name":"Open in GitHub","url":"https://github.com/ikvk/imap_tools"}},"updates":{"snippets":[{"icon":"DESCRIPTION","message":"does not extract attached EML files (#4)"}],"action":{"name":"View Issue","url":"https://github.com/ikvk/imap_tools/issues/4"}}}</script>\r\n<script type="application/ld+json">[\r\n{\r\n"@context": "http://schema.org",\r\n"@type": "EmailMessage",\r\n"potentialAction": {\r\n"@type": "ViewAction",\r\n"target": "https://github.com/ikvk/imap_tools/issues/4",\r\n"url": "https://github.com/ikvk/imap_tools/issues/4",\r\n"name": "View Issue"\r\n},\r\n"description": "View this Issue on GitHub",\r\n"publisher": {\r\n"@type": "Organization",\r\n"name": "GitHub",\r\n"url": "https://github.com"\r\n}\r\n}\r\n]</script>\r\n----==_mimepart_5cc58f537542_49eb3fba40ccd9603084be--\r\n'
            ),
            dict(
                filename='yandex_email.eml',
                content_id='',
                content_disposition='attachment',
                content_type='message/rfc822',
                payload=b'Received: from mxfront2g.mail.yandex.net ([127.0.0.1])\r\n\tby mxfront2g.mail.yandex.net with LMTP id SONmnPb1\r\n\tfor <KaukinVK@yandex.ru>; Sun, 28 Apr 2019 14:32:37 +0300\r\nReceived: from out-3.smtp.github.com (out-3.smtp.github.com [192.30.252.194])\r\n\tby mxfront2g.mail.yandex.net (nwsmtp/Yandex) with ESMTPS id IxG07LRtjb-Warm4eXW;\r\n\tSun, 28 Apr 2019 14:32:36 +0300\r\n\t(using TLSv1.2 with cipher ECDHE-RSA-AES128-GCM-SHA256 (128/128 bits))\r\n\t(Client certificate not present)\r\nReturn-Path: noreply@github.com\r\nX-Yandex-Front: mxfront2g.mail.yandex.net\r\nX-Yandex-TimeMark: 1556451156.153\r\nAuthentication-Results: mxfront2g.mail.yandex.net; spf=pass (mxfront2g.mail.yandex.net: domain of github.com designates 192.30.252.194 as permitted sender, rule=[ip4:192.30.252.0/22]) smtp.mail=noreply@github.com; dkim=pass header.i=@github.com\r\nX-Yandex-Spam: 2\r\nX-Yandex-Fwd: OTM4OTM4Mjc2OTU3NTU3NTYyMyw5NzM5MTE2MTc5NzI0MTAxOTMw\r\nDate: Sun, 28 Apr 2019 04:32:35 -0700\r\nDKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed; d=github.com;\r\n\ts=pf2014; t=1556451155;\r\n\tbh=FsRPUKn3beupt2P3QB36UzfVESVClL07TVINnTX0nBg=;\r\n\th=Date:From:Reply-To:To:Cc:Subject:List-ID:List-Archive:List-Post:\r\n\t List-Unsubscribe:From;\r\n\tb=bzfQrv25o0IpZKiIrcGgLzDvM2VLfYficzjqSPPT0Rd3u3D66awwlxaVEHWqpE6dc\r\n\t 8ETR0+A3kN1V3xlo9Etlgn31105g3OQFG0jBMTdymdaXA/hu8Hrjr4Wf1krAGquHpq\r\n\t gJoF4ChuMuUhL554hguAmsWZ1BmzcjH6vVSa0ZEU=\r\nFrom: Buddy Rikard <notifications@github.com>\r\nReply-To: ikvk/imap_tools <reply+AAV6N2Z5ZMVYPVVMJBXEZE522LA5HEVBNHHBUHAPJU@reply.github.com>\r\nTo: ikvk/imap_tools <imap_tools@noreply.github.com>\r\nCc: Subscribed <subscribed@noreply.github.com>\r\nMessage-ID: <ikvk/imap_tools/issues/4@github.com>\r\nSubject: [ikvk/imap_tools] does not extract attached EML files (#4)\r\nMime-Version: 1.0\r\nContent-Type: multipart/alternative;\r\n boundary="--==_mimepart_5cc58f537542_49eb3fba40ccd9603084be";\r\n charset=UTF-8\r\nContent-Transfer-Encoding: 7bit\r\nPrecedence: list\r\nX-GitHub-Sender: TpyoKnig\r\nX-GitHub-Recipient: ikvk\r\nX-GitHub-Reason: subscribed\r\nList-ID: ikvk/imap_tools <imap_tools.ikvk.github.com>\r\nList-Archive: https://github.com/ikvk/imap_tools\r\nList-Post: <mailto:reply+AAV6N2Z5ZMVYPVVMJBXEZE522LA5HEVBNHHBUHAPJU@reply.github.com>\r\nList-Unsubscribe: <mailto:unsub+AAV6N2Z5ZMVYPVVMJBXEZE522LA5HEVBNHHBUHAPJU@reply.github.com>,\r\n <https://github.com/notifications/unsubscribe/AAV6N24RJYGGQBI5PKMGTK3PSWDNHANCNFSM4HI6JQUA>\r\nX-Auto-Response-Suppress: All\r\nX-GitHub-Recipient-Address: KaukinVK@yandex.ru\r\nX-Yandex-Forward: efb42d76edf7d5556112f3dac099406e\r\n\r\n\r\n----==_mimepart_5cc58f537542_49eb3fba40ccd9603084be\r\nContent-Type: text/plain;\r\n charset=UTF-8\r\nContent-Transfer-Encoding: 7bit\r\n\r\nAs .EML files have these headers:\r\n\r\n`--00000000000094809105878daac0\r\nContent-Type: message/rfc822; name="Totally legit email (2).eml"\r\nContent-Disposition: attachment; filename="Totally legit email (2).eml"\r\nContent-Transfer-Encoding: base64\r\nContent-ID: <f_jv0apprb0>\r\nX-Attachment-Id: f_jv0apprb0\r\n\r\nMIME-Version: 1.0\r\nDate: Fri, 25 Jan 2019 10:37:47 -0800\r\nMessage-ID: <CAKKXz3O5qFoTi68Ls4QCqZzQK8m6mASymTZ9ib6ysnBTOwwJOg@mail.gmail.com>\r\nSubject: Totally legit email\r\nFrom: REDACTED <REDACTED@DOMAIN.COM>\r\nTo: REDACTED <REDACTED@DOMAIN.COM>\r\nContent-Type: multipart/alternative; boundary="000000000000a30bb605804c9ff2"\r\n\r\n--000000000000a30bb605804c9ff2\r\nContent-Type: text/plain; charset="UTF-8"\r\nContent-Transfer-Encoding: quoted-printable`\r\n\r\nimap-tools does not return this as an attachment and completely disregards the attachment itself along with the filename. \r\n\r\n-- \r\nYou are receiving this because you are subscribed to this thread.\r\nReply to this email directly or view it on GitHub:\r\nhttps://github.com/ikvk/imap_tools/issues/4\r\n----==_mimepart_5cc58f537542_49eb3fba40ccd9603084be\r\nContent-Type: text/html;\r\n charset=UTF-8\r\nContent-Transfer-Encoding: 7bit\r\n\r\n<p>As .EML files have these headers:</p>\r\n<p>`--00000000000094809105878daac0<br>\r\nContent-Type: message/rfc822; name="Totally legit email (2).eml"<br>\r\nContent-Disposition: attachment; filename="Totally legit email (2).eml"<br>\r\nContent-Transfer-Encoding: base64<br>\r\nContent-ID: &lt;f_jv0apprb0&gt;<br>\r\nX-Attachment-Id: f_jv0apprb0</p>\r\n<p>MIME-Version: 1.0<br>\r\nDate: Fri, 25 Jan 2019 10:37:47 -0800<br>\r\nMessage-ID: <a href="mailto:CAKKXz3O5qFoTi68Ls4QCqZzQK8m6mASymTZ9ib6ysnBTOwwJOg@mail.gmail.com">CAKKXz3O5qFoTi68Ls4QCqZzQK8m6mASymTZ9ib6ysnBTOwwJOg@mail.gmail.com</a><br>\r\nSubject: Totally legit email<br>\r\nFrom: REDACTED <a href="mailto:REDACTED@DOMAIN.COM">REDACTED@DOMAIN.COM</a><br>\r\nTo: REDACTED <a href="mailto:REDACTED@DOMAIN.COM">REDACTED@DOMAIN.COM</a><br>\r\nContent-Type: multipart/alternative; boundary="000000000000a30bb605804c9ff2"</p>\r\n<p>--000000000000a30bb605804c9ff2<br>\r\nContent-Type: text/plain; charset="UTF-8"<br>\r\nContent-Transfer-Encoding: quoted-printable`</p>\r\n<p>imap-tools does not return this as an attachment and completely disregards the attachment itself along with the filename.</p>\r\n\r\n<p style="font-size:small;-webkit-text-size-adjust:none;color:#666;">&mdash;<br />You are receiving this because you are subscribed to this thread.<br />Reply to this email directly, <a href="https://github.com/ikvk/imap_tools/issues/4">view it on GitHub</a>, or <a href="https://github.com/notifications/unsubscribe-auth/AAV6N2ZD2P5MW33322GDAFTPSWDNHANCNFSM4HI6JQUA">mute the thread</a>.<img src="https://github.com/notifications/beacon/AAV6N27JEB4SBCE3VILPO6LPSWDNHANCNFSM4HI6JQUA.gif" height="1" width="1" alt="" /></p>\r\n<script type="application/json" data-scope="inboxmarkup">{"api_version":"1.0","publisher":{"api_key":"05dde50f1d1a384dd78767c55493e4bb","name":"GitHub"},"entity":{"external_key":"github/ikvk/imap_tools","title":"ikvk/imap_tools","subtitle":"GitHub repository","main_image_url":"https://github.githubassets.com/images/email/message_cards/header.png","avatar_image_url":"https://github.githubassets.com/images/email/message_cards/avatar.png","action":{"name":"Open in GitHub","url":"https://github.com/ikvk/imap_tools"}},"updates":{"snippets":[{"icon":"DESCRIPTION","message":"does not extract attached EML files (#4)"}],"action":{"name":"View Issue","url":"https://github.com/ikvk/imap_tools/issues/4"}}}</script>\r\n<script type="application/ld+json">[\r\n{\r\n"@context": "http://schema.org",\r\n"@type": "EmailMessage",\r\n"potentialAction": {\r\n"@type": "ViewAction",\r\n"target": "https://github.com/ikvk/imap_tools/issues/4",\r\n"url": "https://github.com/ikvk/imap_tools/issues/4",\r\n"name": "View Issue"\r\n},\r\n"description": "View this Issue on GitHub",\r\n"publisher": {\r\n"@type": "Organization",\r\n"name": "GitHub",\r\n"url": "https://github.com"\r\n}\r\n}\r\n]</script>\r\n----==_mimepart_5cc58f537542_49eb3fba40ccd9603084be--\r\n'
            ),
        ],
        from_values={'email': 'kaukinvk@yandex.ru', 'name': 'Каукин Владимир',
                     'full': 'Каукин Владимир <kaukinvk@yandex.ru>'},
        to_values=({'email': 'imap.tools@ya.ru', 'name': '', 'full': 'imap.tools@ya.ru'},),
        cc_values=(),
        bcc_values=(),
        reply_to_values=(),
    ),
    'double_fields': dict(
        subject='double_fields',
        from_='kaukinvk@yandex.ru',
        to=('aa@aa.ru', 'bb@aa.ru'),
        cc=('cc@aa.ru', 'dd@aa.ru'),
        bcc=('zz1@aa.ru', 'zz2@aa.ru'),
        reply_to=('foma1@company.ru', 'petr1@company.ru', 'foma2@company.ru', 'petr2@company.ru'),
        date=datetime.datetime(2019, 5, 1, 12, 20),
        date_str='Wed, 01 May 2019 12:20',
        text='',
        html='<div>double_fields</div>',
        headers={'To': ('aa@aa.ru', 'bb@aa.ru', ''),
                 'From': ('=?utf-8?B?0JrQsNGD0LrQuNC9INCS0LvQsNC00LjQvNC40YA=?= <kaukinvk@yandex.ru>',),
                 'Return-Path': ('kaukinvk@yandex.ru',), 'Envelope-From': ('kaukinvk@yandex.ru',),
                 'Date': ('Wed, 01 May 2019 12:20',), 'Subject': ('double_fields',),
                 'Message-Id': ('<8872861556695229@myt5-262fb1897c00.qloud-c.yandex.net>',), 'MIME-Version': ('1.0',),
                 'Content-Type': (
                     'multipart/mixed;\r\n\tboundary="----==--bound.887287.myt5-262fb1897c00.qloud-c.yandex.net"',),
                 'Reply-To': (
                     '=?UTF-8?B?0L/RgNC40LLQtdGC?= <foma1@company.ru>,\r\n =?UTF-8?B?0L/QvtC60LA=?= <petr1@company.ru>',
                     '=?UTF-8?B?0L/RgNC40LLQtdGC?= <foma2@company.ru>,\r\n =?UTF-8?B?0L/QvtC60LA=?= <petr2@company.ru>'),
                 'Bcc': ('zz1@aa.ru', 'zz2@aa.ru'), 'Cc': ('cc@aa.ru', 'dd@aa.ru')},
        attachments=[],
        from_values={'email': 'kaukinvk@yandex.ru', 'name': 'Каукин Владимир',
                     'full': 'Каукин Владимир <kaukinvk@yandex.ru>'},
        to_values=(
            {'email': 'aa@aa.ru', 'name': '', 'full': 'aa@aa.ru'},
            {'email': 'bb@aa.ru', 'name': '', 'full': 'bb@aa.ru'}),
        cc_values=(
            {'email': 'cc@aa.ru', 'name': '', 'full': 'cc@aa.ru'},
            {'email': 'dd@aa.ru', 'name': '', 'full': 'dd@aa.ru'}),
        bcc_values=({'email': 'zz1@aa.ru', 'name': '', 'full': 'zz1@aa.ru'},
                    {'email': 'zz2@aa.ru', 'name': '', 'full': 'zz2@aa.ru'}),
        reply_to_values=({'email': 'foma1@company.ru', 'name': 'привет', 'full': 'привет <foma1@company.ru>'},
                         {'email': 'petr1@company.ru', 'name': 'пока', 'full': 'пока <petr1@company.ru>'},
                         {'email': 'foma2@company.ru', 'name': 'привет', 'full': 'привет <foma2@company.ru>'},
                         {'email': 'petr2@company.ru', 'name': 'пока', 'full': 'пока <petr2@company.ru>'}),
    ),
    'attachment_inline': dict(
        subject='Mail.Ru – больше, чем почта. Познакомьтесь с проектами Mail.Ru Group',
        from_='welcome@corp.mail.ru',
        to=('imap.tools@mail.ru',),
        cc=(),
        bcc=(),
        reply_to=(),
        date=datetime.datetime(1900, 1, 1, 0, 0),
        date_str='',
        text="""Здравствуйте\r\n""",
        html="""<html>\r\n  <head>\r\n    <meta http-equiv="content-type" content="text/html; charset=utf-8">\r\n  </head>\r\n  <body bgcolor="#FFFFFF" text="#000000">\r\n    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">\r\n        \r\n    <div style="line-height:0;font-size:0;"><img\r\n                src="cid:part1.02000503.06000807@mail.ru" alt=""\r\n                style="width:28px;height:1px;" height="1" width="28"></div>\r\n\r\n    <div style="line-height:0;height:25px;" class="mmwe3-mso_lh5"><img\r\n                src="cid:part51.09060808.01070700@mail.ru"\r\n                style="width:125px;height:25px;" alt="@Mail.Ru"\r\n                height="25" width="125"></div>\r\n                \r\n    <div style="line-height:0;height:60px;" class="mmwe3-mso_lh4"><a\r\n                        href="https://www.odnoklassniki.ru/pochtamail"\r\n                        title="Одноклассники"><img\r\n                          src="cid:part41.01020108.09060604@mail.ru"\r\n                          style="width:60px;height:60px;"\r\n                          alt="Одноклассники" height="60" width="60"></a></div>\r\n\r\n  </body>\r\n</html>\r\n""",
        headers={'Content-Type': ('multipart/alternative;\r\n boundary="------------080400030209020702000207"',),
                 'From': ('=?UTF-8?B?0JrQvtC80LDQvdC00LAg0J/QvtGH0YLRiyBNYWlsLlJ1?=\r\n <welcome@corp.mail.ru>',),
                 'MIME-Version': ('1.0',), 'To': ('imap.tools@mail.ru',), 'Subject': (
            '=?UTF-8?B?TWFpbC5SdSDigJMg0LHQvtC70YzRiNC1LCDRh9C10Lwg0L/QvtGH0YLQsC4g?=\r\n =?UTF-8?B?0J/QvtC30L3QsNC60L7QvNGM0YLQtdGB0Ywg0YEg0L/RgNC+0LXQutGC0LA=?=\r\n =?UTF-8?B?0LzQuCBNYWlsLlJ1IEdyb3Vw?=',)},
        attachments=[
            dict(
                filename='blank.png',
                content_id='part1.02000503.06000807@mail.ru',
                content_disposition='inline',
                content_type='image/png',
                payload=b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x08\x00\x00\x00\x08\x01\x00\x00\x00\x00\xect\x83&\x00\x00\x00\x02tRNS\x00\x01\x01\x94\xfd\xae\x00\x00\x00\x0bIDATx\x01c\xfc\x8f\n\x01@\x18\x08\x01\xdez\xda\x08\x00\x00\x00\x00IEND\xaeB`\x82',
            ),
            dict(
                filename='sm-ok.png',
                content_id='part41.01020108.09060604@mail.ru',
                content_disposition='inline',
                content_type='image/png',
                payload=b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00<\x00\x00\x00<\x08\x03\x00\x00\x00\r")@\x00\x00\x00\x19tEXtSoftware\x00Adobe ImageReadyq\xc9e<\x00\x00\x01\xd1PLTE\xffs\x01\xfft\x03\xffu\x06\xff\xf7\xf0\xff\x84!\xff\x93<\xff\xf3\xe9\xff\xfc\xf9\xff\x94>\xff\xde\xc3\xff\xdd\xc1\xff\xf5\xed\xff\xda\xbc\xff\xc8\x9b\xffs\x02\xff\xf8\xf3\xff\xael\xff\x906\xff\xfc\xfa\xff\xef\xe2\xff\xf0\xe3\xff\x8b-\xff\xf4\xec\xff\xa2W\xff\x94=\xff\x81\x1c\xff\xc8\x9c\xff\xeb\xda\xff\xd7\xb7\xfft\x04\xff\xba\x83\xff\xcc\xa2\xff\x9fQ\xff\xd1\xac\xff\xfd\xfb\xff\xfb\xf8\xff\xf6\xef\xff\xd0\xaa\xff\xa3Y\xff\x92:\xffy\x0c\xff{\x10\xff\xbd\x87\xff\xee\xe1\xff\xf3\xea\xffv\x08\xff\xeb\xdb\xff\x9bK\xff\xa2V\xff\xc9\x9d\xff\xc1\x8f\xff\x9cL\xff\xf7\xf1\xff\xfa\xf6\xff\x8f5\xff\xf1\xe6\xff\xee\xe0\xff\xd7\xb6\xff\xc9\x9e\xff\xa3X\xff\xc7\x99\xff\xadj\xffu\x05\xff\x8e3\xff\xadk\xffz\x0f\xff\xa0S\xff{\x11\xff\xdd\xc2\xff\xf8\xf2\xff\x929\xff\xdc\xbf\xff\x93;\xff\x8e2\xff\xdc\xc0\xff\x97C\xff\xcf\xa9\xff\xba\x82\xff\xc7\x9a\xffy\r\xff\x83\x1e\xff\xa4[\xff\xa8b\xff\x8d0\xff|\x12\xff\x88\'\xff\xb7}\xff\xc3\x93\xff\x9fR\xff\xed\xdf\xff\x86%\xff\x96B\xff\x8c/\xff\xd3\xb0\xff\xca\xa0\xff\xa9c\xff\xaci\xff\xe8\xd5\xff\xbf\x8c\xff\xed\xde\xff\xaem\xff\x918\xffv\x07\xff\xbf\x8b\xff\xdb\xbe\xffx\n\xff\xafo\xff\xc3\x92\xff\x95?\xff\xca\x9f\xff\xbd\x88\xff\xc6\x98\xff\x81\x1b\xff\xd6\xb4\xff\x9aH\xff\xec\xdd\xff\xd3\xaf\xff\xd9\xbb\xff\xf9\xf5\xff\x8d1\xff\xf9\xf4\xff\xc5\x96\xff\x907\xff\xf0\xe4\xff\xa9d\xff\xaae\xff\x8a,\xff\xd2\xae\xff\x95@\xff\xfd\xfc\xff\x83\x1f\xff\xd6\xb5\xff\xd8\xb8\xff\xa0T\xff\xc5\x97\xff\xbe\x89\xff\xbe\x8a\xff}\x14\xff\x96A\xff\xa4Z\xffz\x0e\xff\xf6\xee\xff\x84 \xff\xce\xa7\xff\xd4\xb2\xff\x9aI\xff\xcd\xa5\xff}\x13\xff\xf2\xe7\xff\xa1U\xff\x8a+\xff\xbb\x84\xff\xd4\xb1\xffr\x00\xff\xff\xff\xe4\xd8\x99$\x00\x00\x03\xcbIDATx\xda\xac\x97g_\x13A\x10\x877\xb9\x90J\x08\x81P\x12i!\x14)J/J\x17\xa5*\xa0" \x08*J\xb5\xf7\xde{\xefe\xf6\xd3:sg\x80d\xe7\x92X\xe6\r\xfbc\xe6\xc9\xee\xed\xee\xfcgVH\xd6\xb4\x82\xa2\x8e\xdb\xc1\xed\x00\xdb\x83\xfe\x8e\xa2\x02\x8d\x8f\x12\xcc\xff\x02\x8b\x95\x16\x881K\xe5bMJ\xb0\xbb)\x8e\xfc\xcd7\x8d$\x85\x07\xf3\xf5\xd0\x8c\xe1\xcc\x90\xab\xdd\'\xa5\xaf\xdd\x15\xca\x1c\xce\xd0\xff\x99?\x98\x10n;HA\xc2\xd9Y\x1b\x1bU\xdb\xe9\x14\xe49\xd8f\x0e\x97\xf7a\x80\xf5\xf86ns\xb6\x1d\xb7\xa2\xb3\xaf\xdc\x04vd\xd2\x8f\xe7\xd5H\x13\xcb\xee \x7ff\x84\x83\xf7\x8d\xa2\xcb\x96.\x13X\xba\rC\x9c\x1e\x15\xae\xedAGI\x99Lhe3\x18t\xac6\x1e\xd6\x86q\xa3\xce\xcb\xa4v\x1e7\xee\x86\x16\x0b;\xe6\xf0$\x8be\nV\x8c\xb7`\xce\x11\x03w\xe1\xbc\x9d2%\xeb\xc4\xb9\xbb\xb6\xc2\xe5\xf8)\xd52E\xab\xc6\xe0\xfd\x9b\xf0\x9d*\x80\x19\x99\xb2\xed\x01\xa8\nl\xc0%xFZ\xea\xb0\x86\'V\x12\x85Wq\x1d\xe9\xf2\x0f,\xfd7@p\x1a@\x05\x1btr~\xfe$\xeb\xa8\x00H3`7\xc0\x8el5\xc0q\xe6=]G\xdb\x99,\xe6\xa6\xee\x00p\xebp\x13@\xaf\xea\xffZ\x19\xcd\xe4!\xbb\xea\xed\x05h"\xd8^\x08B\xcd\xa3\x96c\x9b:p\xb8Eq\xef\x14PhG\xb8\x11\xb3\\\xfd\xe9)C\x13\x0c\x15\x98R\xfdN\x80F\x84q\xbb\xc6\x14_V?2\xe3\xc5\x91H\xf18\x0e&\xd5\xcf\xf6\xd2\x96\t\xcd\x02B\xfd(7M\xf8\x81F\x9fi\xb4W\t\xb0\x0b\xb0hb\x17@\x8e\xba\xaa\xddH,\xeb\xf3e\x91\x80,\xa8\x119\x00\xbb\xc4\x0f\x80\xd3\xaak\x8c\xf4H\x87\x1d\x04{\xd5\x08\x94\x9d\x03"\x0f $\xf9e\x9f\x8b\xae\x81Y\xb6l@\xc5\x12~\x00\x97\xea*\xfd\x82\xc8\xda\xf3\xe6\xe6[k8x\xf5H\x8dp\x01\xf8E\x10\xe0(s\x01\x0fl\x15\xfc"&\xe0\x14\xc0E\x81\xf5h\x1f\xe3s\xa4m\xb2\xf9\x0e& \x17\x8f\x92\xb4\x9c\xbd\xfb\x9e\xd1(;\xea\xe1\xfc\x0e\xaa\x0ef\xb0,\r}\'\xf4~C\xa94\x81\xad\xb4l\x1f3\xef\xb902\xd9{]\x98n\xa5\xe1\x05\x0f\xbb\xecI~\xc3|\x13\x00\xb3\r:\xe2\t\xcd\x02L\xf8\xb8\r{\xcc\x1f\xd5\x13#-\x8e\x9c={\xc4H\x8d\x02\xfe\xa8\xf0\x92\xecV\xabZ\\\x89.\xdc\xc9]\xe0<Q\xc4^\xcfpp+\x1b\x0c\x9b\\O>1d\xcbtO\x14\xed\x99n\x91&\x89\xc1\xa7$\xd9\x05\x83\x1dc\x9d\x94\x92e\xba\x18x9\xf7G\xab\x01/_\xe2\xbc\x86\x18\x90\x0c9\x19\xefUkt\xd9\xd6\x9f\xd2T\x86H\x00\xd5\xcd\x0c\xeb\xac\xbfU\xa7\x1f\x98\n\xa0\xac\xc3^!\xdeYPHT\xa5\xa6\r\xd0\xdf\xee\xa7\xcc^\xd7m\x88~ \xcey\x99\x984L\xb7\xe6!\x1a}2\x15}\xae\xdc\xd4S\xf3\xa1\xdfI\x1f5f\xf5\xa6\xe5f\xa3nm\xb1\xf6%k\xc7ucx3\xcf\xba\x94\xad\x16\xbak\xff\xa3\xc4\xca\x00\x16\xf7=\x7f[\xdc\xe5\xfe\x7fh+\xa4<\x81\x9a\xe2M\x8d\xf5\xa2\xf8\x9c\x88m\xa5\x1e\xfeI+\xe5\x8cm\xa5d.f\x89x\x91\x9c}\x89\xf3\xe6\xe4\xc6\xb7\x8f\xf6\xc3\xf8)\xcf\x92\xb5\x8f\xdf0(\xc7\xae6\xae\xcd\xaf\xa9\x89p\'b\xdd\xd4\xb8\xe6{\xb8\x969\xd2KR|(`\x86\x06\x0e\x91NwE\x126\xebw\xf9f\xfd\x1e\xe5\xd9\xdb\xf2\x04\xcf\x847\xc63\xc1\x9b\x1b\'\xd2^\xe3\x99P\xd1\x96\xf8\x81b\xd4(K\xeb\xba\xfe@\xc9zw\xc5\xd5\xb0\xee7\xc4th5\xe9\xd3h\xa4.\x83{\x1ae\xd4%\x7f\x1a\x91\xd5\xac\x0c\xc4?\xca\x06VR{\x94E\x9f\x83\xf5\xad\xb6\xfe\xee\xee~[k\xbd\xe9s\xf0\x97\x00\x03\x003\xa2}\xdf\xee~*\xa5\x00\x00\x00\x00IEND\xaeB`\x82',
            ),
            dict(
                filename='logo.png',
                content_id='part51.09060808.01070700@mail.ru',
                content_disposition='inline',
                content_type='image/png',
                payload=b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00}\x00\x00\x00\x19\x08\x03\x00\x00\x00+;\xd1[\x00\x00\x00\x19tEXtSoftware\x00Adobe ImageReadyq\xc9e<\x00\x00\x00fPLTE\xfd\xfd\xfd\xfe\xfe\xfe\xf3\xf3\xf3\xec\xec\xec\xe8\xe8\xe8\xdf\xdf\xdf\xf1\xf1\xf1\xfc\xfc\xfc\xee\xee\xee\xe2\xe2\xe2\xfb\xfb\xfb\xf7\xf7\xf7\xe0\xe0\xe0\xf5\xf5\xf5\xed\xed\xed\xf2\xf2\xf2\xf9\xf9\xf9\xeb\xeb\xeb\xe6\xe6\xe6\xf4\xf4\xf4\xef\xef\xef\xf6\xf6\xf6\xf8\xf8\xf8\xe7\xe7\xe7\xe3\xe3\xe3\xe5\xe5\xe5\xea\xea\xea\xfa\xfa\xfa\xe4\xe4\xe4\xe1\xe1\xe1\xf0\xf0\xf0\xe9\xe9\xe9\xde\xde\xde\xff\xff\xff\xe4X/e\x00\x00\x03-IDATx\xda\xc4\x96\xd9\x96\x83 \x0c\x86\xc5\r\x17\xd4\xba\xef-\xbc\xffKN\x12@mG\xcf\x1c\xe7b\x86\x8b\x9e\x8a$_H~\x82\x8e\xb2\x83\x87\xfe\x10H1L\x85\xa3n\x8e$\x0ej\xa5|\xe9\xdd5\xb4$\xee\x05\xd2\x8e\xc0\xbb\xc9\x0f\xa5\xf4U\x02\x96\xbf\xa4g\x02\xb1b\xa9\x06\nbmo9\xc9\xa4,\xef\xd1\x1fE\xd1m\xf4\'\x12\x9b\x19\xff\xb2v\xc2\x00\xdc{x\x97\xdd\xa3\x870,\xdd\x05\xc3\x12\xff1z5W\xf0\x9c\xe9\x8a\x82\x08:\xd7Mt\xbc.?D_\x17\x19\x980\x17\xf7\x90B\xd9\xcf\xe9`\x0cN\xebc.3p]4Ma\xe83l\xb6\x81\xd2\xe7\xb1\x94C\x84.KH\x05\xc55\xc8q\xc0R\xbc\x9cn$E\xe8\xf8T\x11\x93B\xfc\xd9\x93\xb2S)\xda\x9f\xd0Y\x88\xcbJUHYo\x93\xf4\xe0\xd6\xb5\xa5\xfbRN\xb6\xf4P\xfcl\x899L\xe5\xf8vSblD\xd9\x93X\xfcM\xa0+\x16\xe9BuNOk^\nB\x8c\xb6Y\xfd\x90\xccFu3\x109*GVy\xae\rR\x0eg\x8f\x19\xba\x98\xf4\xe4:\xe1\xf6!d\x86\x95\x11\xfeT\xe9\x08\xae\xe8l\xa4e9?\xa3o\x9a\x8fp\x9f\\HA\xc5y`\xb2R\\\x93i\xfa\x0b\x96@%\xe4\x04\xd1\xf4\xb4\xf9\x06\x9erf\x05rI\xcfa"b\x9f\xc0O:\xb8x\xe0RS\x1aTA\xaaZJ=\xd2QiPX\xe9hy\xc6\xca\x11$\x93m{\x17tH\x9f\x0c\xbf\x03?\xe9\xb0k\xa5bpk\xc6\x84t\x8e\x0e\x89\x8e\xd4\x87\xf1\x9c!\xbd\x06m2\xab\xfck:L\x8e\xeag:8S\x8c\x84\xb7\x99\xa58\xbb\\\xd0\xa3\xa3\xaf\xe1\x92>m[\xff\x81\xbe \xa6<\x1c\x89\x14\xc3\xb9\xa2\x97$=3\xfaK:\xbciw\x05\xbc\xd1\x9b\xb7\xcc\xaf\xf8\xd3\x1f\xd4\x92\xa2\xaf\xea\x82\x9e\x1f\xcc\xd5rI\xaf(\x85\xb6\x95n{S\xafC\xf0\xe0\x1b\x94\x93\xc0\\`\x1a\x99\xb3\xa2YM\x06\xa7tw/(!\r\xdd*\xf4\x84\x0e\x12\x8e\xadRP\xb3\xdd\xfb\x89\x0bU\x07g\x89\x160\x9fN\x9cN\xef)\xdd\t\xf6\xd6\xf5\xda\xe9j\xdd\x0b\xfdAg\xfb)\xc1\xc4\xc7\xc7;\xae#\rC\x0c\x8b;\xcf\xeeb\xbb\r\xe6\xe2\x94\x8e\xa9\x0f\x08\xcf\xbc\xc3yG\xbfA{J\xa7[\xac\xc1\xcd\xb1H\x1eU\x83\xbeG\x8a\xcc\xb3\xdd\x136\x1f\xe9\xe6{Ag\x18\xe1\xd8\x84\xdez\xecu\xd8\xb0 \x81y\x8a\xe1U\xec\x8dN\xdd1\xceC\x0f[\x99\xff~\xbfw\xfaFm\xb1u\xc81c\xd4\xd2\x05\xbf\xa4\xabd\x90\x87a\xe9\xaa%C\xc8\x99\xc0\xfeu\xa4+\xa7\xda\x96\xf7\xce\xc7\xd7Ecz"OSdbv\x84\xb6\x142`Z\\B\xe98\x17\xb22\x89\x8a\xdd\t\xcfUm4\xddQ\xd98\xb4.\xd21\x84\xb07\xfdF_S\xe2\xc9\xbe}\xdb`\x1f\x8f\x9f\xa4X\x96>TV\xe6\x89~\x9d\x96\xba\x92\x99\xa7u\xeaz\xc6#/\xf22j\x19|\x91\xa1\xd2\x9e\xb9Q{\x1b\x955ZA*\x13\xafx\xbf\xf1j\xb0\xa8\xd9\xd9\x97\xd5\x93"\x1bz\xbf\n\xb6\xa3\xf7\x07\xc3\x16a\xf6\xf7\x8f\xca\xbf\xa7C\xa6\x9e>\xd4+\x18\xca\x87\xfa\x07\xfa\x7f\x8c/\x01\x06\x00\xcc\x9eX\xf3u\xe2\x94\xf6\x00\x00\x00\x00IEND\xaeB`\x82',
            ),
        ],
        from_values={'email': 'welcome@corp.mail.ru', 'name': 'Команда Почты Mail.Ru',
                     'full': 'Команда Почты Mail.Ru <welcome@corp.mail.ru>'},
        to_values=({'email': 'imap.tools@mail.ru', 'name': '', 'full': 'imap.tools@mail.ru'},),
        cc_values=(),
        bcc_values=(),
        reply_to_values=(),
    ),
}
