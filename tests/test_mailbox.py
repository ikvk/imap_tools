import imaplib
import unittest
from unittest.mock import MagicMock, call, patch

from tests.utils import MailboxTestCase, TEST_MAILBOX_NAME_SET, get_test_mailbox
from imap_tools.errors import MailboxCopyError
from imap_tools.consts import MailMessageFlags, SortCriteria
from imap_tools.query import A
from imap_tools.mailbox import MailBox

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
            found_msgs_fetch_bulk = tuple(mailbox.fetch(bulk=True, headers_only=1))
            self.assertEqual(len(found_msgs_fetch_bulk), self.base_test_msg_cnt)
            found_msgs_fetch_bulk3 = tuple(mailbox.fetch(bulk=3, headers_only=1))
            self.assertEqual(len(found_msgs_fetch_bulk3), self.base_test_msg_cnt)

            # FETCH by uid_list
            found_msgs_by_uids = tuple(mailbox.fetch(uid_list=mailbox.uids(), reverse=True))
            self.assertEqual(len(found_msgs_by_uids), self.base_test_msg_cnt)

            # FETCH nonexistent
            nonexistent_criteria = A(uid=['1000000000'])
            nonexistent_msgs1 = tuple(mailbox.fetch(nonexistent_criteria, bulk=False))
            self.assertEqual(len(nonexistent_msgs1), 0)
            nonexistent_msgs2 = tuple(mailbox.fetch(nonexistent_criteria, bulk=True))
            self.assertEqual(len(nonexistent_msgs2), 0)

            # NUMBERS
            found_numbers = mailbox.numbers()
            self.assertTrue(bool(found_numbers))
            self.assertTrue(all(type(i) is str for i in found_numbers))
            self.assertEqual(len(found_numbers), self.base_test_msg_cnt)

            # NUMBERS charset=None
            self.assertEqual(len(mailbox.numbers(charset=None)), self.base_test_msg_cnt)

            # NUMBERS_TO_UIDS
            found_uids1 = mailbox.numbers_to_uids(found_numbers)
            self.assertTrue(bool(found_uids1))
            self.assertTrue(all(type(i) is str for i in found_uids1))
            self.assertEqual(len(found_uids1), self.base_test_msg_cnt)

            # UIDS
            found_uids2 = mailbox.uids()
            self.assertTrue(bool(found_uids2))
            self.assertTrue(all(type(i) is str for i in found_uids2))
            self.assertEqual(set([i.uid for i in mailbox.fetch(headers_only=True, bulk=True)]), set(found_uids2))
            self.assertEqual(len(found_uids2), self.base_test_msg_cnt)

            # UIDS charset=None
            self.assertEqual(len(mailbox.uids(charset=None)), self.base_test_msg_cnt)

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


class LoginQuotingTest(unittest.TestCase):
    """
    Verify that login() quotes both username and password (issue #265).
    [*1] v3.14.7 quoting changed https://github.com/python/cpython/commit/03d090972a368cbac89acff5ed2a63bdba14dff7
    """

    def _make_mock_client(self):
        mock_client = MagicMock(spec=imaplib.IMAP4)
        mock_client._encoding = 'utf-8'  # [*1]
        mock_client._quote.side_effect = lambda arg: imaplib.IMAP4._quote(mock_client, arg)
        mock_client._simple_command.return_value = ('OK', [b'Logged in'])
        mock_client.select.return_value = ('OK', [b'1'])
        return mock_client

    def test_login_quotes_username_with_special_chars(self):
        """Username containing special IMAP chars (e.g. *) must be quoted."""
        with patch.object(MailBox, '_get_mailbox_client', return_value=self._make_mock_client()):
            mb = MailBox('localhost')
            mb.login('user*name', 'pass', initial_folder=None)
            self.assertIn(
                mb.client._simple_command.call_args[0],
                (('LOGIN', '"user*name"', '"pass"'),
                 ('LOGIN', b'"user*name"', b'"pass"'))  # [*1]
            )

    def test_login_quotes_plain_username(self):
        """Plain username is also correctly passed through quoting."""
        with patch.object(MailBox, '_get_mailbox_client', return_value=self._make_mock_client()):
            mb = MailBox('localhost')
            mb.login('user', 'pass', initial_folder=None)
            self.assertIn(
                mb.client._simple_command.call_args[0],
                (('LOGIN', '"user"', '"pass"'),
                 ('LOGIN', b'"user"', b'"pass"'))  # [*1]
            )


class IterableArgumentsTest(unittest.TestCase):
    def setUp(self):
        self.client = MagicMock(spec=imaplib.IMAP4)
        self.client.capabilities = ()
        self.client.uid.return_value = ('OK', [b'done'])
        self.client.expunge.return_value = ('OK', [])
        self.client.append.return_value = ('OK', [b'done'])
        with patch.object(MailBox, '_get_mailbox_client', return_value=self.client):
            self.mailbox = MailBox('localhost')

    def test_uid_generators_reach_each_command(self):
        for operation in ('copy', 'delete', 'move'):
            for server_move in (False, True):
                with self.subTest(operation=operation, server_move=server_move):
                    self.client.reset_mock()
                    self.client.capabilities = ('MOVE',) if server_move else ()
                    args = () if operation == 'delete' else ('Archive',)
                    result = getattr(self.mailbox, operation)(
                        (uid for uid in (' 1 ', '2')), *args, chunks=1)
                    self.assertEqual(len(result), 2)
                    command = 'COPY' if operation == 'copy' else 'STORE'
                    if operation == 'move':
                        command = 'MOVE' if server_move else 'COPY'
                    self.assertEqual(
                        [c.args[1] for c in self.client.uid.call_args_list if c.args[0] == command],
                        ['1', '2'])

    def test_flag_generators_are_reused_for_all_chunks(self):
        for value in (True, False):
            with self.subTest(value=value):
                self.client.reset_mock()
                self.mailbox.flag(iter(['1', '2']), iter(['\\Seen', 'custom']), value, chunks=1)
                operation = '+FLAGS' if value else '-FLAGS'
                self.assertEqual(self.client.uid.call_args_list, [
                    call('STORE', '1', operation, '(\\Seen custom)'),
                    call('STORE', '2', operation, '(\\Seen custom)'),
                ])

    def test_append_retains_generator_flags(self):
        self.mailbox.append(TEST_MESSAGE_DATA, flag_set=iter(['\\Seen', 'custom']))
        self.assertEqual(self.client.append.call_args.args[1], '(\\Seen custom)')

    def test_invalid_generator_values_do_not_send_commands(self):
        with self.assertRaises(TypeError):
            self.mailbox.copy(iter(['1', 'invalid']), 'Archive', chunks=1)
        with self.assertRaises(ValueError):
            self.mailbox.flag(['1', '2'], iter(['\\Seen', '\\Invalid']), True, chunks=1)
        self.client.uid.assert_not_called()

    def test_empty_generator_is_noop(self):
        self.assertIsNone(self.mailbox.copy(iter([]), 'Archive'))
        self.assertIsNone(self.mailbox.flag(iter([]), ['\\Seen'], True))
        self.client.uid.assert_not_called()

    def test_fetch_accepts_uid_generator(self):
        with patch.object(self.mailbox, '_fetch_by_one', return_value=iter([])) as fetch:
            list(self.mailbox.fetch(uid_list=iter(['1', '2'])))
        self.assertEqual(fetch.call_args.args[0], ('1', '2'))


if __name__ == "__main__":
    unittest.main()
