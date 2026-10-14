import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='Test message with attached message',
    from_='test@example.com',
    to=('test@example.com',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2017, 12, 30, 19, 12, 38, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))),
    date_str='Sat, 30 Dec 2017 19:12:38 +0100',
    text='This is a test message with an attached message.\r\n\r\nHere is the body of the attached message. Search for bodyOfAttachedMessagePlain.',
    html='<body>Here is the body of the attached message. Search for bodyOfAttachedMessägeHTML.</body>',
    headers={'to': ('test@example.com',), 'from': ('test@example.com',), 'subject': ('Test message with attached message',), 'message-id': ('<8259dd8e-2293-8765-e720-61dfcd10a6f3@example.com>',), 'date': ('Sat, 30 Dec 2017 19:12:38 +0100',), 'user-agent': ('Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101\r\n Thunderbird/59.0a1',), 'mime-version': ('1.0',), 'content-type': ('multipart/mixed;\r\n boundary="------------9B410E80D6DA0868F068B0E4"',), 'content-language': ('en-GB',)},
    attachments=[
        dict(
            filename='attached-message.eml',
            content_id='',
            content_disposition='attachment',
            content_type='message/rfc822',
            payload=b'To: test@example.com\nFrom: test@example.com\nSubject: Attached message (plaintext + HMTL, both base64 encoded)\nMessage-ID: <a30f750d-d56c-8a52-971c-f95a131e8332@example.com>\nDate: Sat, 30 Dec 2017 19:31:21 +0100\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101\n Thunderbird/59.0a1\nMIME-Version: 1.0\nContent-Type: multipart/alternative;\n boundary="------------FAB286B8794CC63C0A0FD1BB"\nContent-Language: de-DE\n\nThis is a multi-part message in MIME format.\n--------------FAB286B8794CC63C0A0FD1BB\nContent-Type: text/plain; charset=windows-1252; format=flowed\nContent-Transfer-Encoding: base64\n\nSGVyZSBpcyB0aGUgYm9keSBvZiB0aGUgYXR0YWNoZWQgbWVzc2FnZS4gU2VhcmNoIGZvciBib2R5T2ZBdHRhY2hlZE1lc3NhZ2VQbGFpbi4=\n\n\n--------------FAB286B8794CC63C0A0FD1BB\nContent-Type: text/html; charset=utf-8\nContent-Transfer-Encoding: base64\n\nPGJvZHk+SGVyZSBpcyB0aGUgYm9keSBvZiB0aGUgYXR0YWNoZWQgbWVzc2FnZS4gU2VhcmNoIGZvciBib2R5T2ZBdHRhY2hlZE1lc3PDpGdlSFRNTC48L2JvZHk+\n\n--------------FAB286B8794CC63C0A0FD1BB--\n\n',
        ),
        ],
    from_values=EmailAddress(name='', email='test@example.com'),
    to_values=(EmailAddress(name='', email='test@example.com'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)