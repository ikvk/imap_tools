import ssl

from imap_tools import MailBox

ssl_context = ssl.create_default_context()
ssl_context.load_cert_chain(certfile="./one.crt", keyfile="./one.key")
with MailBox('imap.my.ru', ssl_context=ssl_context, starttls=True).login('acc', 'pwd', 'INBOX') as mailbox:
    for msg in mailbox.fetch():
        print(msg.subject, msg.date_str)
