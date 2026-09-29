import os
import tempfile
import unittest

from imap_tools import MailMessage
from imap_tools.contacts import (
    ContactInfo,
    collect_from_message,
    folder_scan_mode,
    normalize_email,
    write_contacts_csv,
)
from imap_tools.folder import FolderInfo


class ContactsTest(unittest.TestCase):

    def test_normalize_email(self):
        self.assertEqual(normalize_email('  Foo@Bar.COM '), 'foo@bar.com')

    def test_folder_scan_mode(self):
        self.assertEqual(folder_scan_mode(FolderInfo('INBOX', '/', ('\\Inbox',))), 'inbound')
        self.assertEqual(folder_scan_mode(FolderInfo('Sent', '/', ('\\Sent',))), 'outbound')
        self.assertEqual(folder_scan_mode(FolderInfo('Archive', '/', ()),), 'both')

    def test_collect_from_simple_eml(self):
        eml_path = os.path.join(os.path.dirname(__file__), 'messages', 'rfc2822', 'example02.eml')
        with open(eml_path, 'rb') as fh:
            msg = MailMessage.from_bytes(fh.read())
        contacts = {}
        collect_from_message(contacts, msg, 'INBOX', 'inbound', exclude=set(), skip_noise=True)
        self.assertIn('jdoe@machine.example', contacts)
        self.assertEqual(contacts['jdoe@machine.example'].inbound_count, 1)
        self.assertEqual(contacts['jdoe@machine.example'].outbound_count, 0)

    def test_collect_outbound_mode(self):
        eml_path = os.path.join(os.path.dirname(__file__), 'messages', 'rfc2822', 'example02.eml')
        with open(eml_path, 'rb') as fh:
            msg = MailMessage.from_bytes(fh.read())
        contacts = {}
        collect_from_message(contacts, msg, 'Sent', 'outbound', exclude=set(), skip_noise=True)
        self.assertIn('mary@example.net', contacts)
        self.assertEqual(contacts['mary@example.net'].outbound_count, 1)

    def test_exclude_and_noise(self):
        eml_path = os.path.join(os.path.dirname(__file__), 'messages', 'multipart_report_emails', 'report_530.eml')
        with open(eml_path, 'rb') as fh:
            msg = MailMessage.from_bytes(fh.read())
        contacts = {}
        collect_from_message(contacts, msg, 'INBOX', 'inbound', exclude=set(), skip_noise=True)
        self.assertNotIn('mailer-daemon@tttttt.com.au', contacts)

    def test_write_contacts_csv(self):
        contacts = {
            'a@b.com': ContactInfo('a@b.com', 'Alice'),
        }
        contacts['a@b.com'].inbound_count = 2
        contacts['a@b.com'].folders.add('INBOX')
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False, encoding='utf-8') as tmp:
            path = tmp.name
        try:
            write_contacts_csv(path, contacts)
            with open(path, encoding='utf-8') as fh:
                text = fh.read()
            self.assertIn('a@b.com', text)
            self.assertIn('Alice', text)
        finally:
            os.unlink(path)


if __name__ == '__main__':
    unittest.main()
