import os
import unittest
import datetime
from tests.utils import MailboxTestCase

from tests.data import MESSAGE_ATTRIBUTES
from imap_tools import MailMessage, MessageFlags


class MessageTest(MailboxTestCase):

    def test_live(self):
        none_type = type(None)
        for mailbox in self.mailbox_set.values():
            mailbox.folder.set(mailbox.folder_test_base)
            answered_and_flagged_cnt = 0
            # headers_only
            for message in mailbox.fetch(headers_only=True):
                self.assertEqual(message.text, '')
                self.assertEqual(message.html, '')
                self.assertEqual(len(message.attachments), 0)
            # types
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

                for addr_field in {'to', 'cc', 'bcc', 'reply_to'}:
                    self.assertIs(type(getattr(message, addr_field)), tuple)
                    for i in getattr(message, addr_field):
                        self.assertIs(type(i), str)
                    self.assertIs(type(getattr(message, '{}_values'.format(addr_field))), tuple)
                    for i in getattr(message, '{}_values'.format(addr_field)):
                        self.assertIs(type(i), dict)

                self.assertIs(type(message.flags), tuple)
                for i in message.flags:
                    self.assertIs(type(i), str)
                if {MessageFlags.ANSWERED, MessageFlags.FLAGGED}.issubset(message.flags):
                    answered_and_flagged_cnt += 1

                for att in message.attachments:
                    self.assertIs(type(att.filename), str)
                    self.assertIs(type(att.content_type), str)
                    self.assertIs(type(att.payload), bytes)
            # flags
            self.assertTrue(answered_and_flagged_cnt >= 1)

    def test_attributes(self):
        msg_attr_set = {'subject', 'from_', 'to', 'cc', 'bcc', 'reply_to', 'date', 'date_str', 'text', 'html',
                        'headers', 'from_values', 'to_values', 'cc_values', 'bcc_values', 'reply_to_values'}
        att_attr_set = {'filename', 'content_type', 'payload'}
        for file_name in MESSAGE_ATTRIBUTES.keys():
            message_data = MESSAGE_ATTRIBUTES[file_name]
            for msg_path in ('../tests/messages/{}.eml'.format(file_name), 'tests/messages/{}.eml'.format(file_name)):
                if not os.path.exists(msg_path):
                    continue
                with open(msg_path, 'rb') as f:
                    bytes_data = f.read()
            message = MailMessage.from_bytes(bytes_data)
            for msg_attr in msg_attr_set:
                self.assertEqual(getattr(message, msg_attr), message_data[msg_attr])
            for att_i, att in enumerate(message.attachments):
                for att_attr in att_attr_set:
                    self.assertEqual(getattr(att, att_attr), message_data['attachments'][att_i][att_attr])


if __name__ == "__main__":
    unittest.main()
