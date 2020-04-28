from imap_tools import MailMessage

with open('.../attachment_2_base64.eml', 'rb') as f:
    bytes_data = f.read()
msg = MailMessage.from_bytes(bytes_data)
print(msg.date_str, msg.subject)
for i, att in msg.attachments:
    print('-', att.filename, att.content_type, len(att.payload))
