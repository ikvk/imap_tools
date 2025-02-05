import unittest
import datetime
import unicodedata

from imap_tools.errors import ImapToolsError, UnexpectedCommandStatusError, MailboxCopyError
from imap_tools.consts import MailMessageFlags
from imap_tools.utils import clean_flags, chunked, quote, pairs_to_dict, decode_value, check_command_status, \
    parse_email_date, parse_email_addresses, EmailAddress, clean_uids, replace_html_ct_charset, chunked_crop, \
    remove_non_printable


class UtilsTest(unittest.TestCase):

    def test_remove_non_printable(self):
        all_non_printable_chars = []
        for i in range(0x110000):  # Диапазон всех кодовых точек Unicode
            char = chr(i)
            if unicodedata.category(char).startswith('C'):
                all_non_printable_chars.append(char)
        self.assertEqual(remove_non_printable('123{}'.format(''.join(all_non_printable_chars))), '123')

    def test_clean_uids(self):
        # *clean_uids also implicitly tested in test_query.py
        self.assertEqual(clean_uids('11'), ['11'])
        self.assertEqual(clean_uids('1,2'), ['1', '2'])
        self.assertEqual(clean_uids(' 1,2, 4 '), ['1', '2', '4'])
        self.assertEqual(clean_uids('1,222'), ['1', '222'])
        self.assertEqual(clean_uids('1,2:*'), ['1', '2:*'])
        for i in ['', 1, 1.0, dict(a=1)]:
            with self.assertRaises(TypeError):
                clean_uids(i)  # noqa

    def test_clean_flags(self):
        self.assertEqual(clean_flags([MailMessageFlags.FLAGGED, MailMessageFlags.SEEN]), ['\\Flagged', '\\Seen'])
        self.assertEqual(clean_flags(['\\FLAGGED', '\\seen']), ['\\FLAGGED', '\\seen'])
        self.assertEqual(clean_flags(['TAG1']), ['TAG1'])
        self.assertEqual(clean_flags(['tag2']), ['tag2'])
        for flag in MailMessageFlags.all:
            self.assertEqual(clean_flags(flag), ['\\' + flag.replace('\\', '', 1).capitalize()])
        with self.assertRaises(ValueError):
            clean_flags([MailMessageFlags.FLAGGED, '\\CUSTOM_TAG_WITH_SLASH'])

    def test_chunked(self):
        self.assertEqual(list(chunked('ABCDE', 2, '=')), [('A', 'B'), ('C', 'D'), ('E', '=')])
        self.assertEqual(list(chunked([1, 2, 3, 4, 5, 6], 3)), [(1, 2, 3), (4, 5, 6)])
        self.assertEqual(list(chunked([], 4)), [])
        self.assertEqual(list(chunked([1, 2], 0)), [])
        self.assertEqual(list(chunked(['0', '0'], 1)), [('0',), ('0',)])

    def test_chunked_crop(self):
        self.assertEqual(list(chunked_crop([1, 2, 3, 4, 5, 6, 7], 3)), [[1, 2, 3], [4, 5, 6], [7]])
        self.assertEqual(list(chunked_crop([1, 2, 3, 4, 5, 6], 3)), [[1, 2, 3], [4, 5, 6]])
        self.assertEqual(list(chunked_crop([1, ], 3)), [[1]])
        self.assertEqual(list(chunked_crop([1], 0)), [[1]])
        self.assertEqual(list(chunked_crop([1, 2], False)), [[1, 2]])
        self.assertEqual(list(chunked_crop([1, 2, 3], None)), [[1, 2, 3]])
        with self.assertRaises(ValueError):
            list(chunked_crop([1], -1))

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
            (EmailAddress('Оле', 'name@company.ru'),
             EmailAddress('\'"z, z"\'', 'ya@ya.ru'))
        )
        self.assertEqual(
            parse_email_addresses(' <ivan@mail.ru>'),
            (EmailAddress('', 'ivan@mail.ru'),)
        )
        self.assertEqual(
            parse_email_addresses('ivan'),
            (EmailAddress('ivan', ''),)
        )
        self.assertEqual(
            parse_email_addresses('你好 <chan@mail.ru>'),
            (EmailAddress('你好', 'chan@mail.ru'),)
        )
        self.assertEqual(
            parse_email_addresses(' "hi" <bad_mail.wow> '),
            (EmailAddress('hi', ''),)
        )
        self.assertEqual(
            parse_email_addresses('=?utf-8?Q?ATO.RU?= <subscriptions@ato.ru>'),
            (EmailAddress('ATO.RU', 'subscriptions@ato.ru'),)
        )

    def test_replace_html_ct_charset(self):
        target = 'charset=utf-8'

        data1 = """
          <head>
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <meta http-equiv="content-type" content="text/html; charset=windows-1251">
            <meta name="author" content="cat charset=windows-123">
          </head>
        """
        res1 = replace_html_ct_charset(data1, 'utf-8')
        self.assertIn(target, res1)
        self.assertTrue(res1.count(target) == 1)

        data2 = """
          <head>
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            < 
            META 
             http-EQUIV="
             Content-TYPE " content="text/html; charset 
             = 
             WINDOWS-1251+ ;"/>
            <meta name="author" content="cat charset=windows-123">
          </head>
        """
        res2 = replace_html_ct_charset(data2, 'utf-8')
        self.assertIn(target, res2)
        self.assertTrue(res2.count(target) == 1)
