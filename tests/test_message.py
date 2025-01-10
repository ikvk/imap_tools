import os
import sys
import unittest
import datetime
from tests.utils import MailboxTestCase

from imap_tools import MailMessage, MailMessageFlags, EmailAddress
from imap_tools.consts import PYTHON_VERSION_MINOR


def _load_module(full_path: str):
    module_name = ''
    if sys.version_info.minor >= 5:
        import importlib.util
        spec = importlib.util.spec_from_file_location(module_name, full_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)  # noqa
        return module
    else:
        from importlib.machinery import SourceFileLoader
        return SourceFileLoader(module_name, full_path).load_module()  # noqa


class MessageTest(MailboxTestCase):

    def test_live(self):
        none_type = type(None)
        for mailbox in self.mailbox_set.values():
            mailbox.folder.set(mailbox.folder_test_base)
            flag_set = {MailMessageFlags.ANSWERED, MailMessageFlags.FLAGGED}

            # headers_only
            cnt_fetch_all_head = 0
            cnt_fetch_all_head_answered_and_flagged = 0
            for message in mailbox.fetch(headers_only=True):
                if flag_set.issubset(message.flags):
                    cnt_fetch_all_head_answered_and_flagged += 1
                cnt_fetch_all_head += 1
                self.assertEqual(message.text, '')
                self.assertEqual(message.html, '')
                self.assertEqual(len(message.attachments), 0)

            # fetch in bulk
            cnt_fetch_all_bulk = 0
            cnt_fetch_all_bulk_answered_and_flagged = 0
            for message in mailbox.fetch(bulk=True):
                if flag_set.issubset(message.flags):
                    cnt_fetch_all_bulk_answered_and_flagged += 1
                cnt_fetch_all_bulk += 1

            # fetch by one, types
            cnt_fetch_all = 0
            cnt_fetch_all_answered_and_flagged = 0
            for message in mailbox.fetch():
                if flag_set.issubset(message.flags):
                    cnt_fetch_all_answered_and_flagged += 1
                cnt_fetch_all += 1
                self.assertIn(type(message.uid), (str, none_type))
                self.assertIs(type(message.subject), str)
                self.assertIs(type(message.from_), str)
                self.assertIn(type(message.from_values), (EmailAddress, none_type))
                self.assertIs(type(message.date), datetime.datetime)
                self.assertIs(type(message.date_str), str)
                self.assertIs(type(message.text), str)
                self.assertIs(type(message.html), str)
                self.assertIs(type(message.headers), dict)
                self.assertIs(type(message.size_rfc822), int)
                self.assertIs(type(message.size), int)

                for addr_field in {'to', 'cc', 'bcc', 'reply_to'}:
                    self.assertIs(type(getattr(message, addr_field)), tuple)
                    for i in getattr(message, addr_field):
                        self.assertIs(type(i), str)
                    self.assertIs(type(getattr(message, '{}_values'.format(addr_field))), tuple)
                    for i in getattr(message, '{}_values'.format(addr_field)):
                        self.assertIs(type(i), EmailAddress)

                self.assertIs(type(message.flags), tuple)
                for i in message.flags:
                    self.assertIs(type(i), str)

                for att in message.attachments:
                    self.assertIs(type(att.filename), str)
                    self.assertIs(type(att.content_id), str)
                    self.assertIs(type(att.content_type), str)
                    self.assertIs(type(att.content_disposition), str)
                    self.assertIs(type(att.payload), bytes)
                    self.assertIs(type(att.size), int)

            # counts
            self.assertTrue(cnt_fetch_all_answered_and_flagged >= 1)
            self.assertTrue(cnt_fetch_all_head_answered_and_flagged >= 1)
            self.assertTrue(cnt_fetch_all_bulk_answered_and_flagged >= 1)
            self.assertTrue(
                cnt_fetch_all ==
                cnt_fetch_all_head ==
                cnt_fetch_all_bulk ==
                6
            )
            self.assertTrue(
                cnt_fetch_all_answered_and_flagged ==
                cnt_fetch_all_head_answered_and_flagged ==
                cnt_fetch_all_bulk_answered_and_flagged
            )

    def test_attributes(self):
        test_msg_attr_set = {'subject', 'from_', 'to', 'cc', 'bcc', 'reply_to', 'date', 'date_str', 'text', 'html',
                             'headers', 'from_values', 'to_values', 'cc_values', 'bcc_values', 'reply_to_values'}
        test_att_attr_set = {'filename', 'content_id', 'content_type', 'content_disposition', 'payload'}

        eml_path_set = []
        for path_variant in ('../tests/messages', 'tests/messages'):
            for root, subdirs, files in os.walk(path_variant):
                for file_name in files:
                    full_path = os.path.abspath('{}/{}'.format(root, file_name)).replace('\\', '/')
                    if full_path.lower().endswith('.eml'):
                        eml_path_set.append(full_path)

        for eml_path in eml_path_set:
            # *there are many parser improvements at 3.13
            fixed_in_py313 = ('missing_body.eml', 'bad_date_header.eml', 'raw_email_with_at_display_name.eml')
            if any(i in eml_path for i in fixed_in_py313) and PYTHON_VERSION_MINOR == 13:
                continue
            py_path = eml_path.replace('/messages/', '/messages_data/')[:-4] + '.py'
            eml_data_module = _load_module(py_path)
            expected_data = eml_data_module.DATA  # noqa
            with open(eml_path, 'rb') as f:
                bytes_data = f.read()
            message = MailMessage.from_bytes(bytes_data)
            for msg_attr in test_msg_attr_set:
                self.assertEqual(getattr(message, msg_attr), expected_data[msg_attr])
            for att_i, att in enumerate(message.attachments):
                for att_attr in test_att_attr_set:
                    self.assertEqual(getattr(att, att_attr), expected_data['attachments'][att_i][att_attr])


if __name__ == "__main__":
    unittest.main()

"""
attachment_2_base64
    Непонятно почему get_content_type не может получить content-type, в файле он есть
    Из за этого 2е вложение воспринимается как msg.text, хотя в файле его нет
    Возможно это из за наличия дефекта MissingHeaderBodySeparatorDefect
    .../python/Python36-32/Lib/email/message.py 
    def get_content_type(self): 
        ...
        value = self.get('content-type', missing) -> None -> return self.get_default_type() -> text/plain
"""
