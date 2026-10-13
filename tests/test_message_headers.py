import unittest

from imap_tools import MailMessage
from imap_tools.utils import EmailAddress


class AddressDisplayNameTest(unittest.TestCase):
    def test_all_address_properties_keep_complete_display_names(self):
        cases = (
            ('Team =?utf-8?q?M=C3=BCnchen?=', 'Team München'),
            ('=?utf-8?q?J=C3=B6rg?= Example', 'Jörg Example'),
            ('=?iso-8859-1?q?Andr=E9?= =?utf-8?q?_M=C3=BCller?=', 'André Müller'),
            ('=?utf-8?q?Doe=2C_Jane?= Team', 'Doe, Jane Team'),
            ('Team\r\n =?utf-8?q?M=C3=BCnchen?=', 'Team München'),
        )
        for raw_name, expected in cases:
            with self.subTest(raw_name=raw_name):
                raw_value = raw_name + ' <person@example.com>'
                raw = '\r\n'.join(
                    name + ': ' + raw_value for name in ('From', 'To', 'Cc', 'Bcc', 'Reply-To'))
                message = MailMessage.from_bytes((raw + '\r\n\r\nBody').encode('ascii'))
                address = EmailAddress(expected, 'person@example.com')
                self.assertEqual(message.from_values, address)
                for attr in ('to_values', 'cc_values', 'bcc_values', 'reply_to_values'):
                    self.assertEqual(getattr(message, attr), (address,))
                # The raw-header interface deliberately keeps encoded words.
                self.assertIn('=?', message.headers['from'][0])

    def test_raw_utf8_header_keeps_existing_decoding(self):
        message = MailMessage.from_bytes('From: André <person@example.com>\r\n\r\nBody'.encode('utf-8'))
        self.assertEqual(message.from_values, EmailAddress('André', 'person@example.com'))

    def test_repeated_recipients_and_plain_names(self):
        message = MailMessage.from_bytes(
            b'To: Team =?utf-8?q?M=C3=BCnchen?= <team@example.com>\r\n'
            b'To: Plain Name <plain@example.com>\r\n\r\nBody')
        self.assertEqual(message.to_values, (
            EmailAddress('Team München', 'team@example.com'),
            EmailAddress('Plain Name', 'plain@example.com'),
        ))
        self.assertEqual(message.to, ('team@example.com', 'plain@example.com'))
