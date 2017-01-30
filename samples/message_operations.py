import os
from main import MailBox

box = MailBox('imap.yandex.ru')

# 1. move 100 messages as group, from folder1 to folder2
box.login('some@mail.ru', 'passwd', 'folder1')
uid_list = []
for message in box.fetch(limit=100):
    uid_list.append(message.uid)
res = box.move(uid_list, 'folder2')

# 2. copy ALL messages by one, from INBOX to folder2
box.login('some@mail.ru', 'passwd')
for message in box.fetch():
    res = box.copy(uid_list, 'folder2')
    print(res)

# 3. get some data of ALL messages in _back folder
box.login('some@mail.ru', 'passwd', '_back')
for message in box.fetch():
    print(message.subject)
    print(message.from_)
    print(message.to)
    print(message.date)
    print(message.text)
    print(message.html)

# 4. mark all messages sent at 05.03.2007 in folder _back as unseen
box.login('some@mail.ru', 'passwd', '_back')
res = box.seen([message.uid for message in box.fetch("SENTON 05-Mar-2007")], False)
print(res)

# 5. mark all messages in folder _test as Answered and Flagged
box.login('some@mail.ru', 'passwd', '_test')
res = box.flag([message.uid for message in box.fetch()], ['Answered', 'Flagged'], True)
print(res)

# 6. write all message attachments from UNDEFINED folder to local folder
box.login('some@mail.ru', 'passwd', 'UNDEFINED')
for i, message in enumerate(box.fetch()):
    for filename, payload in message.get_attachments():
        with open(os.path.join('C:/kvk/загрузки/1/', '{}_{}'.format(i, filename)), 'wb') as f: f.write(payload)
