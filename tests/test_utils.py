import unittest

from imap_tools import utils


class UtilsTest(unittest.TestCase):

    def test_some(self):
        self.assertEqual(1, 1)

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