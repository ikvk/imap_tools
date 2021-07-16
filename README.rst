.. http://docutils.sourceforge.net/docs/user/rst/quickref.html

imap_tools 📧
=============

Work with email and mailbox by IMAP:

- Parsed email message attributes
- Query builder for searching emails
- Actions with emails: copy, delete, flag, move, append
- Actions with folders: list, set, get, create, exists, rename, subscribe, delete, status
- No dependencies

.. image:: https://img.shields.io/pypi/dm/imap_tools.svg?style=social

===============  ===============================================================
Python version   3.3+
License          Apache-2.0
PyPI             https://pypi.python.org/pypi/imap_tools/
IMAP RFC         VERSION 4rev1 - https://tools.ietf.org/html/rfc3501
EMAIL RFC        Internet Message Format - https://tools.ietf.org/html/rfc2822
===============  ===============================================================

.. contents::

Installation
------------
::

    $ pip install imap-tools

Guide
-----

Basic
^^^^^

Find info about imap-tools at: *this page*, issues, pull requests, source, stackoverflow.com

.. code-block:: python

    from imap_tools import MailBox, AND

    # get list of email subjects from INBOX folder
    with MailBox('imap.mail.com').login('test@mail.com', 'pwd') as mailbox:
        subjects = [msg.subject for msg in mailbox.fetch()]

    # get list of email subjects from INBOX folder - equivalent verbose version
    mailbox = MailBox('imap.mail.com')
    mailbox.login('test@mail.com', 'pwd', initial_folder='INBOX')  # or mailbox.folder.set instead 3d arg
    subjects = [msg.subject for msg in mailbox.fetch(AND(all=True))]
    mailbox.logout()

MailBox(BaseMailBox), MailBoxUnencrypted(BaseMailBox) - for create mailbox instance.

BaseMailBox.login, MailBox.xoauth2 - authentication functions. TLS connection
`example <https://github.com/ikvk/imap_tools/blob/master/examples/tls.py>`_.

BaseMailBox.fetch - first searches email nums by criteria in current folder, then fetch and yields `MailMessage <#email-attributes>`_:

* *criteria* = 'ALL', message search criteria, `query builder <#search-criteria>`_
* *charset* = 'US-ASCII', indicates charset of the strings that appear in the search criteria. See rfc2978
* *limit* = None, limit on the number of read emails, useful for actions with a large number of messages, like "move"
* *miss_no_uid* = True, miss emails without uid
* *mark_seen* = True, mark emails as seen on fetch
* *reverse* = False, in order from the larger date to the smaller
* *headers_only* = False, get only email headers (without text, html, attachments)
* *bulk* = False, False - fetch each message separately per N commands - low memory consumption, slow; True - fetch all messages per 1 command - high memory consumption, fast

BaseMailBox.<action> - `copy, move, delete, flag, append <#actions-with-emails>`_

BaseMailBox.folder - `folder manager <#actions-with-folders>`_

BaseMailBox.search - search mailbox for matching message numbers in current folder (this is not uids)

BaseMailBox.box - imaplib.IMAP4/IMAP4_SSL client instance.

Email attributes
^^^^^^^^^^^^^^^^

MailMessage and MailAttachment public attributes are cached by functools.lru_cache

.. code-block:: python

    for msg in mailbox.fetch():  # generator: imap_tools.MailMessage
        msg.uid          # str or None: '123'
        msg.subject      # str: 'some subject 你 привет'
        msg.from_        # str: 'Bartölke@ya.ru'
        msg.to           # tuple: ('iam@goo.ru', 'friend@ya.ru', )
        msg.cc           # tuple: ('cc@mail.ru', )
        msg.bcc          # tuple: ('bcc@mail.ru', )
        msg.reply_to     # tuple: ('reply_to@mail.ru', )
        msg.date         # datetime.datetime: 1900-1-1 for unparsed, may be naive or with tzinfo
        msg.date_str     # str: original date - 'Tue, 03 Jan 2017 22:26:59 +0500'
        msg.text         # str: 'Hello 你 Привет'
        msg.html         # str: '<b>Hello 你 Привет</b>'
        msg.flags        # tuple: ('\\Seen', '\\Flagged', 'ENCRYPTED')
        msg.headers      # dict: {'received': ('from 1.m.ru', 'from 2.m.ru'), 'anti-virus': ('Clean',)}
        msg.size_rfc822  # int: 20664 bytes - size info from server (*useful with headers_only arg)
        msg.size         # int: 20377 bytes - size of received message

        for att in msg.attachments:  # list: imap_tools.MailAttachment
            att.filename             # str: 'cat.jpg'
            att.payload              # bytes: b'\xff\xd8\xff\xe0\'
            att.content_id           # str: 'part45.06020801.00060008@mail.ru'
            att.content_type         # str: 'image/jpeg'
            att.content_disposition  # str: 'inline'
            att.part                 # email.message.Message: original object
            att.size                 # int: 17361 bytes

        msg.obj              # email.message.Message: original object
        msg.from_values      # dict or None: {'email': 'im@ya.ru', 'name': 'Ya', 'full': 'Ya <im@ya.ru>'}
        msg.to_values        # tuple: ({'email': '', 'name': '', 'full': ''},)
        msg.cc_values        # tuple: ({'email': '', 'name': '', 'full': ''},)
        msg.bcc_values       # tuple: ({'email': '', 'name': '', 'full': ''},)
        msg.reply_to_values  # tuple: ({'email': '', 'name': '', 'full': ''},)

Search criteria
^^^^^^^^^^^^^^^

This chapter about "criteria" and "charset" arguments of MailBox.fetch.

You can use 3 approaches to build search criteria:

.. code-block:: python

    from imap_tools import AND, OR, NOT

    mailbox.fetch(AND(subject='weather'))  # query, the str-like object
    mailbox.fetch('TEXT "hello"')          # str
    mailbox.fetch(b'TEXT "\xd1\x8f"')      # bytes, *charset arg is ignored

The "charset" is argument used for encode criteria to this encoding.
You can pass the criteria as bytes in the desired encoding - in this case, the encoding will be ignored.

.. code-block:: python

    mailbox.fetch(A(subject='жёлтый'), charset='utf8')

Query builder implements all search logic described in `rfc3501 <https://tools.ietf.org/html/rfc3501#section-6.4.4>`_.
It uses this classes:

========  =====  ========================================== ======================================
Class     Alias  Usage                                      Arguments
========  =====  ========================================== ======================================
AND       A      combines keys by logical "AND" condition   Search keys (see table below) | str
OR        O      combines keys by logical "OR" condition    Search keys (see table below) | str
NOT       N      invert the result of a logical expression  AND/OR instances | str
Header    H      for search by headers                      name: str, value: str
UidRange  U      for search by UID range                    start: str, end: str
========  =====  ========================================== ======================================

See `query examples <https://github.com/ikvk/imap_tools/blob/master/examples/search.py>`_. A few examples:

.. code-block:: python

    from imap_tools import A, AND, OR, NOT
    # AND
    A(text='hello', new=True)  # '(TEXT "hello" NEW)'
    # OR
    OR(text='hello', date=datetime.date(2000, 3, 15))  # '(OR TEXT "hello" ON 15-Mar-2000)'
    # NOT
    NOT(text='hello', new=True)  # 'NOT (TEXT "hello" NEW)'
    # complex
    A(OR(from_='from@ya.ru', text='"the text"'), NOT(OR(A(answered=False), A(new=True))), to='to@ya.ru')
    # python note: you can't do: A(text='two', NOT(subject='one'))
    A(NOT(subject='one'), text='two')  # use kwargs after logic classes (args)

Search key table. Key types marked with `*` can accepts a sequence of values like list, tuple, set or generator.

=============  ===============  ======================  =================================================================
Key            Types            Results                 Description
=============  ===============  ======================  =================================================================
answered       bool             `ANSWERED/UNANSWERED`   with/without the Answered flag
seen           bool             `SEEN/UNSEEN`           with/without the Seen flag
flagged        bool             `FLAGGED/UNFLAGGED`     with/without the Flagged flag
draft          bool             `DRAFT/UNDRAFT`         with/without the Draft flag
deleted        bool             `DELETED/UNDELETED`     with/without the Deleted flag
keyword        str*             KEYWORD KEY             with the specified keyword flag
no_keyword     str*             UNKEYWORD KEY           without the specified keyword flag
`from_`        str*             FROM `"from@ya.ru"`     contain specified str in envelope struct's FROM field
to             str*             TO `"to@ya.ru"`         contain specified str in envelope struct's TO field
subject        str*             SUBJECT "hello"         contain specified str in envelope struct's SUBJECT field
body           str*             BODY "some_key"         contain specified str in body of the message
text           str*             TEXT "some_key"         contain specified str in header or body of the message
bcc            str*             BCC `"bcc@ya.ru"`       contain specified str in envelope struct's BCC field
cc             str*             CC `"cc@ya.ru"`         contain specified str in envelope struct's CC field
date           datetime.date*   ON 15-Mar-2000          internal date is within specified date
date_gte       datetime.date*   SINCE 15-Mar-2000       internal date is within or later than the specified date
date_lt        datetime.date*   BEFORE 15-Mar-2000      internal date is earlier than the specified date
sent_date      datetime.date*   SENTON 15-Mar-2000      rfc2822 Date: header is within the specified date
sent_date_gte  datetime.date*   SENTSINCE 15-Mar-2000   rfc2822 Date: header is within or later than the specified date
sent_date_lt   datetime.date*   SENTBEFORE 1-Mar-2000   rfc2822 Date: header is earlier than the specified date
size_gt        int >= 0         LARGER 1024             rfc2822 size larger than specified number of octets
size_lt        int >= 0         SMALLER 512             rfc2822 size smaller than specified number of octets
new            True             NEW                     have the Recent flag set but not the Seen flag
old            True             OLD                     do not have the Recent flag set
recent         True             RECENT                  have the Recent flag set
all            True             ALL                     all, criteria by default
uid            iter(str)/str/U  UID 1,2,17              corresponding to the specified unique identifier set
header         H(str, str)*     HEADER "A-Spam" "5.8"   have a header that contains the specified str in the text
gmail_label    str*             X-GM-LABELS "label1"    have this gmail label.
=============  ===============  ======================  =================================================================

Server side search notes:

* For string search keys a message matches if the string is a substring of the field. The matching is case-insensitive.
* When searching by dates - email's time and timezone are disregarding.

Actions with emails
^^^^^^^^^^^^^^^^^^^

First of all read about uid `at rfc3501 <https://tools.ietf.org/html/rfc3501#section-2.3.1.1>`_.

Action's uid_list arg may takes:

* str, that is comma separated uids
* Iterable, that contains str uids
* Generator with "fetch" name, implicitly gets all uids

For actions with a large number of messages imap command may be too large and will cause exception at server side,
use 'limit' argument for fetch in this case.

.. code-block:: python

    with MailBox('imap.mail.com').login('test@mail.com', 'pwd', initial_folder='INBOX') as mailbox:

        # COPY messages with uid in 23,27 from current folder to folder1
        mailbox.copy('23,27', 'folder1')

        # MOVE all messages from current folder to INBOX/folder2, (implicit creation of uid list)
        mailbox.move(mailbox.fetch(), 'INBOX/folder2')

        # DELETE all messages from current folder, (explicit creation of uid list)
        mailbox.delete([msg.uid for msg in mailbox.fetch()])

        # FLAG unseen messages in current folder as \Seen, \Flagged and TAG1
        flags = (imap_tools.MailMessageFlags.SEEN, imap_tools.MailMessageFlags.FLAGGED, 'TAG1')
        mailbox.flag(mailbox.fetch(AND(seen=False)), flags, True)

        # APPEND: add message to mailbox directly, to INBOX folder with \Seen flag and now date
        with open('/tmp/message.eml', 'rb') as f:
            msg = imap_tools.MailMessage.from_bytes(f.read())  # *or use bytes instead MailMessage
        mailbox.append(msg, 'INBOX', dt=None, flag_set=[imap_tools.MailMessageFlags.SEEN])

Actions with folders
^^^^^^^^^^^^^^^^^^^^
.. code-block:: python

    with MailBox('imap.mail.com').login('test@mail.com', 'pwd') as mailbox:

        # LIST: get all subfolders of the specified folder (root by default)
        for f in mailbox.folder.list('INBOX'):
            print(f)  # {'name': 'INBOX|cats', 'delim': '|', 'flags': ('\\Unmarked', '\\HasChildren')}

        # SET: select folder for work
        mailbox.folder.set('INBOX')

        # GET: get selected folder
        current_folder = mailbox.folder.get()

        # CREATE: create new folder
        mailbox.folder.create('INBOX|folder1')

        # EXISTS: check is folder exists (shortcut for list)
        is_exists = mailbox.folder.exists('INBOX|folder1')

        # RENAME: set new name to folder
        mailbox.folder.rename('folder3', 'folder4')

        # SUBSCRIBE: subscribe/unsubscribe to folder
        mailbox.folder.subscribe('INBOX|папка два', True)

        # DELETE: delete folder
        mailbox.folder.delete('folder4')

        # STATUS: get folder status info
        stat = mailbox.folder.status('some_folder')
        print(stat)  # {'MESSAGES': 41, 'RECENT': 0, 'UIDNEXT': 11996, 'UIDVALIDITY': 1, 'UNSEEN': 5}

Exceptions
^^^^^^^^^^

Custom lib exceptions here: `errors.py <https://github.com/ikvk/imap_tools/blob/master/imap_tools/errors.py>`_.

Release notes
-------------

History of important changes: `release_notes.rst <https://github.com/ikvk/imap_tools/blob/master/docs/release_notes.rst>`_

Contribute
----------

If you found a bug or have a question, then:

1. Look for answer at: this page, issues, pull requests, source, RFCs, stackoverflow.com, internet.
2. And only then - create merge request or issue.

Reasons
-------

- Excessive low level of `imaplib` library.
- Other libraries contain various shortcomings or not convenient.
- Open source projects make world better.

Thanks
------

Big thanks to people who helped develop this library:

`shilkazx <https://github.com/shilkazx>`_,
`somepad <https://github.com/somepad>`_,
`0xThiebaut <https://github.com/0xThiebaut>`_,
`TpyoKnig <https://github.com/TpyoKnig>`_,
`parchd-1 <https://github.com/parchd-1>`_,
`dojasoncom <https://github.com/dojasoncom>`_,
`RandomStrangerOnTheInternet <https://github.com/RandomStrangerOnTheInternet>`_,
`jonnyarnold <https://github.com/jonnyarnold>`_,
`Mitrich3000 <https://github.com/Mitrich3000>`_,
`audemed44 <https://github.com/audemed44>`_,
`mkalioby <https://github.com/mkalioby>`_,
`atlas0fd00m <https://github.com/atlas0fd00m>`_,
`unqx <https://github.com/unqx>`_,
`daitangio <https://github.com/daitangio>`_,
`upils <https://github.com/upils>`_,
`Foosec <https://github.com/Foosec>`_,
`frispete <https://github.com/frispete>`_,
`PH89 <https://github.com/PH89>`_,
`amarkham09 <https://github.com/amarkham09>`_,
`nixCodeX <https://github.com/nixCodeX>`_,
`backelj <https://github.com/backelj>`_,
`ohayak <https://github.com/ohayak>`_,
`mwherman95926 <https://github.com/mwherman95926>`_,
`andyfensham <https://github.com/andyfensham>`_,
`mike-code <https://github.com/mike-code>`_,
`aknrdureegaesr <https://github.com/aknrdureegaesr>`_,
`ktulinger <https://github.com/ktulinger>`_,
`SamGenTLEManKaka <https://github.com/SamGenTLEManKaka>`_,
`devkral <https://github.com/devkral>`_,
`tnusraddinov <https://github.com/tnusraddinov>`_,
`thepeshka <https://github.com/thepeshka>`_,
`shofstet <https://github.com/shofstet>`_,
`the7erm <https://github.com/the7erm>`_,
`c0da <https://github.com/c0da>`_,
`dev4max <https://github.com/dev4max>`_,
`ascheucher <https://github.com/ascheucher>`_,
`Borutia <https://github.com/Borutia>`_,
`nathan30 <https://github.com/nathan30>`_,
`daniel55411 <https://github.com/daniel55411>`_,
`rcarmo <https://github.com/rcarmo>`_,
`bhernacki <https://github.com/bhernacki>`_,
`ilep <https://github.com/ilep>`_,
`ThKue <https://github.com/ThKue>`_,
`repodiac <https://github.com/repodiac>`_,
`tiuub <https://github.com/tiuub>`_,
`Yannik <https://github.com/Yannik>`_

Donate
------

💰 You may `donate <https://github.com/ikvk/imap_tools/blob/master/docs/donate.rst>`_, if this library helped you.
