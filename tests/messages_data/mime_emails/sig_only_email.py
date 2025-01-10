import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='Re: Testing multipart/signed',
    from_='test@test.lindsaar.net',
    to=('mikel@test.lindsaar.net',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2007, 6, 4, 15, 1, 31, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=61200))),
    date_str='Mon, 4 Jun 2007 15:01:31 -0700',
    text='This is random text, not what has been signed below, ie, this sig\r\nemail is not signed correctly.\r\n',
    html='',
    headers={'date': ('Mon, 4 Jun 2007 15:01:31 -0700',), 'from': ('Test <test@test.lindsaar.net>',), 'to': ('Mikel <mikel@test.lindsaar.net>',), 'subject': ('Re: Testing multipart/signed',), 'message-id': ('<20070604150131.40d4fa1e@reforged>',), 'mime-version': ('1.0',), 'content-type': ('multipart/signed; boundary=Sig_2GIY2xfzqSADMmu9sKGJqWm;\r\n protocol="application/pgp-signature"; micalg=PGP-SHA1',)},
    attachments=[
        dict(
            filename='signature.asc',
            content_id='',
            content_disposition='attachment',
            content_type='application/pgp-signature',
            payload=b'-----BEGIN PGP SIGNATURE-----\r\nVersion: GnuPG v1.4.6 (GNU/Linux)\r\n\r\niD8DB1111Iu7dfRchrkBInkRArniAKCue17JOxXBiAZHwLy3uFacU+pmhwCgwzhf\r\nV5YSPv2xmYOA6mJ6oVaasseQ=\r\n=T7p9\r\n-----END PGP SIGNATURE-----\r\n',
        ),
        ],
    from_values=EmailAddress(name='Test', email='test@test.lindsaar.net'),
    to_values=(EmailAddress(name='Mikel', email='mikel@test.lindsaar.net'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)