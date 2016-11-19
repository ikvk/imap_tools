from main import MailBox

# 1. move 100 messages as group, from test2 to test3
box = MailBox('imap.company.ru', 'i.user', '123', 'test2')
uid_list = []
for message in box.get_mails(limit=100):
    uid_list.append(message.uid)
res = box.move(uid_list, 'test3')

# 2. copy ALL messages by one, from INBOX to test3
box = MailBox('imap.company.ru', 'i.user', '123')
for message in box.get_mails():
    res = box.copy(uid_list, 'test3')

# 3. get some data of ALL messages in _back folder
box = MailBox('imap.company.ru', 'i.user', '123', '_back')
for message in box.get_mails():
    print(message.subject)
    print(message.from_)
    print(message.to)
    print(message.date)
    print(message.text)
    print(message.html)

# 4. mark all messages sent at 05.03.2007 in folder _back as unseen
box = MailBox('imap.company.ru', 'i.user', '123', '_back')
res = box.seen([message.uid for message in box.get_mails("SENTON 05-Mar-2007")], False)

# 5. mark all messages in folder _test as Answered and Flagged
box = MailBox('imap.company.ru', 'i.user', '123', '_test')
res = box.flag([message.uid for message in box.get_mails()], ['Answered', 'Flagged'], True)

# 6. write all message attachments from UNDEFINED folder to local folder
box = MailBox('imap.company.ru', 'i.user', '123', 'UNDEFINED')
for i, message in enumerate(box.get_mails()):
    for filename, payload in message.get_attachments():
        with open(os.path.join('C:/kvk/загрузки/1/', '{}_{}'.format(i, filename)), 'wb') as f: f.write(payload)