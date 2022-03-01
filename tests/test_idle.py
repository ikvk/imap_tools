import unittest

from tests.utils import MailboxTestCase


class IdleTest(MailboxTestCase):

    def test_idle(self):
        for mailbox_name, mailbox in self.mailbox_set.items():
            if mailbox.mailbox_name in ('MAIL_RU', 'YAHOO'):
                continue
            responses1 = mailbox.idle.wait(timeout=0.5)
            self.assertIs(type(responses1), list)

            mailbox.idle.start()
            responses2 = mailbox.idle.poll(0.5)
            mailbox.idle.stop()
            self.assertIs(type(responses2), list)

            self.assertEqual(len(tuple(mailbox.fetch(limit=1))), 1)


if __name__ == "__main__":
    unittest.main()
