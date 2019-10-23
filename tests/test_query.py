import unittest
import datetime as dt

from imap_tools.query import ParamConverter, Q, AND, OR, NOT, H


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
                ('cleaned_date', (dt.date.today(),), (dt.datetime.now(), 1, 's', [], {}, type, True, b'1')),
                ('cleaned_uint', (0, 1, 145), (-1, 'str', [], {}, type, True, b'1')),
                ('cleaned_str', ('', 'good', 'я 你好'), (1, [], {}, type, True, b'1')),
                ('cleaned_true', (True,), (1, 'str', [], {}, type, False, b'1')),
                ('cleaned_uid', ('1', '1,2', ['1', '2'], fetch()), (1, [], {}, type, True, b'1', not_fetch())),
                ('cleaned_header', (H('X-Google-Smtp', '123'), H('a', '1')), (1, 's', ['s', 1], {}, type, False, b'1')),
        ):
            cleaned_fn = getattr(ParamConverter, cleaned_fn_name)
            for good in good_vals:
                self.assertIsNotNone(cleaned_fn('key_does_not_matter', good))
            for bad in bad_vals:
                with self.assertRaises(ValueError):
                    cleaned_fn('key_does_not_matter', bad)

    def test_converters(self):
        self.assertEqual(Q(answered=True), '(ANSWERED)')
        self.assertEqual(Q(answered=False), '(UNANSWERED)')
        self.assertEqual(Q(seen=True), '(SEEN)')
        self.assertEqual(Q(seen=False), '(UNSEEN)')
        self.assertEqual(Q(flagged=True), '(FLAGGED)')
        self.assertEqual(Q(flagged=False), '(UNFLAGGED)')
        self.assertEqual(Q(draft=True), '(DRAFT)')
        self.assertEqual(Q(draft=False), '(UNDRAFT)')
        self.assertEqual(Q(deleted=True), '(DELETED)')
        self.assertEqual(Q(deleted=False), '(UNDELETED)')
        self.assertEqual(Q(keyword='KEY1'), '(KEYWORD KEY1)')
        self.assertEqual(Q(no_keyword='KEY2'), '(UNKEYWORD KEY2)')

        self.assertEqual(Q(from_='from@ya.ru'), '(FROM "from@ya.ru")')
        self.assertEqual(Q(to='to@ya.ru'), '(TO "to@ya.ru")')
        self.assertEqual(Q(subject='hello'), '(SUBJECT "hello")')
        self.assertEqual(Q(body='body text'), '(BODY "body text")')
        self.assertEqual(Q(body='hi'), '(BODY "hi")')
        self.assertEqual(Q(text='"quoted text"'), '(TEXT "\\"quoted text\\"")')
        self.assertEqual(Q(text='hi'), '(TEXT "hi")')
        self.assertEqual(Q(bcc='bcc@ya.ru'), '(BCC "bcc@ya.ru")')
        self.assertEqual(Q(cc='cc@ya.ru'), '(CC "cc@ya.ru")')

        self.assertEqual(Q(date=dt.date(2000, 3, 15)), '(ON 15-Mar-2000)')
        self.assertEqual(Q(date_gte=dt.date(2000, 3, 15)), '(SINCE 15-Mar-2000)')
        self.assertEqual(Q(date_lt=dt.date(2000, 3, 15)), '(BEFORE 15-Mar-2000)')
        self.assertEqual(Q(sent_date=dt.date(2000, 3, 15)), '(SENTON 15-Mar-2000)')
        self.assertEqual(Q(sent_date_gte=dt.date(2000, 3, 15)), '(SENTSINCE 15-Mar-2000)')
        self.assertEqual(Q(sent_date_lt=dt.date(2000, 3, 15)), '(SENTBEFORE 15-Mar-2000)')

        self.assertEqual(Q(size_gt=1024), '(LARGER 1024)')
        self.assertEqual(Q(size_lt=512), '(SMALLER 512)')

        self.assertEqual(Q(new=True), '(NEW)')
        self.assertEqual(Q(old=True), '(OLD)')
        self.assertEqual(Q(recent=True), '(RECENT)')
        self.assertEqual(Q(all=True), '(ALL)')

        self.assertEqual(Q(header=H('X-Google-Smtp-Source', '123')), '(HEADER "X-Google-Smtp-Source" "123")')
        self.assertEqual(Q(uid='1,2'), '(UID 1,2)')
        self.assertEqual(Q(uid=['3', '4']), '(UID 3,4)')

    def test_format_date(self):
        self.assertEqual(ParamConverter.format_date(dt.date(2000, 1, 15)), '15-Jan-2000')
        self.assertEqual(ParamConverter.format_date(dt.date(2000, 12, 15)), '15-Dec-2000')

    def test_logic_operators(self):
        self.assertEqual(AND(text='hello', new=True), '(TEXT "hello" NEW)')
        self.assertEqual(OR(text='hello', new=True), '(OR TEXT "hello" NEW)')
        self.assertEqual(NOT(text='hello', new=True), 'NOT (TEXT "hello" NEW)')
        self.assertEqual(Q(AND(to='one@mail.ru'), AND(to='two@mail.ru')), '((TO "one@mail.ru") (TO "two@mail.ru"))')
        self.assertEqual(
            OR(date=[dt.date(2019, 10, 1), dt.date(2019, 10, 10), dt.date(2019, 10, 15), dt.date(2019, 10, 20)]),
            '(OR OR OR ON 1-Oct-2019 ON 10-Oct-2019 ON 15-Oct-2019 ON 20-Oct-2019)')
        self.assertEqual(
            Q(OR(from_='from@ya.ru', text='"the text"'), NOT(OR(Q(answered=False), Q(new=True))), to='to@ya.ru'),
            '((OR FROM "from@ya.ru" TEXT "\\"the text\\"") NOT ((OR (UNANSWERED) (NEW))) TO "to@ya.ru")')

    def test_header(self):
        header = H('key1', 'val1')
        self.assertEqual(header.name, '"key1"')
        self.assertEqual(header.value, '"val1"')
        with self.assertRaises(ValueError):
            str(H('key1', eval('1')))
        with self.assertRaises(ValueError):
            str(H(eval('1'), 'val1'))
