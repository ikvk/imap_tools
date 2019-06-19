0.6.0
=====

* decomposition to modules
* remove typing dependency
* add MailMessage.cc, MailMessage.bcc attrs
* specify custom classes email_message_class directly
* MailBox._uid_str change type check logic
* Change MailMessage attr return types: lists -> tuples
* MailBox.fetch add mark_seen param
* fix MailMessage.from_ bug when empty

0.5.0
=====
* new MailMessage.uid parse logic
* functools.lru_cache for MailMessage properties
* MailMessage.get_attachments() -> MailMessage.attachments
* fix setuptools