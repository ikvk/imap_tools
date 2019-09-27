import unittest
import datetime

from imap_tools import query


class QueryTest(unittest.TestCase):

    def test_converters(self):
        self.assertEqual(1, 1)

    def test_cleaners(self):
        def fetch():
            class A:
                uid = '1'
            yield A()

        def not_fetch():
            yield 1

        for cleaned_fn_name, good_vals, bad_vals in (
                ('cleaned_bool', (True, False), (1, 'str', [], {}, type, b'1')),
                ('cleaned_date', (datetime.date(2000, 10, 15),), (1, 'str', [], {}, type, True, b'1')),
                ('cleaned_uint', (0, 1, 145), (-1, 'str', [], {}, type, True, b'1')),
                ('cleaned_str', ('', 'good', 'я 你好'), (1, [], {}, type, True, b'1')),
                ('cleaned_true', (True,), (1, 'str', [], {}, type, False, b'1')),
                ('cleaned_uid', ('1', '1,2', ['1', '2'], fetch()), (1, [], {}, type, True, b'1', not_fetch())),):
            cleaned_fn = getattr(query.ParamConverter, cleaned_fn_name)
            for good in good_vals:
                self.assertIsNotNone(cleaned_fn('key_does_not_matter', good))
            for bad in bad_vals:
                with self.assertRaises(ValueError):
                    cleaned_fn('key_does_not_matter', bad)

    def test_format_date(self):
        self.assertEqual(1, 1)


'''
ParamConverter
__init__
cleaned_bool
cleaned_date
cleaned_uint
cleaned_str
cleaned_true
cleaned_uid

convert_all
convert_answered
convert_bcc
convert_body
convert_cc
convert_date
convert_date_gt
convert_date_lt
convert_deleted
convert_draft
convert_flagged
convert_from_
convert_header
convert_keyword
convert_new
convert_no_keyword
convert_old
convert_recent
convert_seen
convert_sent_date
convert_sent_date_gt
convert_sent_date_lt
convert_size_gt
convert_size_lt
convert_subject
convert_text
convert_to
convert_uid
format_date
to_str
'''
