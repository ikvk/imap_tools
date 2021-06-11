import unittest

import imap_tools
from tests.utils import MailboxTestCase, TEST_MAILBOX_NAME_SET, get_test_mailbox
from imap_tools.errors import MailboxCopyError

FETCH_ARGS = dict(bulk=True, headers_only=True)


class ActionTest(MailboxTestCase):
    base_test_msg_cnt = 6

    @classmethod
    def setUpClass(cls):
        # clear temp folders
        for test_mailbox_name in TEST_MAILBOX_NAME_SET:
            mailbox = get_test_mailbox(test_mailbox_name)
            mailbox.folder.set(mailbox.folder_test_temp1)
            for_del_1 = [msg.uid for msg in mailbox.fetch(**FETCH_ARGS)]
            if for_del_1:
                mailbox.delete([msg.uid for msg in mailbox.fetch(**FETCH_ARGS)])
            mailbox.folder.set(mailbox.folder_test_temp2)
            for_del_2 = [msg.uid for msg in mailbox.fetch(**FETCH_ARGS)]
            if for_del_2:
                mailbox.delete(for_del_2)

    def test_action(self):
        for mailbox in self.mailbox_set.values():
            # FETCH
            mailbox.folder.set(mailbox.folder_test_base)
            self.assertEqual(len(list(mailbox.fetch(**FETCH_ARGS))), self.base_test_msg_cnt)

            # COPY
            mailbox.folder.set(mailbox.folder_test_base)
            uid_set = [msg.uid for msg in mailbox.fetch(**FETCH_ARGS)]
            mailbox.copy(uid_set, mailbox.folder_test_temp1)
            if mailbox.mailbox_name != 'YAHOO':
                # YAHOO:
                #   imaplib.IMAP4.error: UID command error: BAD [b'[TRYCREATE] UID COPY failed -
                #   No mailbox exists with name - "__nonexistent_folder__"']
                with self.assertRaises(MailboxCopyError):
                    mailbox.copy(uid_set, '__nonexistent_folder__')
            self.assertEqual(len(list(mailbox.fetch(**FETCH_ARGS))), self.base_test_msg_cnt)
            mailbox.folder.set(mailbox.folder_test_temp1)
            self.assertEqual(len(list(mailbox.fetch(**FETCH_ARGS))), self.base_test_msg_cnt)

            # MOVE
            mailbox.folder.set(mailbox.folder_test_temp1)
            mailbox.move([msg.uid for msg in mailbox.fetch(**FETCH_ARGS)], mailbox.folder_test_temp2)
            self.assertEqual(len(list(mailbox.fetch(**FETCH_ARGS))), 0)
            mailbox.folder.set(mailbox.folder_test_temp2)
            self.assertEqual(len(list(mailbox.fetch(**FETCH_ARGS))), self.base_test_msg_cnt)

            # FLAG
            mailbox.folder.set(mailbox.folder_test_temp2)
            mailbox.flag([msg.uid for msg in mailbox.fetch(**FETCH_ARGS)], imap_tools.MailMessageFlags.FLAGGED, True)
            self.assertTrue(
                all([imap_tools.MailMessageFlags.FLAGGED in msg.flags for msg in mailbox.fetch(**FETCH_ARGS)]))

            # SEEN
            mailbox.folder.set(mailbox.folder_test_temp2)
            mailbox.seen([msg.uid for msg in mailbox.fetch(**FETCH_ARGS)], False)
            self.assertTrue(all([imap_tools.MailMessageFlags.SEEN not in msg.flags
                                 for msg in mailbox.fetch(mark_seen=False)]))

            # DELETE
            mailbox.folder.set(mailbox.folder_test_temp2)
            mailbox.delete([msg.uid for msg in mailbox.fetch(**FETCH_ARGS)])
            self.assertEqual(len(list(mailbox.fetch(**FETCH_ARGS))), 0)


if __name__ == "__main__":
    unittest.main()
