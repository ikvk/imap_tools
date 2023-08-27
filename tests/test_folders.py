import unittest

from tests.utils import MailboxTestCase, TEST_MAILBOX_NAME_SET, get_test_mailbox
from imap_tools.errors import MailboxFolderSelectError


class FoldersTest(MailboxTestCase):
    @classmethod
    def setUpClass(cls):
        # delete temp new folders
        for test_mailbox_name in TEST_MAILBOX_NAME_SET:
            mailbox = get_test_mailbox(test_mailbox_name)
            for del_folder in (mailbox.folder_test_new, mailbox.folder_test_new1):
                if mailbox.folder.exists(del_folder):
                    mailbox.folder.delete(del_folder)

    def test_folders(self):
        for mailbox_name, mailbox in self.mailbox_set.items():
            # LIST
            folder_list = mailbox.folder.list(mailbox.folder_test)
            check_folder_set = {mailbox.folder_test_base, mailbox.folder_test_temp1, mailbox.folder_test_temp2}
            self.assertTrue(check_folder_set.issubset(set([i.name for i in folder_list])))
            for folder in folder_list:
                self.assertIs(type(folder.name), str)
                self.assertIs(type(folder.delim), str)
                for flag in folder.flags:
                    self.assertIs(type(flag), str)

            # SET, GET
            mailbox.folder.set(mailbox.folder_test_base)
            self.assertEqual(mailbox.folder.get(), mailbox.folder_test_base)

            # CREATE
            mailbox.folder.create(mailbox.folder_test_new)
            folder_list_names = [i.name for i in mailbox.folder.list(mailbox.folder_test)]
            self.assertTrue(mailbox.folder_test_new in folder_list_names)

            # EXISTS
            self.assertTrue(mailbox.folder.exists(mailbox.folder_test_new))

            # RENAME
            mailbox.folder.rename(mailbox.folder_test_new, mailbox.folder_test_new1)
            folder_list_names = [i.name for i in mailbox.folder.list(mailbox.folder_test)]
            self.assertTrue(mailbox.folder_test_new1 in folder_list_names)
            self.assertFalse(mailbox.folder_test_new in folder_list_names)

            # DELETE
            mailbox.folder.delete(mailbox.folder_test_new1)
            folder_list_names = [i.name for i in mailbox.folder.list(mailbox.folder_test)]
            self.assertFalse(mailbox.folder_test_new1 in folder_list_names)

            # STATUS
            for status_key, status_val in mailbox.folder.status(mailbox.folder_test_base).items():
                self.assertIs(type(status_key), str)
                self.assertIs(type(status_val), int)

            # SUBSCRIBE
            if mailbox.mailbox_name not in ('MAIL_RU', 'YAHOO'):
                mailbox.folder.subscribe(mailbox.folder_test_temp2, False)
                self.assertIn(mailbox.folder_test_temp2, [i.name for i in mailbox.folder.list()])
                self.assertNotIn(mailbox.folder_test_temp2,
                                 [i.name for i in mailbox.folder.list(subscribed_only=1)])
                mailbox.folder.subscribe(mailbox.folder_test_temp2, True)
                self.assertIn(mailbox.folder_test_temp2,
                              [i.name for i in mailbox.folder.list(subscribed_only=1)])

            # error
            if mailbox.mailbox_name not in ('YAHOO',):
                # YAHOO:
                #   imaplib.IMAP4.error: SELECT command error: BAD [b'[TRYCREATE] SELECT error -
                #   Folder does not exist or server encountered an error']
                with self.assertRaises(MailboxFolderSelectError):
                    mailbox.folder.set('__nonexistent_folder__')


if __name__ == "__main__":
    unittest.main()
