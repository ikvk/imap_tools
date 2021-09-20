import unittest
import datetime

from imap_tools.errors import ImapToolsError, UnexpectedCommandStatusError, MailboxCopyError
from imap_tools.consts import MailMessageFlags
from imap_tools.utils import clean_flags, chunks, quote, pairs_to_dict, decode_value, check_command_status, \
    parse_email_date, parse_email_addresses, EmailAddress


class UtilsTest(unittest.TestCase):

    def test_clean_uids(self):
        # *clean_uids tested enough in test_query.py
        pass

    def test_clean_flags(self):
        self.assertEqual(clean_flags([MailMessageFlags.FLAGGED, MailMessageFlags.SEEN]), ['\\Flagged', '\\Seen'])
        self.assertEqual(clean_flags(['\\FLAGGED', '\\seen']), ['\\FLAGGED', '\\seen'])
        self.assertEqual(clean_flags(['TAG1']), ['TAG1'])
        self.assertEqual(clean_flags(['tag2']), ['tag2'])
        for flag in MailMessageFlags.all:
            self.assertEqual(clean_flags(flag), ['\\' + flag.replace('\\', '', 1).capitalize()])
        with self.assertRaises(ValueError):
            clean_flags([MailMessageFlags.FLAGGED, '\\CUSTOM_TAG_WITH_SLASH'])

    def test_chunks(self):
        self.assertEqual(list(chunks('ABCDE', 2, '=')), [('A', 'B'), ('C', 'D'), ('E', '=')])
        self.assertEqual(list(chunks([1, 2, 3, 4, 5, 6], 3)), [(1, 2, 3), (4, 5, 6)])
        self.assertEqual(list(chunks([], 4)), [])
        self.assertEqual(list(chunks([1, 2], 0)), [])
        self.assertEqual(list(chunks(['0', '0'], 1)), [('0',), ('0',)])

    def test_quote(self):
        self.assertEqual(quote('str привет'), '"str привет"')
        self.assertEqual(quote('str \\'), '"str \\\\"')
        self.assertEqual(quote(b'\xd1\x8f'), b'"\xd1\x8f"')
        self.assertEqual(quote(b'\\ \xd1\x8f  \\'), b'"\\\\ \xd1\x8f  \\\\"')

    def test_pairs_to_dict(self):
        self.assertEqual(pairs_to_dict(['MESSAGES', '3', 'UIDNEXT', '4']), {'MESSAGES': '3', 'UIDNEXT': '4'})
        with self.assertRaises(ValueError):
            pairs_to_dict(['1', '2', '3'])

    def test_decode_value(self):
        self.assertEqual(decode_value('str привет 你好', 'not matter'), 'str привет 你好')
        self.assertEqual(decode_value(b'str \xd0\xb4\xd0\xb0 \xe4\xbd\xa0'), 'str да 你')
        self.assertEqual(decode_value(b'str \xd0\xb4\xd0\xb0 \xe4\xbd\xa0', 'utf8'), 'str да 你')
        self.assertEqual(decode_value(b'\xef\xf0\xe8\xe2\xe5\xf2', 'cp1251'), 'привет')
        self.assertEqual(decode_value(b'str \xd0\xb4\xd0\xb0 \xe4\xbd\xa0', 'wat?'), 'str да 你')

    def test_check_command_status(self):
        self.assertIsNone(check_command_status(('EXP', 'command_result_data'), MailboxCopyError, expected='EXP'))
        self.assertIsNone(check_command_status(('OK', 'res'), UnexpectedCommandStatusError))
        with self.assertRaises(TypeError):
            check_command_status(('NOT_OK', 'test'), ImapToolsError)
        with self.assertRaises(MailboxCopyError):
            check_command_status(('BYE', ''), MailboxCopyError, expected='OK')

    def test_parse_email_date(self):
        for val, exp in (
                ('1 Jan 2000 00:00', datetime.datetime(2000, 1, 1, 0, 0)),
                ('1 Feb 2000 00:00', datetime.datetime(2000, 2, 1, 0, 0)),
                ('1 Mar 2000 00:00', datetime.datetime(2000, 3, 1, 0, 0)),
                ('1 Apr 2000 00:00', datetime.datetime(2000, 4, 1, 0, 0)),
                ('1 May 2000 00:00', datetime.datetime(2000, 5, 1, 0, 0)),
                ('1 Jun 2000 00:00', datetime.datetime(2000, 6, 1, 0, 0)),
                ('1 Jul 2000 00:00', datetime.datetime(2000, 7, 1, 0, 0)),
                ('1 Aug 2000 00:00', datetime.datetime(2000, 8, 1, 0, 0)),
                ('1 Sep 2000 00:00', datetime.datetime(2000, 9, 1, 0, 0)),
                ('1 Oct 2000 00:00', datetime.datetime(2000, 10, 1, 0, 0)),
                ('1 Nov 2000 00:00', datetime.datetime(2000, 11, 1, 0, 0)),
                ('1 Dec 2000 00:00', datetime.datetime(2000, 12, 1, 0, 0)),

                ('=) wat 7 Jun 2017 09:23!',
                 datetime.datetime(2017, 6, 7, 9, 23)),
                ('7 Jun 2017 09:23',
                 datetime.datetime(2017, 6, 7, 9, 23)),
                ('Wed, 7 Jun 2017 09:23',
                 datetime.datetime(2017, 6, 7, 9, 23)),
                ('Wed, 7 Jun 2017 09:23:14',
                 datetime.datetime(2017, 6, 7, 9, 23, 14)),
                ('Wed, 7 Jun 2017 09:23:14 +0000',
                 datetime.datetime(2017, 6, 7, 9, 23, 14, tzinfo=datetime.timezone.utc)),
                ('Wed, 7 Jun 2017 09:23:14 +0000 (UTC)',
                 datetime.datetime(2017, 6, 7, 9, 23, 14, tzinfo=datetime.timezone.utc)),
                ('Wed, 7 Jun 2017 09:23 +0000',
                 datetime.datetime(2017, 6, 7, 9, 23, tzinfo=datetime.timezone.utc)),
                ('Wed, 7 Jun 2017 09:23 +0000 (UTC)',
                 datetime.datetime(2017, 6, 7, 9, 23, tzinfo=datetime.timezone.utc)),
                ('7 Jun 2017 09:23 +0000',
                 datetime.datetime(2017, 6, 7, 9, 23, tzinfo=datetime.timezone.utc)),
                ('7 Jun 2017 09:23 +0000 (UTC)',
                 datetime.datetime(2017, 6, 7, 9, 23, tzinfo=datetime.timezone.utc)),
                ('7 Jun 2017 09:23 -2359',
                 datetime.datetime(2017, 6, 7, 9, 23, tzinfo=datetime.timezone(datetime.timedelta(-1, 60)))),
                ('7 Jun 2017 09:23 +0530 (UTC) asd',
                 datetime.datetime(2017, 6, 7, 9, 23, tzinfo=datetime.timezone(datetime.timedelta(0, 19800)))),

                ('7 Bad 2017 09:23', datetime.datetime(1900, 1, 1, 0, 0)),
        ):
            self.assertEqual(parse_email_date(val), exp)

    def test_parse_email_addresses(self):
        self.assertEqual(
            parse_email_addresses('=?UTF-8?B?0J7Qu9C1=?= <name@company.ru>,\r\n "\'\\"z, z\\"\'" <ya@ya.ru>\f'),
            (EmailAddress('Оле', 'name@company.ru', 'Оле <name@company.ru>'),
             EmailAddress('\'"z, z"\'', 'ya@ya.ru', '\'"z, z"\' <ya@ya.ru>'))
        )
        self.assertEqual(
            parse_email_addresses(' <ivan@mail.ru>'),
            (EmailAddress('', 'ivan@mail.ru', 'ivan@mail.ru'),)
        )
        self.assertEqual(
            parse_email_addresses('ivan'),
            (EmailAddress('', '', 'ivan'),)  # *в этом случае ivan считается email-ом
        )
        self.assertEqual(
            parse_email_addresses('你好 <chan@mail.ru>'),
            (EmailAddress('你好', 'chan@mail.ru', '你好 <chan@mail.ru>'),)
        )
        self.assertEqual(
            parse_email_addresses(' "hi" <bad_mail.wow> '),
            (EmailAddress('hi', '', 'hi <bad_mail.wow>'),)
        )
        self.assertEqual(
            parse_email_addresses('=?utf-8?Q?ATO.RU?= <subscriptions@ato.ru>'),
            (EmailAddress('ATO.RU', 'subscriptions@ato.ru', 'ATO.RU <subscriptions@ato.ru>'),)
        )
