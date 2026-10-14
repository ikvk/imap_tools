import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='enveloped ',
    from_='Alice@example.com',
    to=('Bob@example.com',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2023, 11, 21, 20, 50, 6, tzinfo=datetime.timezone.utc),
    date_str='Tue, 21 Nov 2023 20:50:06 +0000',
    text='',
    html='',
    headers={'x-info': ('Based on alice.dsig.SHA256.multipart.env.eml',), 'mime-version': ('1.0',), 'date': ('Tue, 21 Nov 2023 20:50:06 +0000',), 'from': ('Alice@example.com',), 'to': ('Bob@example.com',), 'subject': ('enveloped ',), 'content-type': ('multipart/signed; micalg=pgp-sha256;\r\n protocol="application/pgp-signature";\r\n boundary="------------rvEyIV4on03ewe0w3mDNOC3U"',)},
    attachments=[
        dict(
            filename='smime.p7m',
            content_id='',
            content_disposition='attachment',
            content_type='application/pkcs7-mime',
            payload=b'0\x80\x06\t*\x86H\x86\xf7\r\x01\x07\x03\xa0\x800\x80\x02\x01\x001\x82\x01\x850\x82\x01\x81\x02\x01\x000i0d1\x0b0\t\x06\x03U\x04\x06\x13\x02US1\x130\x11\x06\x03U\x04\x08\x13\nCalifornia1\x160\x14\x06\x03U\x04\x07\x13\rMountain View1\x120\x10\x06\x03U\x04\n\x13\tBOGUS NSS1\x140\x12\x06\x03U\x04\x03\x13\x0bNSS Test CA\x02\x01(0\r\x06\t*\x86H\x86\xf7\r\x01\x01\x01\x05\x00\x04\x82\x01\x00\xb0"\x94v&A\x8fR\xfc}\x8c?BY\x90r\xf1\xaaPl\x879\xa4iW\x82\x9b\xcck\x84\x94\xa3R\xa2\xcdcgho\xce=\x03\xcf\xecc+-Ti.\xad\xab\xeeT\x0b\xf9\x1d\x01\x93\x99\r\'\xb4N\xd5\x94\xe2i\x04\x1f\xa7*\xc4VP\x06|\x92\xbe\x07\x84\x02e\x1ba\xa2\xac\xec\nm\t\xcd\xac\xbf\xdfx\x1f\x80\xa2\xd4\x13&\xa1\x1c*\xdcT\xb1\'\xe4\xf6\xd3\x01\xa7a\x08\x87\xf84Y\xa5~\x8c\xe7\x08\x8cDYru<\x10\xaa\x7f\xcc\x13t>@\xb2\x91c\xff\xdf2JiW\x0fh\x7f\xf8\xcaZ\xd1]\xe6\xdc\t\xb9Sd\xe8J\xf5\xb2\xee\n\xcc\x9e:\xb1C\xaf\xb5\xdcZ\xcc\xcbW_\x9bI.U\xb6zN\xdc\xc89\xf3\xbd\xb43,\xcdC\xfa\xc7\x1ct\x8c\x97\xb2\xe8\x1b\xb5v#\x06\xf1\x06\xc3>F\x90N]\xab^N\xdf\xbb\xd2\xd9\xa1b/\x88\xa56\x17\x91\x9a\x96\xc7\t\xdf\xc1\xc0\x81\x15L\xed\xe9R\xbf\x04P\xf7A\x8e\x12\xc8\xd10\x80\x06\t*\x86H\x86\xf7\r\x01\x07\x010\x1d\x06\t`\x86H\x01e\x03\x04\x01\x02\x04\x10\x98\x88\x1aA\xc7\xaa_J\xab xZgIE\xa1\xa0\x80\x04\x81\xa0\x88\xf6^\x0c\x1b\xda\xce\x1d\x05bv\x8d]\xc4\x9b?\xd9\x15\x03\x0e\xb7\xda_s\x89\x1c\x82\x17\xb5\xa0\xb4\xe0\xc8\xed\xc7\xf6d\xd5\x19\xfd\x00Oa\x1a>\x9a\xbe\'\xb0\xc1\xe5\x16\xa0\xd5\xedn\x19\xe5\xb6b\x11\xc4\xa6\x9fM{\x13\x8e\x0c\xbf\x1e\xec\xc2vp\x84\xee\xc2Y,\x8f\x89\xf6j\x9cp\xe3\xccS\x0f{!\xafr\xc2\x9c2Q\x01\x05M\x93\x08^\x96\xa6\xcc\xe8\'\xa6\x9d\xac\xa1\xccnv\x89\xff1ZE\xe4\x7f\x99\x91\x08^\xd3\xe8bA\x1f\x1bf\xaa\x8e@\\\x00&\xa5\x989\xbb\xc3\r\xa4\x1e1\x1b\xecE\xe6\xf5V\x95\xe5#\xe2R\x04\x10\xcb2-\xf8\x9e`\xa9\xfe\x16\x8b`\xa3P\xdc(\x15\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
        ),
        
        dict(
            filename='OpenPGP_signature',
            content_id='',
            content_disposition='attachment',
            content_type='application/pgp-signature',
            payload=b'-----BEGIN PGP SIGNATURE-----\r\n\r\niQIzBAABCAAdFiEEuPL29L060/gtxEaDMJn/EjiFK58FAmObNeAACgkQMJn/EjiF\r\nK58aPQ/+OYoMsHjVrAHhxKZ4HiK9hz+rt5mbI9udUx0krf0/QRug6Lz+zw4SLfjM\r\njHRCHCBImTWB9LooIKQvFngM1Y9f2sA8i5xRLWR326ZJgDNkiUMpRokpzNCH7Xf3\r\nybdFpKJTFEqMIEfuNiWWKbwla+O2ZwvfE60b2QnSRq/ICbqZfzvGNpbVOHfyuKWn\r\ngd/fyWqDBFmRx6+PJuuP6GmZH7h4wnkHDF7faem+ZgW4qZbly53s80H5tsQ2Bydi\r\nBCk00eqbNPJqUNqFgYH91ANfn9qZPD9o3mydCIyPcRnR/3QIQa35ZgM7AWApBdPc\r\nuOIdNkoVCDSFQZUuuPtrK+Me9dohxzdQ656pI/Z1NIO8hAUOG5tWM857RXGHrIxA\r\n7LKYd5nm2m95I0xOsL3KqnZkonqH6XTuUucUt1oKO5x8yjJnedlYhazolaCARB9R\r\nYSALXbJkDEs52M4B0NTQq6i/mD8pO644wKuxqD8es3CaRkKREPphxzcWWCjo19ex\r\n7e8N0P6cAg6RfNql82OLgBGiQ2UvZSY73kwbNAZ3ZKORleRNE9kjOvGIixxhVoG2\r\nvszvZbdDo4NtQD4BcXtR6faAnSiOCW5RRNN39NGcQMXVZf1DY2ryo6rD7B2HQThI\r\nKkbOWzlJ9sYt5g8khTUxNipmnNe9kMyim8VpKdMnOV8TxBHb0r4=\r\n=b2z0\r\n-----END PGP SIGNATURE-----\r\n',
        ),
        ],
    from_values=EmailAddress(name='', email='Alice@example.com'),
    to_values=(EmailAddress(name='', email='Bob@example.com'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)