import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='Contact email-test.fr',
    from_='ne-pas-repondre@email-test.fr',
    to=('service.courrier@mairie-email-test.fr',),
    cc=(),
    bcc=(),
    reply_to=('emmanuellehelou@orange.fr',),
    date=datetime.datetime(2021, 1, 17, 16, 26, 56, tzinfo=datetime.timezone.utc),
    date_str='Sun, 17 Jan 2021 16:26:56 +0000',
    text="Bonjour.\n\nUne nouvelle demande vous a été transmise via le formulaire de contact du site www.saintnazaire.fr\n\nVotre message : onjour,\n\nJe voulais vous alerter que le pizzaïolo du camion ambulant PASTA PIZZA de Villès Martin du dimanche ne porte pas de masques pour confectionner ses pizzas et pour parler à ses clients; pas de gel hydroalcooloique non plus; travaillant dans les hôpitaux je suis consternée de voir encore des professionnels et en contact avec un public de ne pas respecter le port du masque; il contamine ses produits, les clients ...\nCe n'est pas normal de ne pas contrôler ces professionnels ambulants.\n\nMerci beaucoup\n\n\n\nMerci.\n",
    html='',
    headers={'from': ('email-test.fr <ne-pas-repondre@email-test.fr>',), 'to': ('Courrier <service.courrier@mairie-email-test.fr>',), 'subject': ('Contact email-test.fr',), 'thread-topic': ('Contact email-test.fr',), 'thread-index': ('AQHW7O2SJAZxCkqG10awu/NtCY1I/A==',), 'date': ('Sun, 17 Jan 2021 16:26:56 +0000',), 'message-id': ('<c831ea72834dd8fcc648dac294e810fb@www.email-test.fr>',), 'reply-to': ('HELOU <emmanuellehelou@orange.fr>',), 'content-language': ('fr-FR',), 'x-ms-exchange-organization-authas': ('Anonymous',), 'x-ms-exchange-organization-authsource': ('serv-exchange.mairie-email-test.fr',), 'x-ms-has-attach': ('',), 'x-ms-exchange-organization-network-message-id': ('b33ffe95-382f-49d7-269d-08d8bb04b512',), 'x-ms-tnef-correlator': ('',), 'x-ms-exchange-organization-recordreviewcfmtype': ('0',), 'x-ms-exchange-organization-originalclientipaddress': ('192.168.2.8',), 'x-ms-exchange-organization-originalserveripaddress': ('172.16.0.199',), 'x-mailer': ('TYPO3',), 'dkim-signature': ('v=1; a=rsa-sha256; c=simple/simple; d=email-test.fr;\ts=dkim;\r\n t=1610900816;\tbh=OW4RY4SudtC3hIBJtmsQXcuoAP02QMZsI0y7sCUVX00=;\r\n\th=Date:Subject:From:Reply-To:To:From;\r\n\tb=sPHozdsx6imqijuc+XCa9szrzsigwwFKERJ1KeO0L6Omm0gL+a4+F2/I3BePWKn5Y\r\n\t Y9Kott89Zop2kx/mnnGObQ9wY7RevYce9Ke5YXyXBzkyqzhlKsgzXKsJtB2XZcWoXH\r\n\t WtNyyhiD1w84rIHmCosuKrhrFFI50+ZihXxXhxek=',), 'content-type': ('text/plain; charset="utf-8"',), 'content-id': ('<8DEF3B2930D4004EB38802D09A7F5EDE@mairie-email-test.fr>',), 'content-transfer-encoding': ('base64',), 'mime-version': ('1.0',)},
    attachments=[
        dict(
            filename='',
            content_id='8DEF3B2930D4004EB38802D09A7F5EDE@mairie-email-test.fr',
            content_disposition='',
            content_type='text/plain',
            payload=b"Bonjour.\n\nUne nouvelle demande vous a \xc3\xa9t\xc3\xa9 transmise via le formulaire de contact du site www.saintnazaire.fr\n\nVotre message : onjour,\n\nJe voulais vous alerter que le pizza\xc3\xafolo du camion ambulant PASTA PIZZA de Vill\xc3\xa8s Martin du dimanche ne porte pas de masques pour confectionner ses pizzas et pour parler \xc3\xa0 ses clients; pas de gel hydroalcooloique non plus; travaillant dans les h\xc3\xb4pitaux je suis constern\xc3\xa9e de voir encore des professionnels et en contact avec un public de ne pas respecter le port du masque; il contamine ses produits, les clients ...\nCe n'est pas normal de ne pas contr\xc3\xb4ler ces professionnels ambulants.\n\nMerci beaucoup\n\n\n\nMerci.\n",
        ),
        ],
    from_values=EmailAddress(name='email-test.fr', email='ne-pas-repondre@email-test.fr'),
    to_values=(EmailAddress(name='Courrier', email='service.courrier@mairie-email-test.fr'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(EmailAddress(name='HELOU', email='emmanuellehelou@orange.fr'),),
)