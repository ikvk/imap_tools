import unittest

from imap_tools import query


class QueryTest(unittest.TestCase):

    def test_converters(self):
        self.assertEqual(1, 1)

    def test_cleaners(self):
        self.assertEqual(1, 1)

    def test_format_date(self):
        self.assertEqual(1, 1)


'''
ParamConverter
__init__
cleaned_bool
cleaned_date
cleaned_int
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
