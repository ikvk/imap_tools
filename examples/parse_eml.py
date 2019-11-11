from imap_tools import MailBox, MailMessage

# parse .eml files attached to email messages
with MailBox('imap.mail.com').login('test@mail.com', 'password') as mailbox:
    for message in mailbox.fetch():
        for filename, payload in message.attachments:
            if '.eml' in filename:
                print(filename)
                eml_email = MailMessage.from_bytes(payload)
                print('- subject: ', eml_email.subject)
                print('- date_str: ', eml_email.date_str)
