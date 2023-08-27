"""How to use keyword criteria"""

from imap_tools import A, MailBox

with MailBox('imap.wow.ru').xoauth2('imap.tools', '123') as mailbox:
    uids = ['183']
    # get messages by uid
    for msg in mailbox.fetch(A(uid=uids)):
        print(msg.uid, msg.subject)
    # add custom flag
    mailbox.flag(uids, ['flag1'], True)
    # get messages by custom flag
    for msg in mailbox.fetch(A(keyword='flag1')):
        print(msg.uid, msg.subject, msg.flags)
