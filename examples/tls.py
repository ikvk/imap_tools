import ssl
from imap_tools import MailBox

sc = ssl.create_default_context()
with MailBox('imap.my.ru', ssl_context=sc, starttls=True).login('acc', 'pwd', 'INBOX') as mailbox:
    for msg in mailbox.fetch():
        print(msg.subject, msg.date_str)
