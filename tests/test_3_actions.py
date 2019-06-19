import unittest

import imap_tools
from tests.utils import MailboxTestCase, test_mailbox_name_set, get_test_mailbox


class ActionTest(MailboxTestCase):
    base_test_msg_cnt = 6

    @classmethod
    def setUpClass(cls):
        # clear temp folders
        for test_mailbox_name in test_mailbox_name_set:
            mailbox = get_test_mailbox(test_mailbox_name)
            mailbox.folder.set(mailbox.folder_test_temp1)
            for_del_1 = [msg.uid for msg in mailbox.fetch()]
            if for_del_1:
                mailbox.delete([msg.uid for msg in mailbox.fetch()])
            mailbox.folder.set(mailbox.folder_test_temp2)
            for_del_2 = [msg.uid for msg in mailbox.fetch()]
            if for_del_2:
                mailbox.delete(for_del_2)

    def test_action(self):
        for mailbox in self.mailbox_set.values():
            # FETCH
            mailbox.folder.set(mailbox.folder_test_base)
            self.assertEqual(len(list(mailbox.fetch())), self.base_test_msg_cnt)

            # COPY
            mailbox.folder.set(mailbox.folder_test_base)
            mailbox.copy([msg.uid for msg in mailbox.fetch()], mailbox.folder_test_temp1)
            self.assertEqual(len(list(mailbox.fetch())), self.base_test_msg_cnt)
            mailbox.folder.set(mailbox.folder_test_temp1)
            self.assertEqual(len(list(mailbox.fetch())), self.base_test_msg_cnt)

            # MOVE
            mailbox.folder.set(mailbox.folder_test_temp1)
            mailbox.move([msg.uid for msg in mailbox.fetch()], mailbox.folder_test_temp2)
            self.assertEqual(len(list(mailbox.fetch())), 0)
            mailbox.folder.set(mailbox.folder_test_temp2)
            self.assertEqual(len(list(mailbox.fetch())), self.base_test_msg_cnt)

            # FLAG
            mailbox.folder.set(mailbox.folder_test_temp2)
            mailbox.flag([msg.uid for msg in mailbox.fetch()], imap_tools.StandardMessageFlags.FLAGGED, True)
            self.assertTrue(all([imap_tools.StandardMessageFlags.FLAGGED in msg.flags for msg in mailbox.fetch()]))

            # SEEN
            mailbox.folder.set(mailbox.folder_test_temp2)
            mailbox.seen([msg.uid for msg in mailbox.fetch()], False)
            self.assertTrue(all([imap_tools.StandardMessageFlags.SEEN not in msg.flags
                                 for msg in mailbox.fetch(mark_seen=False)]))

            # DELETE
            mailbox.folder.set(mailbox.folder_test_temp2)
            mailbox.delete([msg.uid for msg in mailbox.fetch()])
            self.assertEqual(len(list(mailbox.fetch())), 0)

            # _uid_str
            for i in [' 1, 2, 3 ', ['1', '2', '3'], (' 1 ', '2', '3')]:
                self.assertEqual(mailbox._uid_str(i), '1,2,3')
            for i in ['', [], (), set(), [1, '2'], ('1', '2', 'test_3')]:
                with self.assertRaises(imap_tools.MailBoxUidParamError):
                    mailbox._uid_str(i)
            for i in [dict, int, 1, ..., MailboxTestCase]:
                with self.assertRaises(TypeError):
                    mailbox._uid_str(i)

            # check_status
            self.assertIsNone(mailbox.check_status('test', ('EXP', 'test'), expected='EXP'))
            with self.assertRaises(imap_tools.ImapToolsError):
                self.assertFalse(mailbox.check_status('test', ('NOT_OK', 'test')))


if __name__ == "__main__":
    unittest.main()
