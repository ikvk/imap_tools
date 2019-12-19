from imap_tools import MailBox

# get all attachments from INBOX and save them to files
with MailBox('imap.my.ru').login('acc', 'pwd', 'INBOX') as mailbox:
    for msg in mailbox.fetch():
        for att in msg.attachments:
            print(att.filename, att.content_type)
            with open('C:/1/{}'.format(att.filename), 'wb') as f:
                f.write(att.payload)
