import os
import unittest
import configparser
from imap_tools import MailBox

TEST_MAILBOX_NAME_SET = {'YANDEX', 'ZIMBRA', 'MAIL_RU', 'OUTLOOK', 'GOOGLE'}


def get_test_mailbox_config(mailbox_name: str) -> dict:
    config = configparser.ConfigParser()
    for config_path in (r'../tests/credentials.ini', r'tests/credentials.ini'):
        if not os.path.exists(config_path):
            continue
        config.read(config_path)
        return dict(
            host=config[mailbox_name]['host'],
            email=config[mailbox_name]['email'],
            password=config[mailbox_name]['password'],
            path_separator=config[mailbox_name]['path_separator'],
            test_folder=config[mailbox_name]['test_folder'],
        )


def get_test_mailbox(mailbox_name: str):
    # get config
    config = get_test_mailbox_config(mailbox_name)

    # add test attributes to MailBox
    class MailBoxTestEx(MailBox):
        def __init__(self, *args):
            super().__init__(*args)
            test_folder = config['test_folder']
            path_separator = config['path_separator']
            self.folder_test = '{}'.format(test_folder)
            self.folder_test_base = '{}{}base'.format(test_folder, path_separator)
            self.folder_test_temp1 = '{}{}temp1'.format(test_folder, path_separator)
            self.folder_test_temp2 = '{}{}temp2'.format(test_folder, path_separator)
            self.folder_test_new = '{}{}new'.format(test_folder, path_separator)
            self.folder_test_new1 = '{}{}new1'.format(test_folder, path_separator)

    # create mailbox instance
    mailbox = MailBoxTestEx(config['host'])
    # connect
    mailbox.login(config['email'], config['password'])
    # done
    return mailbox


class MailboxTestCase(unittest.TestCase):
    def setUp(self):
        self.mailbox_set = dict()
        for test_mailbox_name in TEST_MAILBOX_NAME_SET:
            self.mailbox_set[test_mailbox_name] = get_test_mailbox(test_mailbox_name)

    def tearDown(self):
        for mailbox in self.mailbox_set.values():
            mailbox.logout()
