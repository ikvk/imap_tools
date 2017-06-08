import unittest
from tests.utils import MailboxTestCase


class MessageTest(MailboxTestCase):
    def test_attributes(self):
        for mailbox in self.mailbox_set.values():
            mailbox.folder.set(mailbox.folder_test_base)
            for message in mailbox.fetch():
                self.assertIs(type(message.id), str)
                self.assertIn(type(message.uid), [str, type(None)])
                self.assertIs(type(message.subject), str)
                self.assertIs(type(message.from_), str)
                self.assertIs(type(message.from_values), dict)
                self.assertIs(type(message.to), list)
                self.assertIs(type(message.to_values), list)
                self.assertIs(type(message.date), str)
                self.assertIn(type(message.text), [str, type(None)])
                self.assertIn(type(message.html), [str, type(None)])
                self.assertIs(type(message.flags), list)
                for filename, payload in message.get_attachments():
                    self.assertIs(type(filename), str)
                    self.assertIs(type(payload), bytes)


if __name__ == "__main__":
    unittest.main()
