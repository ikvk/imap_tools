0.12.0
======
* MailBox.fetch - added "reverse" parameter
* in utils.parse_email_address used email.utils.parseaddr
* added tests for message attributes

0.11.1
======
* message.Attachment.payload - removed probability of return None

0.11.0
======
* message.MailMessage.attachments now return list of message.MailMessage.Attachment objects

0.10.0
======
* utils.cleaned_uid_set now not raise ValueError('uid_set should not be empty')
* mailbox.MailBox delete,copy,move,flag,seen methods changed: Do nothing on empty uid_list - return None
* mailbox.StandardMessageFlags renamed to mailbox.MessageFlags

0.9.4
=====
* MailMessage.from_bytes - Alternative constructor

0.9.3
=====
* change license: MIT -> Apache License, Version 2.0
* improve utils.decode_value
* improve MailMessage.attachment decoding
* MailBoxFolderManager.status now returns int values in result
* fix query builder bugs - imap prefix notation rules
* query builder: The key types are marked with `*` can accepts a sequence of values like list, tuple, set or generator.
* add new examples

0.9.2
=====
* improved MailMessage._parse_addresses
* improved utils.parse_email_address
* improved utils.parse_email_date
* fixed utils.short_month_names +Dec
* fixed MailMessage.text and MailMessage.html encoding bug on invalid headers

0.9.1
=====
* fix README.rst encoding in setup.py

0.9.0
=====
* Added query builder - implemented the search logic described in rfc3501
* MailBox.fetch - added "charset" parameter. If the "charset" argument is specified in MailBox.fetch, the search string will be encoded to this encoding.
* MailBox.fetch "search_criteria" parameter renamed to "criteria"
* MailMessage.date now returns datetime.date
* MailMessage.date_str attribute added
* MailMessage.headers attribute added
* MailMessage.id removed
* ImapToolsError base exception class removed
* MailBoxWrongFlagError exception class removed
* functions: (cleaned_uid_set,check_command_status,decode_value,parse_email_address,parse_email_date,quote,pairs_to_dict) moved to utils module
* readme text improved
* fixed folder.set encoding dug

0.8.0
=====
* Add context manager

0.7.2
=====
* MailBox._uid_str - get uid attrs for MailBox.fetch generator only

0.7.1
=====
* Less strict regexp for parse uid

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
