0.8.0
=====
Add context manager

0.7.2
=====
MailBox._uid_str - get uid attrs for MailBox.fetch generator only

0.7.1
=====
Less strict regexp for parse uid

0.7.0
=====
* decode MailMessage text and html using encoding, specified in email

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

0.4.0
=====
* fix _decode_value for unknown encoding
* fix _parse_email_address

0.3.0
=====
* install_requires
* fix manifest
* add typing lib
* _uid_str works with generator

0.1.1
=====
* first version: May 31, 2017
