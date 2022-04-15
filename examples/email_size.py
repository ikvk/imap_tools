from imap_tools import MailBox

# get size of message and attachments
with MailBox('imap.my.ru').login('acc', 'pwd', 'INBOX') as mailbox:
    for msg in mailbox.fetch():
        print(msg.date_str, msg.subject)
        print('-- RFC822.SIZE message size', msg.size_rfc822)
        print('-- bytes size', msg.size)  # will returns headers size only when fetch headers_only=True
        for att in msg.attachments:
            print('---- ATT:', att.filename)
            print('-- bytes size', att.size)
