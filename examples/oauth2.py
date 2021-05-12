from imap_tools import MailBox

# Authenticate to account using OAuth 2.0 mechanism
with MailBox('imap.my.ru').xoauth2('user', 'token123', 'INBOX') as mailbox:
    for msg in mailbox.fetch():
        print(msg.date_str, msg.subject)
