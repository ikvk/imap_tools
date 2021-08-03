import unittest

from tests.utils import MailboxTestCase, TEST_MAILBOX_NAME_SET, get_test_mailbox
from imap_tools.errors import MailboxCopyError
from imap_tools.consts import MailMessageFlags
from imap_tools.query import A

FETCH_ARGS = dict(bulk=True, headers_only=True)

TEST_MESSAGE_DATA = b'From: Mikel <test@lindsaar.net>\nTo: Mikel <raasdnil@gmail.com>\nContent-Type: text/plain; charset=US-ASCII; format=flowed\nContent-Transfer-Encoding: 7bit\nMime-Version: 1.0 (Apple Message framework v929.2)\nSubject: _append_\nDate: Sat, 22 Nov 2008 11:04:59 +1100\n\nPlain email.\n'  # noqa


class ActionTest(MailboxTestCase):
    base_test_msg_cnt = 6

    @classmethod
    def setUpClass(cls):
        # clear temp folders
        for test_mailbox_name in TEST_MAILBOX_NAME_SET:
            mailbox = get_test_mailbox(test_mailbox_name)
            mailbox.folder.set(mailbox.folder_test_temp1)
            mailbox.delete(mailbox.fetch(**FETCH_ARGS))
            mailbox.folder.set(mailbox.folder_test_temp2)
            mailbox.delete(mailbox.fetch(**FETCH_ARGS))

    def test_action(self):
        for mailbox in self.mailbox_set.values():
            # FETCH
            mailbox.folder.set(mailbox.folder_test_base)
            self.assertEqual(len(list(mailbox.numbers())), self.base_test_msg_cnt)

            # COPY
            mailbox.folder.set(mailbox.folder_test_base)
            mailbox.copy(mailbox.fetch(**FETCH_ARGS), mailbox.folder_test_temp1)
            if mailbox.mailbox_name != 'YAHOO':
                # YAHOO:
                #   imaplib.IMAP4.error: UID command error: BAD [b'[TRYCREATE] UID COPY failed -
                #   No mailbox exists with name - "__nonexistent_folder__"']
                with self.assertRaises(MailboxCopyError):
                    mailbox.copy(mailbox.fetch(limit=1), '__nonexistent_folder__')
            self.assertEqual(len(list(mailbox.numbers())), self.base_test_msg_cnt)
            mailbox.folder.set(mailbox.folder_test_temp1)
            self.assertEqual(len(list(mailbox.numbers())), self.base_test_msg_cnt)

            # MOVE
            mailbox.folder.set(mailbox.folder_test_temp1)
            mailbox.move(mailbox.fetch(**FETCH_ARGS), mailbox.folder_test_temp2)
            self.assertEqual(len(list(mailbox.numbers())), 0)
            mailbox.folder.set(mailbox.folder_test_temp2)
            self.assertEqual(len(list(mailbox.numbers())), self.base_test_msg_cnt)

            # FLAG
            mailbox.folder.set(mailbox.folder_test_temp2)
            mailbox.flag(mailbox.fetch(**FETCH_ARGS), MailMessageFlags.FLAGGED, True)
            self.assertTrue(
                all([MailMessageFlags.FLAGGED in msg.flags for msg in mailbox.fetch(**FETCH_ARGS)]))

            # DELETE
            mailbox.folder.set(mailbox.folder_test_temp2)
            mailbox.delete(mailbox.fetch(**FETCH_ARGS))
            self.assertEqual(len(list(mailbox.numbers())), 0)

            # APPEND
            if mailbox.mailbox_name not in ('MAIL_RU', 'YANDEX'):
                mailbox.folder.set('INBOX')
                q = A(subject='_append_')
                mailbox.delete(mailbox.fetch(q, **FETCH_ARGS))
                self.assertEqual(len(list(mailbox.numbers(q))), 0)
                mailbox.append(TEST_MESSAGE_DATA)
                self.assertEqual(len(list(mailbox.numbers(q))), 1)  # YANDEX 0!=1 in test only, strange
                mailbox.delete(mailbox.fetch(q, **FETCH_ARGS))


if __name__ == "__main__":
    unittest.main()
