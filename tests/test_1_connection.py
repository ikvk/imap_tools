import unittest
from imap_tools import MailBox
from tests.utils import get_test_mailbox_config, test_mailbox_name_set


class ConnectionTest(unittest.TestCase):
    def test_connection(self):
        for test_mailbox_name in test_mailbox_name_set:
            config = get_test_mailbox_config(test_mailbox_name)
            mailbox = MailBox(config['host'])
            self.assertIs(type(mailbox), MailBox)
            login_result = mailbox.login(config['email'], config['password'])
            self.assertEqual(login_result[0], 'OK')
            logout_result = mailbox.logout()
            self.assertEqual(logout_result[0], 'BYE')


if __name__ == "__main__":
    unittest.main()
