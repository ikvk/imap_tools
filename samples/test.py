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
        print('text:', len(message.text or ''))
        print('html:', len(message.html or ''))
        print()


def folder_list():
    for folder in box.folder.list('inbox/1 привет', subscribed_only=not True):
        print(folder['name'])


def folder_status():
    res = box.folder.status('inbox')
    print(res)

# email_data()
# folder_list()
folder_status()
