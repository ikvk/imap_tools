from imap_tools import MailBox, MailMessage

# parse .eml files attached to email messages
with MailBox('imap.mail.com').login('test@mail.com', 'password') as mailbox:
    for message in mailbox.fetch():
        for att in message.attachments:
            if '.eml' in att.filename:
                print(att.filename)
                eml_email = MailMessage.from_bytes(att.payload)
                print('- subject: ', eml_email.subject)
                print('- date_str: ', eml_email.date_str)

# parse .eml files from attached .eml files (2 levels of nesting)
with open('/tmp/1.eml', 'rb') as f:
    bytes_data = f.read()
msg = MailMessage.from_bytes(bytes_data)
for att in msg.attachments:
    if '.eml' in att.filename:
        # 1 level .eml
        msg_level_1 = MailMessage.from_bytes(att.payload)
        print(att.filename)
        print('* subject: ', msg_level_1.subject)
        print('* date: ', msg_level_1.date)
        for att_sub in msg_level_1.attachments:
            if '.eml' in att_sub.filename:
                # 2 level .eml
                msg_level_2 = MailMessage.from_bytes(att_sub.payload)
                print('|--', att_sub.filename)
                print('|   * subject: ', msg_level_2.subject)
                print('|   * date: ', msg_level_2.date)
