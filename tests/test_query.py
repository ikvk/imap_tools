import unittest
import datetime

from imap_tools import query


class QueryTest(unittest.TestCase):
    """
    # Messages with the specified keyword flag set. (KEYWORD)
    KEYWORD=str <flag> 
    # Messages that do not have the specified keyword flag set. (UNKEYWORD)
    NO_KEYWORD=str <flag>
    
    # Messages that contain the specified string in the envelope structure's FROM field.
    FROM=str
    # Messages that contain the specified string in the envelope structure's TO field.
    TO=str
    # Messages that contain the specified string in the envelope structure's SUBJECT field.
    SUBJECT=str
    # Messages that contain the specified string in the body of the message.
    BODY=str
    # Messages that contain the specified string in the header or body of the message.
    TEXT=str
    # Messages that contain the specified string in the envelope structure's BCC field.
    BCC=str
    # Messages that contain the specified string in the envelope structure's CC field.
    CC=str
    
    # Messages whose internal date (disregarding time and timezone) is within the specified date. (ON)
    DATE=date
    # Messages whose internal date (disregarding time and timezone) is within or later than the specified date. (SINCE)
    DATE_GT=date
    # Messages whose internal date (disregarding time and timezone) is earlier than the specified date. (BEFORE)
    DATE_LT=date
    # Messages whose [RFC-2822] Date: header (disregarding time and timezone) is within the specified date. (SENTON)
    SENT_DATE=date
    # Messages whose [RFC-2822] Date: header (disregarding time and timezone) is within or later than the specified date. (SENTSINCE)
    SENT_DATE_GT=date
    # Messages whose [RFC-2822] Date: header (disregarding time and timezone) is earlier than the specified date. (SENTBEFORE)
    SENT_DATE_LT=date
    
    # Messages with an [RFC-2822] size larger than the specified number of octets. (LARGER)
    SIZE_GT=int
    # Messages with an [RFC-2822] size smaller than the specified number of octets. (SMALLER)
    SIZE_LT=int
    
    # Messages that have the \Recent flag set but not the \Seen flag. This is functionally equivalent to "(RECENT UNSEEN)".
    NEW=True
    # Messages that do not have the \Recent flag set. This is functionally equivalent to "NOT RECENT" (as opposed to "NOT NEW").
    OLD=True
    # Messages that have the \Recent flag set.
    RECENT=True
    # by default ALL 
    ALL=True
    
    # Messages that have a header with the specified field-name (as defined in [RFC-2822]) 
    # and that contains the specified string in the text of the header (what comes after the colon).  
    # If the string to search is zero-length, this matches all messages that have a header line 
    # with the specified field-name regardless of the contents.
    HEADER=(<field-name>:str, str)
    
    Messages with unique identifiers corresponding to the specified unique identifier set. Sequence set ranges are permitted.
    UID=<uid_list>: list

    """

    def test_converters(self):
        for key, case_set in (
                ('answered', [(True, 'ANSWERED'), (False, 'UNANSWERED')]),
                ('seen', [(True, 'SEEN'), (False, 'UNSEEN')]),
                ('flagged', [(True, 'FLAGGED'), (False, 'UNFLAGGED')]),
                ('draft', [(True, 'DRAFT'), (False, 'UNDRAFT')]),
                ('deleted', [(True, 'DELETED'), (False, 'UNDELETED')]),
                ('keyword', [(1, ''), (2, '')]),
                ('no_keyword', [(1, ''), (2, '')]),
                ('from_', [(1, ''), (2, '')]),
                ('to', [(1, ''), (2, '')]),
                ('subject', [(1, ''), (2, '')]),
                ('body', [(1, ''), (2, '')]),
                ('text', [(1, ''), (2, '')]),
                ('bcc', [(1, ''), (2, '')]),
                ('cc', [(1, ''), (2, '')]),
                ('date', [(1, ''), (2, '')]),
                ('date_gt', [(1, ''), (2, '')]),
                ('date_lt', [(1, ''), (2, '')]),
                ('sent_date', [(1, ''), (2, '')]),
                ('sent_date_gt', [(1, ''), (2, '')]),
                ('sent_date_lt', [(1, ''), (2, '')]),
                ('size_gt', [(1, ''), (2, '')]),
                ('size_lt', [(1, ''), (2, '')]),
                ('new', [(1, ''), (2, '')]),
                ('old', [(1, ''), (2, '')]),
                ('recent', [(1, ''), (2, '')]),
                ('all', [(1, ''), (2, '')]),
                ('header', [(1, ''), (2, '')]),
                ('uid', '')):
            for value, result in case_set:
                self.assertEqual(1, 1) # todo stop

    def test_cleaners(self):
        def fetch():
            class A:
                uid = '1'

            yield A()

        def not_fetch():
            yield 1

        for cleaned_fn_name, good_vals, bad_vals in (
                ('cleaned_bool', (True, False), (1, 'str', [], {}, type, b'1')),
                ('cleaned_date', (datetime.date.today(),), (datetime.datetime.now(), 1, 's', [], {}, type, True, b'1')),
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





























format_date
to_str
'''
