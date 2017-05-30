import unittest
from tests.utils import MailboxTestCase, test_mailbox_name_set, get_test_mailbox


class ActionTest(MailboxTestCase):
    base_folder = 'test|base'
    temp1_folder = 'test|temp1'
    temp2_folder = 'test|temp2'
    test_msg_cnt = 6

    @classmethod
    def tearDownClass(cls):
        # clear temp folders
        for test_mailbox_name in test_mailbox_name_set:
            mailbox = get_test_mailbox(test_mailbox_name)
            mailbox.folder.set(ActionTest.temp1_folder)
            temp1_uid_set = [msg.uid for msg in mailbox.fetch()]
            if temp1_uid_set:
                mailbox.delete(temp1_uid_set)
            temp2_uid_set = [msg.uid for msg in mailbox.fetch()]
            if temp2_uid_set:
                mailbox.delete(temp2_uid_set)

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

            # DELETE
            mailbox.folder.set(self.temp2_folder)
            mailbox.delete([msg.uid for msg in mailbox.fetch()])
            self.assertEqual(len(list(mailbox.fetch())), 0)

            '''
            # FLAG unseen messages in current folder as Answered and Flagged, *in bulk
            mailbox.flag([msg.uid for msg in mailbox.fetch('(UNSEEN)')], ['Answered', 'Flagged'], True)
            # mark SEEN all messages sent at 05.03.2007 in current folder as unseen, *in bulk
            mailbox.seen([msg.uid for msg in mailbox.fetch("SENTON 05-Mar-2007")], False)
            '''


if __name__ == "__main__":
    unittest.main()
