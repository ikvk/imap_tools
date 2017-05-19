from main import MailBox
import configparser

# get config data
config = configparser.ConfigParser()
config.read('../passwords.ini')

# get email box
email = 'imap.tools@ya.ru'
box = MailBox('imap.yandex.ru')
box.login(email, config['PASSWORDS'][email])


def email_data():
    for message in box.fetch():
        print('id:', message.id)
        print('uid:', message.uid)
        print('subject:', message.subject)
        print('from_:', message.from_)
        print('to:', message.to)
        print('date:', message.date)
        print('text:', 'length {}'.format(len(message.text)) if message.text else '<no text>')
        print('html:', 'length {}'.format(len(message.html)) if message.html else '<no html>')
        print()


def folder_list():
    for folder in box.folder.list('INBOX', subscribed_only=not True):
        print(folder['name'])


def folder_status():
    res = box.folder.status('INBOX')
    print(res)


email_data()
folder_list()
folder_status()

folder = 'test'
new_folder = folder + '1'
print('get: ', box.folder.get())
print('create: ', box.folder.create(folder))
print('exists: ', box.folder.exists(folder))
print('rename: ', box.folder.rename(folder, new_folder))
print('delete: ', box.folder.delete(new_folder))

"""
mailbox = MailBox('imap.mail.com')
mailbox.login('test@mail.com', 'password')

# COPY all messages from current dir to folder1, by one
for msg in mailbox.fetch():
    res = mailbox.copy(msg.uid, 'INBOX/folder1')

# DELETE all messages from current dir to folder1, in bulk
mailbox.delete([msg.uid for msg in mailbox.fetch()])

# FLAG unseen messages in current folder as Answered and Flagged, in bulk
mailbox.flag([msg.uid for msg in mailbox.fetch('(UNSEEN)')], ['Answered', 'Flagged'], True)

# MOVE all messages from current dir to folder2, in bulk
mailbox.move([msg.uid for msg in mailbox.fetch()], 'INBOX/folder2')

# mark SEEN all messages sent at 05.03.2007 in current folder as unseen, in bulk
mailbox.seen([msg.uid for msg in mailbox.fetch("SENTON 05-Mar-2007")], False)

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
"""