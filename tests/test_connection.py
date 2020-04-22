import unittest

from imap_tools import MailBox
from tests.utils import get_test_mailbox_config, TEST_MAILBOX_NAME_SET


class ConnectionTest(unittest.TestCase):
    def test_connection(self):
        # simple
        for test_mailbox_name in TEST_MAILBOX_NAME_SET:
            config = get_test_mailbox_config(test_mailbox_name)
            mailbox = MailBox(config['host'])
            self.assertIs(type(mailbox), MailBox)
            login_result = mailbox.login(config['email'], config['password'])
            self.assertEqual(login_result.login_result[0], 'OK')
            logout_result = mailbox.logout()
            self.assertEqual(logout_result[0], 'BYE')
        # with
        for test_mailbox_name in TEST_MAILBOX_NAME_SET:
            config = get_test_mailbox_config(test_mailbox_name)
            with MailBox(config['host']).login(config['email'], config['password']) as mailbox:
                self.assertIs(type(mailbox), MailBox)
                self.assertEqual(mailbox.login_result[0], 'OK')
            # later: test logout result here


if __name__ == "__main__":
    unittest.main()
