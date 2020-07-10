import unittest
import datetime as dt

from imap_tools.query import ParamConverter, A, AND, OR, NOT, H


class QueryTest(unittest.TestCase):

    def test_cleaners(self):
        def fetch():
            class Msg:
                uid = '1'

            yield Msg()

        def not_fetch():
            yield 1

        for cleaned_fn_name, good_vals, bad_vals in (
                ('cleaned_bool', (True, False), (1, 'str', [], {}, type, b'1')),
                ('cleaned_date', (dt.date.today(),), (dt.datetime.now(), 1, 's', [], {}, type, True, b'1')),
                ('cleaned_uint', (0, 1, 145), (-1, 'str', [], {}, type, True, b'1')),
                ('cleaned_str', ('', 'good', 'я 你好'), (1, [], {}, type, True, b'1')),
                ('cleaned_true', (True,), (1, 'str', [], {}, type, False, b'1')),
                ('cleaned_uid', ('1', '1,2', ['1', '2'], [], {}, fetch()), (1, type, True, b'1', '', not_fetch())),
                ('cleaned_header', (H('X-Google-Smtp', '123'), H('a', '1')), (1, 's', ['s', 1], {}, type, False, b'1')),
        ):
            cleaned_fn = getattr(ParamConverter, cleaned_fn_name)
            for good in good_vals:
                self.assertIsNotNone(cleaned_fn('key_does_not_matter', good))
            for bad in bad_vals:
                with self.assertRaises(TypeError):
                    cleaned_fn('key_does_not_matter', bad)

    def test_converters(self):
        self.assertEqual(A(answered=True), '(ANSWERED)')
        self.assertEqual(A(answered=False), '(UNANSWERED)')
        self.assertEqual(A(seen=True), '(SEEN)')
        self.assertEqual(A(seen=False), '(UNSEEN)')
        self.assertEqual(A(flagged=True), '(FLAGGED)')
        self.assertEqual(A(flagged=False), '(UNFLAGGED)')
        self.assertEqual(A(draft=True), '(DRAFT)')
        self.assertEqual(A(draft=False), '(UNDRAFT)')
        self.assertEqual(A(deleted=True), '(DELETED)')
        self.assertEqual(A(deleted=False), '(UNDELETED)')
        self.assertEqual(A(keyword='KEY1'), '(KEYWORD KEY1)')
        self.assertEqual(A(no_keyword='KEY2'), '(UNKEYWORD KEY2)')

        self.assertEqual(A(from_='from@ya.ru'), '(FROM "from@ya.ru")')
        self.assertEqual(A(to='to@ya.ru'), '(TO "to@ya.ru")')
        self.assertEqual(A(subject='hello'), '(SUBJECT "hello")')
        self.assertEqual(A(body='body text'), '(BODY "body text")')
        self.assertEqual(A(body='hi'), '(BODY "hi")')
        self.assertEqual(A(text='"quoted text"'), '(TEXT "\\"quoted text\\"")')
        self.assertEqual(A(text='hi'), '(TEXT "hi")')
        self.assertEqual(A(bcc='bcc@ya.ru'), '(BCC "bcc@ya.ru")')
        self.assertEqual(A(cc='cc@ya.ru'), '(CC "cc@ya.ru")')

        self.assertEqual(A(date=dt.date(2000, 3, 15)), '(ON 15-Mar-2000)')
        self.assertEqual(A(date_gte=dt.date(2000, 3, 15)), '(SINCE 15-Mar-2000)')
        self.assertEqual(A(date_lt=dt.date(2000, 3, 15)), '(BEFORE 15-Mar-2000)')
        self.assertEqual(A(sent_date=dt.date(2000, 3, 15)), '(SENTON 15-Mar-2000)')
        self.assertEqual(A(sent_date_gte=dt.date(2000, 3, 15)), '(SENTSINCE 15-Mar-2000)')
        self.assertEqual(A(sent_date_lt=dt.date(2000, 3, 15)), '(SENTBEFORE 15-Mar-2000)')

        self.assertEqual(A(size_gt=1024), '(LARGER 1024)')
        self.assertEqual(A(size_lt=512), '(SMALLER 512)')

        self.assertEqual(A(new=True), '(NEW)')
        self.assertEqual(A(old=True), '(OLD)')
        self.assertEqual(A(recent=True), '(RECENT)')
        self.assertEqual(A(all=True), '(ALL)')

        self.assertEqual(A(header=H('X-Google-Smtp-Source', '123')), '(HEADER "X-Google-Smtp-Source" "123")')
        self.assertEqual(A(uid='1,2'), '(UID 1,2)')
        self.assertEqual(A(uid=['3', '4']), '(UID 3,4)')

        self.assertEqual(A(gmail_label="TestLabel"), '(X-GM-LABELS "TestLabel")')

    def test_format_date(self):
        self.assertEqual(ParamConverter.format_date(dt.date(2000, 1, 15)), '15-Jan-2000')
        self.assertEqual(ParamConverter.format_date(dt.date(2000, 12, 15)), '15-Dec-2000')

    def test_logic_operators(self):
        self.assertEqual(AND(text='hello', new=True), '(TEXT "hello" NEW)')
        self.assertEqual(OR(text='hello', new=True), '(OR TEXT "hello" NEW)')
        self.assertEqual(NOT(text='hello', new=True), 'NOT (TEXT "hello" NEW)')
        self.assertEqual(A(AND(to='one@mail.ru'), AND(to='two@mail.ru')), '((TO "one@mail.ru") (TO "two@mail.ru"))')
        self.assertEqual(
            OR(date=[dt.date(2019, 10, 1), dt.date(2019, 10, 10), dt.date(2019, 10, 15), dt.date(2019, 10, 20)]),
            '(OR OR OR ON 1-Oct-2019 ON 10-Oct-2019 ON 15-Oct-2019 ON 20-Oct-2019)')
        self.assertEqual(
            A(OR(from_='from@ya.ru', text='"the text"'), NOT(OR(A(answered=False), A(new=True))), to='to@ya.ru'),
            '((OR FROM "from@ya.ru" TEXT "\\"the text\\"") NOT ((OR (UNANSWERED) (NEW))) TO "to@ya.ru")')

    def test_header(self):
        header = H('key1', 'val1')
        self.assertEqual(header.name, '"key1"')
        self.assertEqual(header.value, '"val1"')
        with self.assertRaises(TypeError):
            str(H('key1', eval('1')))
        with self.assertRaises(TypeError):
            str(H(eval('1'), 'val1'))
