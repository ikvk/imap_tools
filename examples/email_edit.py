"""
Email modification is not common case operation
Most likely it will not be added to lib

Also, I have tried to add public attribute - MailMessage.orig_bytes (raw_message_data)
But it have increased memory consumption: ~10%
"""

import email
from imap_tools import MailBox, A

with MailBox('imap.mail.com').login('test@mail.com', 'password') as mailbox:
    for msg in mailbox.fetch(A(subject='[some]')):
        altered_msg = email.message_from_bytes(msg.obj.as_bytes())
        altered_msg.replace_header('Subject', '[my own subject extension] ' + msg.subject)
        mailbox.append(altered_msg.as_bytes())
