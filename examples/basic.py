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
    First searches email nums by criteria in current folder, then fetch and yields MailMessage
    criteria arg = 'ALL' by default
    Current folder is 'INBOX' (set on login)
    Fetch each message separately per N commands, cause bulk arg = False by default
    Mark each fetched email as seen, cause fetch mark_seen arg = True by default
    
4. print
    msg variable is MailMessage instance
    msg.date - email data, converted to datetime.date
    msg.subject - email subject, utf8 str
    msg.text - email plain text content, utf8 str
    msg.html - email html content, utf8 str
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
