import os
import unittest
import configparser
from imap_tools import MailBox

test_mailbox_name_set = {'YANDEX', 'ZIMBRA', 'MAIL_RU'}  # YANDEX, MAIL_RU, GOOGLE, ZIMBRA


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
        )


def get_test_mailbox(mailbox_name: str):
    # get config
    config = get_test_mailbox_config(mailbox_name)

    # add class attributes for pycharm code analyzer
    class MailBoxTestEx(MailBox):
        def __init__(self, *args):
            super().__init__(*args)
            self.folder_test = 'test'
            self.folder_test_base = 'test{}base'
            self.folder_test_temp1 = 'test{}temp1'
            self.folder_test_temp2 = 'test{}temp2'
            self.folder_test_new = 'test{}new'
            self.folder_test_new1 = 'test{}new1'

    # create mailbox instance
    mailbox = MailBoxTestEx(config['host'])
    # connect
    mailbox.login(config['email'], config['password'])
    # set test folder paths
    mailbox.folder_test_base = mailbox.folder_test_base.format(config['path_separator'])
    mailbox.folder_test_temp1 = mailbox.folder_test_temp1.format(config['path_separator'])
    mailbox.folder_test_temp2 = mailbox.folder_test_temp2.format(config['path_separator'])
    mailbox.folder_test_new = mailbox.folder_test_new.format(config['path_separator'])
    mailbox.folder_test_new1 = mailbox.folder_test_new1.format(config['path_separator'])
    # done
    return mailbox


class MailboxTestCase(unittest.TestCase):
    def setUp(self):
        self.mailbox_set = dict()
        for test_mailbox_name in test_mailbox_name_set:
            self.mailbox_set[test_mailbox_name] = get_test_mailbox(test_mailbox_name)

    def tearDown(self):
        for mailbox in self.mailbox_set.values():
            mailbox.logout()
