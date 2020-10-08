0.26.0
======
BaseMailBox.login initial_folder argument now can be None to skip folder.set

0.25.1
======
* Fixed MailBoxFolderManager.list bug on delim = NIL

0.25.0
======
* Added MailMessage.size attribute

0.24.0
======
* Added MailBox.__init__ starttls argument for using STARTTLS
* Fixed MailBox._fetch_in_bulk bug for empty self.search result

0.23.0
======
* Added BaseMailBox.search method
* Added BaseMailBox.fetch bulk argument
* Removed BaseMailBox._criteria_encoder
* Removed BaseMailBox.last_search_ids
* Added utils.grouper

0.22.0
======
* Added Attachment.content_id
* Added Attachment.content_disposition
* Attachment._part -> Attachment.part
* email.utils.parsedate_to_datetime used in utils.parse_email_addresses
* BaseMailBox.fetch limit argument now can receive slice object
* BaseMailBox instance now has attribute mailbox.last_search_ids, it fills after each fetch - msg ids from search command
* __init__.py refined

0.21.0
======
* Added MailBox.xoauth2 - authentication using OAuth 2.0 mechanism
* MailMessage (to, cc, bcc, reply_to) now works for fields specified multiple times (e.g. twice Cc: Cc:)

0.20.0
======
* BaseMailBox.fetch headers_only arg fixed

0.19.1
======
* Importing all from utils module removed from the default package imports

0.19.0
======
* Support international characters in email addresses

0.18.1
======
* Add deprecated Q to default import, *forgot

0.18.0
======
* Added 14 new custom lib exceptions (errors.py): MailboxCopyError, MailboxDeleteError, MailboxExpungeError, MailboxFetchError, MailboxFlagError, MailboxFolderCreateError, MailboxFolderDeleteError, MailboxFolderRenameError, MailboxFolderSelectError, MailboxFolderStatusError, MailboxFolderStatusValueError, MailboxLoginError, MailboxLogoutError, MailboxSearchError
* UnexpectedCommandStatusError now not used directly.
* Added folder.MailBoxFolderStatusOptions class instead MailBoxFolderManager.folder_status_options
* utils.MessageFlags -> message.MailMessageFlags
* query.py: ValueError replaced to TypeError in many places
* utils.short_month_names renamed to utils.SHORT_MONTH_NAMES
* utils.cleaned_uid_set - parsing optimized, raise TypeError instead ValueError, not ignore empty uid from generator
* utils.check_command_status - new logic
* BaseMailBox.fetch headers_only arg is disabled until fix

0.17.0
======
* Query builder: removed Q alias for AND
* Query builder: added new aliases: A for AND, O for OR, N for NOT

0.16.1
======
* Added X-GM-LABELS support to query builder (gmail_label)

0.16.0
======
* added BaseMailBox.fetch headers_only argument - get only email headers
* BaseMailBox.attachments now can returns nameless attachments (inline/forwarded)
* MailBoxFolderManager.list result changed: item['flags'] now are tuple(str)

0.15.0
======
* mailbox.MailBox splitted to: BaseMailBox, MailBox, MailBoxUnencrypted
* MailBox ssl argument deleted
* mailbox.MessageFlags class moved to utils.MessageFlags
* Add PySocks proxy examples

0.14.3
======
* Fixed multiple encodings case for attachment name

0.14.2
======
* Fixed bug in folder.MailBoxFolderManager.exists/list on folder names with " and \ chars

0.14.1
======
* Fixed bug on folders names with space in folder.MailBoxFolderManager.exists/list

0.14.0
======
* Improved parse logic for message.MailMessage.flags

0.13.1
======
* Improve utils.parse_email_addresses - full values for bad emails

0.13.0
======
* New parse logic for email addresses - utils.parse_email_addresses, using email.utils.getaddresses
* Added message.MailMessage.reply_to, message.MailMessage.reply_to_values
* Removed message.MailMessage._parse_addresses

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
* first version: 31 May 2017
