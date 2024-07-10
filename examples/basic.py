from imap_tools import MailBox, AND

"""
Get date, subject and body len of all emails from INBOX folder

1. MailBox()
    Create IMAP client, the socket is created here
    
2. mailbox.login()
    Login to mailbox account
    It supports context manager, so you do not need to call logout() in this example
    Select INBOX folder, cause login initial_folder arg = 'INBOX' by default (set folder may be disabled with None)
    
3. mailbox.fetch()
    First searches email uids by criteria in current folder, then fetch and yields MailMessage
    Criteria arg is 'ALL' by default
    Current folder is 'INBOX' (set on login), by default it is INBOX too.
    Fetch each message separately per N commands, cause bulk arg = False by default
    Mark each fetched email as seen, cause fetch mark_seen arg = True by default
    
4. print
    msg variable is MailMessage instance
    msg.date - email data, converted to datetime.date
    msg.subject - email subject, utf8 str
    msg.text - email plain text content, utf8 str
    msg.html - email html content, utf8 str
    
Mailbox classes:
    MailBox - for a normal encrypted connection. This is what most email servers use these days, aka IMAPS (imap with SSL/TLS)
    MailBoxTls - For a STARTTLS connection: this creates a plaintext connection then upgrades
        it later by using a STARTTLS command in the protocol. The internet has mostly gone to the "always encrypted"
        rather than "upgrade" paradigm, so this is not the class to use.
    MailBoxUnencrypted - Standard IMAP without SSL/TLS. You should not use this on the public internet.
    
    MailBox corresponds to imaplib.IMAP4_SSL;
    MailBoxTls corresponds to imaplib.IMAP4, then using startls() on the resulting connection;
    MailboxUnencrypted corresponds to imaplib.IMAP4 with no security applied.
"""
with MailBox('imap.mail.com').login('test@mail.com', 'pwd') as mailbox:
    for msg in mailbox.fetch():
        print(msg.date, msg.subject, len(msg.text or msg.html))

# Equivalent verbose version:
mailbox = MailBox('imap.mail.com')
mailbox.login('test@mail.com', 'pwd', 'INBOX') # or use mailbox.folder.set instead initial_folder arg
for msg in mailbox.fetch(AND(all=True)):
    print(msg.date, msg.subject, len(msg.text or msg.html))
mailbox.logout()
