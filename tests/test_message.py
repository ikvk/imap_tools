import unittest
import datetime
from tests.utils import MailboxTestCase


class MessageTest(MailboxTestCase):

    def test_attributes(self):
        none_type = type(None)
        for mailbox in self.mailbox_set.values():
            mailbox.folder.set(mailbox.folder_test_base)
            for message in mailbox.fetch():
                self.assertIn(type(message.uid), (str, none_type))
                self.assertIs(type(message.subject), str)
                self.assertIs(type(message.from_), str)
                self.assertIn(type(message.from_values), (dict, none_type))
                self.assertIs(type(message.date), datetime.datetime)
                self.assertIs(type(message.date_str), str)
                self.assertIs(type(message.text), str)
                self.assertIs(type(message.html), str)
                self.assertIs(type(message.headers), dict)

                self.assertIs(type(message.to), tuple)
                for i in message.to:
                    self.assertIs(type(i), str)
                self.assertIs(type(message.to_values), tuple)
                for i in message.to_values:
                    self.assertIs(type(i), dict)

                self.assertIs(type(message.cc), tuple)
                for i in message.cc:
                    self.assertIs(type(i), str)
                self.assertIs(type(message.cc_values), tuple)
                for i in message.cc_values:
                    self.assertIs(type(i), dict)

                self.assertIs(type(message.bcc), tuple)
                for i in message.bcc:
                    self.assertIs(type(i), str)
                self.assertIs(type(message.bcc_values), tuple)
                for i in message.bcc_values:
                    self.assertIs(type(i), dict)

                self.assertIs(type(message.flags), tuple)
                for i in message.flags:
                    self.assertIs(type(i), str)

                for filename, payload in message.attachments:
                    self.assertIs(type(filename), str)
                    self.assertIs(type(payload), bytes)


if __name__ == "__main__":
    unittest.main()
