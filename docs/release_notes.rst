1.10.0
======
* Added: support IMAP command MOVE at BaseMailBox.move
* Added: MailboxMoveError, raises from BaseMailBox.move when MOVE command is supported
* Added: chunks argument for BaseMailBox.(copy,move,flag,delete) methods - Number of UIDs to proc at once, to avoid server errors on large set
* Changed: BaseMailBox.(copy,move,flag,delete) result types
* Changed: utils.clean_uids now returns List[str]
* Changed: utils.chunks_crop -> utils.chunked_crop, n arg renamed to chunk_size and it takes False-like vals
* Renamed: utils.chunks -> utils.chunked

1.9.1
=====
* Replaced: functools.lru_cache to functools.cached_property
* Replaced: .format() to f''
* Optimized: speed for imap_utf7
* Replaced: typing.AnyStr to utils.StrOrBytes

1.9.0
=====
* Added: __str__ to MailAttachment
* Fixed: MailMessage.text parser - text with inline attachments case
* Fixed: MailMessage.html parser - html with inline attachments case
* Dropped: support py3.3,py3.4,py3.5,py3.6,py3.7

1.8.0
=====
* Added: BaseMailBox.numbers_to_uids - Get message uids by message numbers

1.7.4
=====
* Fixed: encoding bug at MailAttachment.content_id

1.7.3
=====
* Fixed: bug in 3.12.6+ after [[3.12] [CVE-2023-27043] gh-102988: Reject malformed addresses in email.parseaddr()]

1.7.2
=====
* Fixed: MailBoxFolderManager.list double quotes bug

1.7.1
=====
* Fixed: MailBoxFolderManager.list folder_item_re bug

1.7.0
=====
* Moved: SortCriteria to consts
* Added: __str__ to MailMessage
* Added: docs info

1.6.0
=====
* [Breaking] Changed: "bulk" argument at BaseMailBox.fetch now can accept int values >=2 - for control bulk size
* Added "sort" argument to BaseMailBox.fetch and BaseMailBox.uids - for sort on server. Use SortCriteria constants
* Renamed: utf7_encode and utf7_decode from imap_utf7.py (was encode and decode)

1.5.0
=====
* Fixed: MailAttachment.filename parse non-ascii filename

1.4.0
=====
* [Breaking] MailMessage.html replacing charset to utf-8 in html meta for consistency
* Added utils.replace_html_ct_charset

1.3.0
=====
* Added support for python 3.12 - Since 3.12 keyfile and certfile arguments are deprecated for imaplib.IMAP4_SSL, ssl_context and timeout must be keyword arguments

1.2.0
=====
* Fixed MailBoxFolderManager.status bug for folders with brackets
* Added py.typed for mypy lib

1.1.0
=====
* Using BaseMailBox.uids in BaseMailBox.fetch instead BaseMailBox.numbers - for reliable parallel work with mailbox [#202]
* [Breaking] Removed miss_no_uid argument from BaseMailBox.uids as not actual. It may change uids ordering.
* [Breaking] Removed miss_no_uid argument from BaseMailBox.fetch as not actual

1.0.0
=====
* 21 Nov 2022: No constructive issues or merge requests a long time (since 5 May 2022).

0.57.0
======
* Added BaseMailBox.login_utf8 - Authenticate to an account with a UTF-8 username and/or password

0.56.0
======
* Simplify IdleManager.poll

0.55.0
======
* Fixed query builder bug with key - "header" and value - [Header]

0.54.0
======
* EmailAddress full is property now, parse_email_addresses fixed
* Added MailBoxTls into __init__.py
* Fixed tls.py example, rename examples, added basic.py example

0.53.0
======
* [Breaking] BaseMailBox.box client instance renamed to BaseMailBox.client
* Fixed BaseMailBox.xoauth2 consistency with BaseMailBox.login
* BaseMailBox.folder/idle managers now instantiates in __init__

0.52.0
======
* [Breaking] STARTTLS logic moved to MailBoxTls

0.51.1
======
* Fix IdleManager

0.51.0
======
* Added idle manager for work with IDLE: mailbox.idle.<[start,poll,stop,wait]>
* Added BaseMailBox.consume_until_tagged_response method: waiting for tagged response
* Added new exception: MailboxTaggedResponseError
* Removed unused stuff: BaseMailBox.with_headers_only_allowed_errors

0.50.2
======
* query.ParamConverter._gen_values minor improvement
* utils.clean_uids minor improvement
* Added test for utils.clean_uids

0.50.1
======
* Fix ParamConverter.convert order search keys with values list
* Added tox config for test all supported versions

0.50.0
======
* Fix MailboxLoginError was never raise
* ParamConverter.convert now order search keys by alphabet - guarantees a repeatable result for query builder

0.49.1
======
* Fix support for python 3.5

0.49.0
======
* Fixed message.MailAttachment.size wrong size bug
* query.LogicOperator (and subclasses AND, OR, NOT) now have type annotated named search keys

0.48.1
======
* Fix type annotations

0.48.0
======
* [Breaking] MailMessage.<*>_values methods now returns EmailAddress instead dict
* [Breaking] MailBoxFolderManager.list new returns FolderInfo instead dict

0.47.0
======
* Dropped support for python 3.3, 3.4
* Added type annotations
* [Breaking] utils.clean_uids - removed special case for Generator with "fetch" name for implicitly gets all uids. Use BaseMailBox.uids method instead.
* Removed BaseMailBox deprecated stuff: fetch miss_defect arg, seen method, search method

0.46.0
======
* MailBoxFolderManager.status folder argument now may by equal to None - status of current folder
* utils.clean_uids now accept uid strings with uid sequence ranges, example: *:4,5:7,10
* query.UidRange end argument now may be None, equal to None by default

0.45.0
======
* Renamed BaseMailBox.search -> BaseMailBox.numbers, search are deprecated now
* Renamed MailboxSearchError -> MailboxNumbersError
* Added BaseMailBox.uids, MailboxUidsError

0.44.0
======
* Fixed BaseMailBox.append bug on flag_set=None
* Added MailBoxFolderManager.set readonly argument

0.43.0
======
* Added MailBoxFolderManager.subscribe method
* Deprecation: BaseMailBox.seen method are deprecated now, use flag method

0.42.0
======
* Fixed MessageFlags values - all system flags begin with "\"
* Fixed BaseMailBox.flag, BaseMailBox.append, MailMessage.flags - now works with system/custom flags correctly, -upper
* Added utils.clean_flags
* Moved message.MessageFlags -> consts.MailMessageFlags
* Moved folder.MailBoxFolderStatusOptions -> consts.MailBoxFolderStatusOptions
* Moved utils.SHORT_MONTH_NAMES -> consts.SHORT_MONTH_NAMES
* Renamed utils.cleaned_uid_set -> utils.clean_uids

0.41.0
======
* Fixed multiple encodings case bug at MailMessage.subject

0.40.0
======
* Fixed MailMessage.from_bytes - MailMessage.uid/flags parse errors
* Fixed utils.parse_email_date - parse bug on bad dates
* [Breaking] BaseMailBox.fetch miss_defect argument now is False by default, it will be removed soon
* Increased the email collection for tests

0.39.0
======
* Fixed MailAttachment.attachments - message/rfc822 forwarded messages not missing now

0.38.0
======
* Fixed bug at utils.parse_email_addresses - quoted with newlines
* Fixed bug at BaseMailBox.search - empty elements on split result with trailing spaces

0.37.0
======
* [Breaking] MailMessage.headers - now all keys in lower-case (*email headers are not case-sensitive)
* Path with tests excluded from distribution archive

0.36.0
======
* Fixed MailMessage.text/html parse on case: text/html with Content-ID

0.35.0
======
* Added BaseMailBox.append method
* Renamed message.Attachment -> message.MailAttachment
* Fixed bug at utils.encode_folder for bytes
* Fixed bug at mailbox.folder.status on encoded names

0.34.0
======
* Improved MailMessage.text/html on case: no text/html and has text/html attachment

0.33.0
======
* MailMessage.attachments - fixed miss some attachments

0.32.0
======
* Fixed bug at BaseMailBox.copy - folder name was not encoded

0.31.0
======
* MailMessage.uid - fixed bug - UID cannot be parsed if stored with empty flags list
* MailMessage.uid - used one regexp instead two
* MailBox, MailBoxUnencrypted - add timeout argument (supports since python 3.9)
* Added query.UidRange, for search by uid range, UID *:123
* Deprecated query.Q was removed

0.30.0
======
* BaseMailBox.fetch - fixed wrong responses for combinations of: slice, bulk, reverse

0.29.0
======
* BaseMailBox._fetch_in_bulk - add python versions compatibility - used return instead raise StopIteration

0.28.0
======
* MailMessage.attachments - improved parsing - case with Content-ID only

0.27.0
======
* Renamed MailMessage.size -> MailMessage.size_rfc822, returned type now always int
* Added MailMessage.size attribute
* Added Attachment.size attribute

0.26.0
======
* BaseMailBox.login initial_folder argument now can be None to skip folder.set

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
* message.MailMessage.attachments now return list of message.Attachment objects

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
