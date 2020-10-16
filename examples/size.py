from imap_tools import MailBox

# get size of message and attachments
with MailBox('imap.my.ru').login('acc', 'pwd', 'INBOX') as mailbox:
    for msg in mailbox.fetch():
        print(msg.date_str, msg.subject)
        print('-- RFC822.SIZE message size', msg.size)
        print('-- bytes size', len(bytes(msg.obj)))
        print('-- str size', len(str(msg.obj)))
        for att in msg.attachments:
            print('---- ATT:', att.filename)
            print('---- bytes size', len(bytes(att.part)))
            print('---- str size', len(str(att.part)))

# NOTE:
# len(bytes(msg.obj)) method will returns headers size only when fetch headers_only=True
