import unittest

from tests.utils import MailboxTestCase


class IdleTest(MailboxTestCase):

    def test_idle(self):
        for mailbox_name, mailbox in self.mailbox_set.items():
            if mailbox.mailbox_name in ('MAIL_RU', 'YAHOO'):
                continue
            mailbox.idle.wait(timeout=1)
            self.assertEqual(len(tuple(mailbox.fetch(limit=1))), 1)


if __name__ == "__main__":
    unittest.main()
