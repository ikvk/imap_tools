import unittest
import datetime

from imap_tools import query


class QueryTest(unittest.TestCase):

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
                ('cleaned_uid', ('1', '1,2', ['1', '2'], fetch()), (1, [], {}, type, True, b'1', not_fetch())),
                ('cleaned_header', (('X-Google-Smtp', '123'), ['a', '1']), (1, 's', ['s', 1], {}, type, False, b'1')),
        ):
            cleaned_fn = getattr(query.ParamConverter, cleaned_fn_name)
            for good in good_vals:
                self.assertIsNotNone(cleaned_fn('key_does_not_matter', good))
            for bad in bad_vals:
                with self.assertRaises(ValueError):
                    cleaned_fn('key_does_not_matter', bad)

    def test_converters(self):
        for key, case_set in (
                ('answered', [(True, 'ANSWERED'), (False, 'UNANSWERED')]),
                ('seen', [(True, 'SEEN'), (False, 'UNSEEN')]),
                ('flagged', [(True, 'FLAGGED'), (False, 'UNFLAGGED')]),
                ('draft', [(True, 'DRAFT'), (False, 'UNDRAFT')]),
                ('deleted', [(True, 'DELETED'), (False, 'UNDELETED')]),
                ('keyword', [('KEY', 'KEYWORD KEY'), ('Some', 'KEYWORD Some')]),
                ('no_keyword', [('noo', 'UNKEYWORD noo'), ('Some', 'UNKEYWORD Some')]),
                ('from_', [('from@ya.ru', 'FROM from@ya.ru')]),
                ('to', [('to@ya.ru', 'TO to@ya.ru')]),
                ('subject', [('hello', 'SUBJECT hello')]),
                ('body', [('"body text"', 'BODY "body text"'), ('hi', 'BODY hi')]),
                ('text', [('"wow text"', 'TEXT "wow text"'), ('hi', 'TEXT hi')]),
                ('bcc', [('bcc@ya.ru', 'BCC bcc@ya.ru')]),
                ('cc', [('cc@ya.ru', 'CC cc@ya.ru')]),
                ('date', [(datetime.date(2000, 3, 15), 'ON 15-Mar-2000')]),
                ('date_gt', [(datetime.date(2000, 3, 15), 'SINCE 15-Mar-2000')]),
                ('date_lt', [(datetime.date(2000, 3, 15), 'BEFORE 15-Mar-2000')]),
                ('sent_date', [(datetime.date(2000, 3, 15), 'SENTON 15-Mar-2000')]),
                ('sent_date_gt', [(datetime.date(2000, 3, 15), 'SENTSINCE 15-Mar-2000')]),
                ('sent_date_lt', [(datetime.date(2000, 3, 15), 'SENTBEFORE 15-Mar-2000')]),
                ('size_gt', [(1024, 'LARGER 1024')]),
                ('size_lt', [(512, 'SMALLER 512')]),
                ('new', [(True, 'NEW')]),
                ('old', [(True, 'OLD')]),
                ('recent', [(True, 'RECENT')]),
                ('all', [(True, 'ALL')]),
                ('header', [(('X-Google-Smtp-Source', '123'), 'HEADER X-Google-Smtp-Source 123')]),
                ('uid', [('1,2', 'UID 1,2'), (['3', '4'], 'UID 3,4')]),
        ):
            for value, result in case_set:
                self.assertEqual(query.AND(key=value), result)

    def test_format_date(self):
        self.assertEqual(query.ParamConverter.format_date(datetime.date(2000, 3, 15)), '15-Mar-2000')

    def test_logic_operators(self):
        pass
        # to_str
        # todo stop here
