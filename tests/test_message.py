import os
import unittest
import datetime
from tests.utils import MailboxTestCase

from tests.data import MESSAGE_ATTRIBUTES
from imap_tools import MailMessage, MailMessageFlags


class MessageTest(MailboxTestCase):

    def test_live(self):
        none_type = type(None)
        for mailbox in self.mailbox_set.values():
            mailbox.folder.set(mailbox.folder_test_base)
            flag_set = {MailMessageFlags.ANSWERED, MailMessageFlags.FLAGGED}

            # search
            found_nums = mailbox.search()
            self.assertTrue(all(type(i) is str for i in found_nums))

            # headers_only
            cnt_fetch_all_head = 0
            cnt_fetch_all_head_answered_and_flagged = 0
            for message in mailbox.fetch(headers_only=True):
                if flag_set.issubset(message.flags):
                    cnt_fetch_all_head_answered_and_flagged += 1
                cnt_fetch_all_head += 1
                self.assertEqual(message.text, '')
                self.assertEqual(message.html, '')
                self.assertEqual(len(message.attachments), 0)

            # fetch in bulk
            cnt_fetch_all_bulk = 0
            cnt_fetch_all_bulk_answered_and_flagged = 0
            for message in mailbox.fetch(bulk=True):
                if flag_set.issubset(message.flags):
                    cnt_fetch_all_bulk_answered_and_flagged += 1
                cnt_fetch_all_bulk += 1

            # fetch by one, types
            cnt_fetch_all = 0
            cnt_fetch_all_answered_and_flagged = 0
            for message in mailbox.fetch():
                if flag_set.issubset(message.flags):
                    cnt_fetch_all_answered_and_flagged += 1
                cnt_fetch_all += 1
                self.assertIn(type(message.uid), (str, none_type))
                self.assertIs(type(message.subject), str)
                self.assertIs(type(message.from_), str)
                self.assertIn(type(message.from_values), (dict, none_type))
                self.assertIs(type(message.date), datetime.datetime)
                self.assertIs(type(message.date_str), str)
                self.assertIs(type(message.text), str)
                self.assertIs(type(message.html), str)
                self.assertIs(type(message.headers), dict)
                self.assertIn(type(message.size), (int, none_type))

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

                for att in message.attachments:
                    self.assertIs(type(att.filename), str)
                    self.assertIs(type(att.content_type), str)
                    self.assertIs(type(att.payload), bytes)

            # counts
            self.assertTrue(cnt_fetch_all_answered_and_flagged >= 1)
            self.assertTrue(cnt_fetch_all_head_answered_and_flagged >= 1)
            self.assertTrue(cnt_fetch_all_bulk_answered_and_flagged >= 1)
            self.assertTrue(cnt_fetch_all == cnt_fetch_all_head == cnt_fetch_all_bulk == len(found_nums) == 6)
            self.assertTrue(
                cnt_fetch_all_answered_and_flagged ==
                cnt_fetch_all_head_answered_and_flagged ==
                cnt_fetch_all_bulk_answered_and_flagged
            )

    def test_attributes(self):
        msg_attr_set = {'subject', 'from_', 'to', 'cc', 'bcc', 'reply_to', 'date', 'date_str', 'text', 'html',
                        'headers', 'from_values', 'to_values', 'cc_values', 'bcc_values', 'reply_to_values'}
        att_attr_set = {'filename', 'content_id', 'content_type', 'content_disposition', 'payload'}
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
