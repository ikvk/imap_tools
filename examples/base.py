from imap_tools import MailBox
import configparser

# get config data
config = configparser.ConfigParser()
config.read('../credentials.ini')

# get email box
mailbox = MailBox(config['YANDEX']['host'])
mailbox.login(config['YANDEX']['email'], config['YANDEX']['password'])

# MESSAGES
# --------
for message in mailbox.fetch():
    print(message.id)
    print(message.uid)
    print(message.subject)
    print(message.from_)
    print(message.to)
    print(message.date)
    print(message.text)
    print(message.html)
    print(message.flags)
    for filename, payload in message.attachments:
        print(filename, payload)

# MAILBOX
# -------
# NOTE: You can use 2 approaches to perform these operations
# "by one" - Perform operation for each message separately per N commands
# "in bulk" - Perform operation for message set per 1 command

# COPY all messages from current dir to folder1, *by one
for msg in mailbox.fetch():
    res = mailbox.copy(msg.uid, 'INBOX/folder1')
# DELETE all messages from current dir to folder1, *in bulk
mailbox.delete([msg.uid for msg in mailbox.fetch()])
# FLAG unseen messages in current folder as Answered and Flagged, *in bulk
mailbox.flag([msg.uid for msg in mailbox.fetch('(UNSEEN)')], ['Answered', 'Flagged'], True)
# MOVE all messages from current dir to folder2, *in bulk
mailbox.move([msg.uid for msg in mailbox.fetch()], 'INBOX/folder2')
# mark SEEN all messages sent at 05.03.2007 in current folder as unseen, *in bulk
mailbox.seen([msg.uid for msg in mailbox.fetch("SENTON 05-Mar-2007")], False)

# FOLDERS
# -------
# LIST
for folder in mailbox.folder.list('INBOX'):
    print(folder['flags'], folder['delim'], folder['name'])
# SET
mailbox.folder.set('INBOX')
# GET
current_folder = mailbox.folder.get()
# CREATE
mailbox.folder.create('folder1')
# EXISTS
is_exists = mailbox.folder.exists('folder1')
# RENAME
mailbox.folder.rename('folder1', 'folder2')
# DELETE
mailbox.folder.delete('folder2')
# STATUS
for status_key, status_val in mailbox.folder.status('some_folder').items():
    print(status_key, status_val)
