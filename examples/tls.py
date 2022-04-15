"""

If you want to use really secure connection, you MUST read this articles:

https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4_SSL
https://docs.python.org/3/library/ssl.html#ssl-security

"""

import ssl

from imap_tools import MailBoxTls

ssl_context = ssl.create_default_context()
ssl_context.load_cert_chain(certfile="./one.crt", keyfile="./one.key")
with MailBoxTls('imap.my.ru', ssl_context=ssl_context).login('acc', 'pwd', 'INBOX') as mailbox:
    for msg in mailbox.fetch():
        print(msg.subject, msg.date_str)
