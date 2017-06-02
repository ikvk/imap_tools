import unittest
from imap_tools import ImapToolsError
from tests.utils import MailboxTestCase, test_mailbox_name_set, get_test_mailbox


class ActionTest(MailboxTestCase):
    base_folder = 'test|base'
    temp1_folder = 'test|temp1'
    temp2_folder = 'test|temp2'
    test_msg_cnt = 6

    @classmethod
    def setUpClass(cls):
        # clear temp folders
        for test_mailbox_name in test_mailbox_name_set:
            mailbox = get_test_mailbox(test_mailbox_name)
            mailbox.folder.set(ActionTest.temp1_folder)
            mailbox.delete([msg.uid for msg in mailbox.fetch()])
            mailbox.folder.set(ActionTest.temp2_folder)
            mailbox.delete([msg.uid for msg in mailbox.fetch()])

    def test_action(self):
        for mailbox in self.mailbox_set.values():
            # FETCH
            mailbox.folder.set(self.base_folder)
            self.assertEqual(len(list(mailbox.fetch())), self.test_msg_cnt)

            # COPY
            mailbox.folder.set(self.base_folder)
            mailbox.copy([msg.uid for msg in mailbox.fetch()], self.temp1_folder)
            self.assertEqual(len(list(mailbox.fetch())), self.test_msg_cnt)
            mailbox.folder.set(self.temp1_folder)
            self.assertEqual(len(list(mailbox.fetch())), self.test_msg_cnt)

            # MOVE
            mailbox.folder.set(self.temp1_folder)
            mailbox.move([msg.uid for msg in mailbox.fetch()], self.temp2_folder)
            self.assertEqual(len(list(mailbox.fetch())), 0)
            mailbox.folder.set(self.temp2_folder)
            self.assertEqual(len(list(mailbox.fetch())), self.test_msg_cnt)

            # FLAG
            mailbox.folder.set(self.temp2_folder)
            mailbox.flag([msg.uid for msg in mailbox.fetch()], mailbox.StandardMessageFlags.FLAGGED, True)
            self.assertTrue(all([mailbox.StandardMessageFlags.FLAGGED in msg.flags for msg in mailbox.fetch()]))

            # SEEN
            mailbox.folder.set(self.temp2_folder)
            mailbox.seen([msg.uid for msg in mailbox.fetch()], False)
            # fetching data implicitly set the \Seen flag., waiting for improve fetch
            # self.assertTrue(all([mailbox.StandardMessageFlags.SEEN not in msg.flags for msg in mailbox.fetch()]))

            # DELETE
            mailbox.folder.set(self.temp2_folder)
            mailbox.delete([msg.uid for msg in mailbox.fetch()])
            self.assertEqual(len(list(mailbox.fetch())), 0)

            # _uid_str
            self.assertEqual(mailbox._uid_str(['1', '2', 'test_3']), '1,2,test_3')
            with self.assertRaises(mailbox.MailBoxUidParamError):
                mailbox._uid_str([])
            with self.assertRaises(mailbox.MailBoxUidParamError):
                mailbox._uid_str([1, 2, 3])

            # check_status
            self.assertIsNone(mailbox.check_status('test', ('EXP', 'test'), expected='EXP'))
            with self.assertRaises(ImapToolsError):
                self.assertFalse(mailbox.check_status('test', ('NOT_OK', 'test')))


if __name__ == "__main__":
    unittest.main()
