from imap_tools import MailBox

# get all attachments from INBOX and save them to files
with MailBox('imap.my.ru').login('acc', 'pwd', 'INBOX') as mailbox:
    for msg in mailbox.fetch():
        for name, payload in msg.attachments:
            with open('C:/1/{}'.format(name), 'wb') as f:
                f.write(payload)
