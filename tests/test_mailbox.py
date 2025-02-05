import unittest

from tests.utils import MailboxTestCase, TEST_MAILBOX_NAME_SET, get_test_mailbox
from imap_tools.errors import MailboxCopyError
from imap_tools.consts import MailMessageFlags, SortCriteria
from imap_tools.query import A

TEST_MESSAGE_DATA = b'From: Mikel <test@lindsaar.net>\nTo: Mikel <raasdnil@gmail.com>\nContent-Type: text/plain; charset=US-ASCII; format=flowed\nContent-Transfer-Encoding: 7bit\nMime-Version: 1.0 (Apple Message framework v929.2)\nSubject: _append_\nDate: Sat, 22 Nov 2008 11:04:59 +1100\n\nPlain email.\n'  # noqa


class MailboxTest(MailboxTestCase):
    base_test_msg_cnt = 6
    test_chunks_size = 4

    @classmethod
    def setUpClass(cls):
        # clear temp folders
        for test_mailbox_name in TEST_MAILBOX_NAME_SET:
            mailbox = get_test_mailbox(test_mailbox_name)
            mailbox.folder.set(mailbox.folder_test_temp1)
            mailbox.delete(mailbox.uids())
            mailbox.folder.set(mailbox.folder_test_temp2)
            mailbox.delete(mailbox.uids())

    def test_action(self):
        for mailbox in self.mailbox_set.values():
            mailbox.folder.set(mailbox.folder_test_base)

            # SORT
            if mailbox.mailbox_name == 'ZIMBRA':
                found_msgs = tuple(mailbox.fetch(
                    bulk=True, headers_only=1, sort=[SortCriteria.SIZE_ASC, SortCriteria.FROM_DESC]))
                self.assertEqual(len(found_msgs), self.base_test_msg_cnt)

            # FETCH
            found_msgs = tuple(mailbox.fetch(bulk=True, headers_only=1))
            self.assertEqual(len(found_msgs), self.base_test_msg_cnt)
            found_msgs = tuple(mailbox.fetch(bulk=3, headers_only=1))
            self.assertEqual(len(found_msgs), self.base_test_msg_cnt)

            # FETCH nonexistent
            nonexistent_criteria = A(uid=['1000000000'])
            nonexistent_msgs1 = tuple(mailbox.fetch(nonexistent_criteria, bulk=False))
            self.assertEqual(len(nonexistent_msgs1), 0)
            nonexistent_msgs2 = tuple(mailbox.fetch(nonexistent_criteria, bulk=True))
            self.assertEqual(len(nonexistent_msgs2), 0)

            # NUMBERS
            found_nums = mailbox.numbers()
            self.assertTrue(bool(found_nums))
            self.assertTrue(all(type(i) is str for i in found_nums))

            # NUMBERS_TO_UIDS
            found_uids = mailbox.numbers_to_uids(found_nums)
            self.assertTrue(bool(found_uids))
            self.assertTrue(all(type(i) is str for i in found_uids))

            # UIDS
            found_uids = mailbox.uids()
            self.assertTrue(bool(found_uids))
            self.assertTrue(all(type(i) is str for i in found_uids))
            self.assertEqual(set([i.uid for i in mailbox.fetch(headers_only=True, bulk=True)]), set(found_uids))

            # cnt
            self.assertTrue(
                len(found_msgs) ==
                len(found_nums) ==
                len(found_uids) ==
                self.base_test_msg_cnt
            )

            # APPEND
            if mailbox.mailbox_name not in ('MAIL_RU', 'YANDEX'):
                mailbox.folder.set('INBOX')
                q = A(subject='_append_')
                mailbox.delete(mailbox.uids(q))
                self.assertEqual(len(list(mailbox.numbers(q))), 0)
                mailbox.append(TEST_MESSAGE_DATA)
                self.assertEqual(len(list(mailbox.numbers(q))), 1)  # YANDEX 0!=1 in test only, strange
                mailbox.delete(mailbox.uids(q))

            # COPY
            mailbox.folder.set(mailbox.folder_test_base)
            mailbox.copy(mailbox.uids(), mailbox.folder_test_temp1)
            if mailbox.mailbox_name != 'YAHOO':
                # YAHOO:
                #   imaplib.IMAP4.error: UID command error: BAD [b'[TRYCREATE] UID COPY failed -
                #   No mailbox exists with name - "__nonexistent_folder__"']
                with self.assertRaises(MailboxCopyError):
                    mailbox.copy(mailbox.uids(), '__nonexistent_folder__')
            self.assertEqual(len(list(mailbox.numbers())), self.base_test_msg_cnt)
            mailbox.folder.set(mailbox.folder_test_temp1)
            self.assertEqual(len(list(mailbox.numbers())), self.base_test_msg_cnt)

            # MOVE
            mailbox.folder.set(mailbox.folder_test_temp1)
            mailbox.move(mailbox.uids(), mailbox.folder_test_temp2)
            self.assertEqual(len(list(mailbox.numbers())), 0)
            mailbox.folder.set(mailbox.folder_test_temp2)
            self.assertEqual(len(list(mailbox.numbers())), self.base_test_msg_cnt)

            # FLAG
            mailbox.folder.set(mailbox.folder_test_temp2)
            mailbox.flag(mailbox.uids(), MailMessageFlags.FLAGGED, True)
            self.assertTrue(
                all([MailMessageFlags.FLAGGED in msg.flags for msg in mailbox.fetch(bulk=True, headers_only=1)]))

            # DELETE
            mailbox.folder.set(mailbox.folder_test_temp2)
            mailbox.delete(mailbox.uids())
            self.assertEqual(len(list(mailbox.numbers())), 0)

            # COPY chunks
            mailbox.folder.set(mailbox.folder_test_base)
            mailbox.copy(mailbox.uids(), mailbox.folder_test_temp1, self.test_chunks_size)
            self.assertEqual(len(list(mailbox.numbers())), self.base_test_msg_cnt)
            mailbox.folder.set(mailbox.folder_test_temp1)
            self.assertEqual(len(list(mailbox.numbers())), self.base_test_msg_cnt)
            # MOVE chunks
            mailbox.folder.set(mailbox.folder_test_temp1)
            mailbox.move(mailbox.uids(), mailbox.folder_test_temp2, self.test_chunks_size)
            self.assertEqual(len(list(mailbox.numbers())), 0)
            mailbox.folder.set(mailbox.folder_test_temp2)
            self.assertEqual(len(list(mailbox.numbers())), self.base_test_msg_cnt)
            # FLAG chunks
            mailbox.folder.set(mailbox.folder_test_temp2)
            mailbox.flag(mailbox.uids(), MailMessageFlags.FLAGGED, True, self.test_chunks_size)
            self.assertTrue(
                all([MailMessageFlags.FLAGGED in msg.flags for msg in mailbox.fetch(bulk=True, headers_only=1)]))
            # DELETE chunks
            mailbox.folder.set(mailbox.folder_test_temp2)
            mailbox.delete(mailbox.uids(), self.test_chunks_size)
            self.assertEqual(len(list(mailbox.numbers())), 0)


if __name__ == "__main__":
    unittest.main()
