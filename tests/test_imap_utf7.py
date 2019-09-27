import unittest

from imap_tools import imap_utf7


class ImapUtf7Test(unittest.TestCase):
    data = (
        ('Test', b'Test'),
        ('Test One more', b'Test One more'),
        ('Might & Magic', b'Might &- Magic'),
        ('Might & magic', b'Might &- magic'),
        ('Imap&\xffworld', b'Imap&-&AP8-world'),
        ('\xff\xfe\xfd\xfc', b'&AP8A,gD9APw-'),
        ('\x00', b'&AAA-'),
        ('hello, Jackie Chan 你好，成龙', b'hello, Jackie Chan &T2BZff8MYhCfmQ-'),  # RFC-2060
        ('str \t\n\r\f\vwhitespace \t\n\r\f\v', b'str &AAkACgANAAwACw-whitespace &AAkACgANAAwACw-')
    )

    def test_encode(self):
        for string, code in self.data:
            self.assertEqual(imap_utf7.encode(string), code)

    def test_decode(self):
        for string, code in self.data:
            self.assertEqual(string, imap_utf7.decode(code))

    def test_printable_chars(self):
        for code in range(32, 127):
            if code == 38:  # &
                continue
            self.assertEqual(bytes((code,)), imap_utf7.encode(chr(code)))
            self.assertEqual(chr(code), imap_utf7.decode(bytes((code,))))
        self.assertEqual(imap_utf7.encode('&'), b'&-')
        self.assertEqual(imap_utf7.decode(b'&-'), '&')
