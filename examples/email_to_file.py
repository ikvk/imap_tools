"""

If you want to save message as .eml file, work with MailMessage.obj - it is email.message.EmailMessage

Python email lib docs for .as_string() and .as_bytes():
    https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.as_string
    https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.as_bytes

So, you have 2 ways to save message as .eml file:
    * msg.obj.as_string(...
    * msg.obj.as_bytes(...

"""
