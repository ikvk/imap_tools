import unittest
from tests.utils import MailboxTestCase, test_mailbox_name_set, get_test_mailbox


class FoldersTest(MailboxTestCase):
    folder_test = 'test'
    folder_test_base = 'test|base'
    folder_test_temp1 = 'test|temp1'
    folder_test_temp2 = 'test|temp2'
    folder_test_new = 'test|new'
    folder_test_new1 = 'test|new1'

    @classmethod
    def setUpClass(cls):
        # delete temp new folders
        for test_mailbox_name in test_mailbox_name_set:
            mailbox = get_test_mailbox(test_mailbox_name)
            for del_folder in (FoldersTest.folder_test_new, FoldersTest.folder_test_new1):
                if mailbox.folder.exists(del_folder):
                    mailbox.folder.delete(del_folder)

    def test_folders(self):
        for mailbox in self.mailbox_set.values():
            # _pairs_to_dict
            self.assertEqual(mailbox.folder._pairs_to_dict(['a', '1', 'b', '2']), dict(a='1', b='2'))
            with self.assertRaises(ValueError):
                mailbox.folder._pairs_to_dict(['1', '2', '3'])
            # LIST
            folder_list = mailbox.folder.list(self.folder_test)
            self.assertEqual(
                set([i['name'] for i in folder_list]),
                {self.folder_test_base, self.folder_test_temp1, self.folder_test_temp2}
            )
            for folder in folder_list:
                self.assertIs(type(folder['flags']), str)
                self.assertIs(type(folder['delim']), str)
                self.assertIs(type(folder['name']), str)
            # SET, GET
            mailbox.folder.set(self.folder_test_base)
            self.assertEqual(mailbox.folder.get(), self.folder_test_base)
            # CREATE
            mailbox.folder.create(self.folder_test_new)
            folder_list_names = [i['name'] for i in mailbox.folder.list(self.folder_test)]
            self.assertTrue(self.folder_test_new in folder_list_names)
            # EXISTS
            self.assertTrue(mailbox.folder.exists(self.folder_test_new))
            # RENAME
            mailbox.folder.rename(self.folder_test_new, self.folder_test_new1)
            folder_list_names = [i['name'] for i in mailbox.folder.list(self.folder_test)]
            self.assertTrue(self.folder_test_new1 in folder_list_names)
            self.assertFalse(self.folder_test_new in folder_list_names)
            # DELETE
            mailbox.folder.delete(self.folder_test_new1)
            folder_list_names = [i['name'] for i in mailbox.folder.list(self.folder_test)]
            self.assertFalse(self.folder_test_new1 in folder_list_names)
            # STATUS
            for status_key, status_val in mailbox.folder.status(self.folder_test_base).items():
                self.assertIs(type(status_key), str)
                self.assertIs(type(status_val), str)


if __name__ == "__main__":
    unittest.main()
