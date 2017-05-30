import os
import unittest
import configparser
from imap_tools import MailBox

test_mailbox_name_set = {'YANDEX', }


def get_test_mailbox_config(mailbox_name: str) -> dict:
    config = configparser.ConfigParser()
    for config_path in (r'..\tests\credentials.ini', r'tests\credentials.ini'):
        if not os.path.exists(config_path):
            continue
        config.read(config_path)
        return dict(
            host=config[mailbox_name]['host'],
            email=config[mailbox_name]['email'],
            password=config[mailbox_name]['password'],
        )


def get_test_mailbox(mailbox_name: str):
    config = get_test_mailbox_config(mailbox_name)
    mailbox = MailBox(config['host'])
    mailbox.login(config['email'], config['password'])
    return mailbox


class MailboxTestCase(unittest.TestCase):
    def setUp(self):
        self.mailbox_set = dict()
        for test_mailbox_name in test_mailbox_name_set:
            self.mailbox_set[test_mailbox_name] = get_test_mailbox(test_mailbox_name)

    def tearDown(self):
        for mailbox in self.mailbox_set.values():
            mailbox.logout()

