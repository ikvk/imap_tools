import unittest
import datetime

from imap_tools import utils


class UtilsTest(unittest.TestCase):

    # *cleaned_uid_set tested enough in test_query

    def test_decode_value(self):
        # todo
        def1 decode_value(value, encoding) -> str:
            """Converts value to utf-8 encoding"""
            if isinstance(value, bytes):
                if encoding in ['utf-8', None]:
                    return value.decode('utf-8', 'ignore')
                else:
                    try:
                        return value.decode(encoding)
                    except LookupError:  # unknown encoding
                        return value.decode('utf-8', 'ignore')
            return value

    def test_check_command_status(self):
        self.assertIsNone(utils.check_command_status('box.fetch', ('EXP', 'command_result_data'), expected='EXP'))
        self.assertIsNone(utils.check_command_status('test', ('OK', 'res')))
        with self.assertRaises(utils.UnexpectedCommandStatusError):
            self.assertFalse(utils.check_command_status('test', ('NOT_OK', 'test')))
        with self.assertRaises(utils.UnexpectedCommandStatusError):
            self.assertFalse(utils.check_command_status('box.logout', ('BYE', ''), 'OK'))

    def test_parse_email_date(self):
        for val, exp in (
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
        ):
            self.assertEqual(utils.parse_email_date(val), exp)

    def test_parse_email_address(self):
        self.assertEqual(
            utils.parse_email_address('"Ivan Petrov" <ivan@mail.ru>'),
            {'email': 'ivan@mail.ru', 'name': '"Ivan Petrov"', 'full': '"Ivan Petrov" <ivan@mail.ru>'})
        self.assertEqual(
            utils.parse_email_address(' <ivan@mail.ru>'),
            {'email': 'ivan@mail.ru', 'name': '', 'full': ' <ivan@mail.ru>'})
        self.assertEqual(
            utils.parse_email_address('你好 <chan@mail.ru>'),
            {'email': 'chan@mail.ru', 'name': '你好', 'full': '你好 <chan@mail.ru>'})
