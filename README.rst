.. http://docutils.sourceforge.net/docs/user/rst/quickref.html

imap_tools
==========

Working with email and mailbox using IMAP protocol.

===================  ====================================================
Python version       3.3+
License              MIT
PyPI                 https://pypi.python.org/pypi/imap_tools/
IMAP                 VERSION 4rev1 - https://tools.ietf.org/html/rfc3501
===================  ====================================================

.. contents::

Features
--------
- Parsed email message attributes
- Query builder for searching emails
- Work with emails in folders (copy, delete, flag, move, seen)
- Work with mailbox folders (list, set, get, create, exists, rename, delete, status)
- No dependencies

Installation
------------
::

    $ pip install imap_tools

Guide
-----

Basic
^^^^^
.. code-block:: python

    from imap_tools import MailBox, Q

    # get list of email subjects from INBOX folder
    with MailBox('imap.mail.com').login('test@mail.com', 'password') as mailbox:
        subjects = [msg.subject for msg in mailbox.fetch()]
    # OR the same otherwise
    mailbox = MailBox('imap.mail.com')
    mailbox.login('test@mail.com', 'password', initial_folder='INBOX')
    subjects = [msg.subject for msg in mailbox.fetch(Q(all=True))]
    mailbox.logout()

MailBox.fetch - email message generator, first searches email uids by criteria, then fetch and yields emails by one:

* *criteria*: message search criteria, `docs <#search-criteria>`_
* *charset*: 'US-ASCII', indicates charset of the strings that appear in the search criteria. See rfc2978
* *limit*: None, limit on the number of read emails, useful for actions with a large number of messages, like "move"
* *miss_defect*: True, miss emails with defects
* *miss_no_uid*: True, miss emails without uid
* *mark_seen*: True, mark emails as seen on fetch

Email attributes
^^^^^^^^^^^^^^^^
.. code-block:: python

    # NOTE: All message properties are cached by functools.lru_cache

    for message in mailbox.fetch():
        message.uid          # str or None, '123'
        message.subject      # str, 'some subject'
        message.from_        # str, 'sender@ya.ru'
        message.to           # tuple, ('iam@goo.ru', 'friend@ya.ru', )
        message.cc           # tuple, ('cc@mail.ru', )
        message.bcc          # tuple, ('bcc@mail.ru', )
        message.date         # datetime.datetime, 1900-1-1 for unparsed, may be naive or with tzinfo
        message.text         # str, 'hi'
        message.html         # str, '<b>hi</b>'
        message.flags        # tuple, ('SEEN', 'FLAGGED', 'ENCRYPTED')
        message.headers      # dict, {'Received': ('from 1.m.net', 'from 2.m.net'), 'AntiVirus-Status': ('Clean',)}
        message.attachments  # [(str, bytes)], 'cat.jpg', b'\xff\xd8\xff\xe0\'
        message.obj          # original email.message.Message object
        message.from_values  # dict or None, {'email': 'sender@ya.ru', 'name': 'Ivan', 'full': 'Ivan <sender@ya.ru>'}
        message.to_values    # tuple, ({'email': '', 'name': '', 'full': ''},)
        message.cc_values    # tuple, ({'email': '', 'name': '', 'full': ''},)
        message.bcc_values   # tuple, ({'email': '', 'name': '', 'full': ''},)
        message.date_str     # original date str, 'Tue, 03 Jan 2017 22:26:59 +0500'

Search criteria
^^^^^^^^^^^^^^^

| Implemented the search logic described in `rfc3501 <https://tools.ietf.org/html/rfc3501#section-6.4.4>`_.
| Class AND and its alias Q are used to combine keys by the logical "and" condition.
| Class OR is used to combine keys by the logical "or" condition.
| Class NOT is used to invert the result of a logical expression.
| If the "charset" argument is specified in MailBox.fetch, the search string will be encoded to this encoding.
| You can change this behavior by overriding MailBox._criteria_encoder or pass criteria as bytes in desired encoding.
|
.. code-block:: python

    from imap_tools import Q, AND, OR, NOT
    # base
    mailbox.fetch('TEXT "hello"')  # str
    mailbox.fetch(b'TEXT "\xd1\x8f"')  # bytes
    mailbox.fetch(Q(subject='weather'))  # query, the str-like object
    # AND
    Q(text='hello', new=True)  # 'TEXT "hello" NEW'
    # OR
    OR(text='hello', date=datetime.date(2000, 3, 15))  # '(OR TEXT "hello" ON 15-Mar-2000)'
    # NOT
    NOT(text='hello', new=True)  # '(NOT TEXT "hello" NEW)'
    # complex:
    # 'TO "to@ya.ru" (OR FROM "from@ya.ru" TEXT "\\"the text\\"") (NOT (OR UNANSWERED NEW))')
    Q(OR(from_='from@ya.ru', text='"the text"'), NOT(OR(Q(answered=False), Q(new=True))), to='to@ya.ru')
    # encoding
    mailbox.fetch(Q(subject='привет'), charset='utf8')  # 'привет' will be encoded by MailBox._criteria_encoder

Python syntax limitations:

.. code-block:: python

    # you can't do: Q(to='one@mail.ru', to='two@mail.ru'), instead you can:
    Q(AND(to='one@mail.ru'), AND(to='two@mail.ru'))  # 'TO "one@mail.ru" TO "two@mail.ru"'
    # you can't do: Q(subject='two', NOT(subject='one')), use kwargs after args (after logic classes):
    Q(NOT(subject='one'), subject='two')

=============  =============  =======================  =================================================================
Key            Types          Results                  Description
=============  =============  =======================  =================================================================
answered       bool           `ANSWERED|UNANSWERED`    with|without the Answered flag
seen           bool           `SEEN|UNSEEN`            with|without the Seen flag
flagged        bool           `FLAGGED|UNFLAGGED`      with|without the Flagged flag
draft          bool           `DRAFT|UNDRAFT`          with|without the Draft flag
deleted        bool           `DELETED|UNDELETED`      with|without the Deleted flag
keyword        str            KEYWORD KEY              with the specified keyword flag
no_keyword     str            UNKEYWORD KEY            without the specified keyword flag
`from_`        str            FROM `"from@ya.ru"`      contain specified str in envelope struct's FROM field
to             str            TO `"to@ya.ru"`          contain specified str in envelope struct's TO field
subject        str            SUBJECT "hello"          contain specified str in envelope struct's SUBJECT field
body           str            BODY "some_key"          contain specified str in body of the message
text           str            TEXT "some_key"          contain specified str in header or body of the message
bcc            str            BCC `"bcc@ya.ru"`        contain specified str in envelope struct's BCC field
cc             str            CC `"cc@ya.ru"`          contain specified str in envelope struct's CC field
date           datetime.date  ON 15-Mar-2000           internal date* is within specified date
date_gte       datetime.date  SINCE 15-Mar-2000        internal date* is within or later than the specified date
date_lt        datetime.date  BEFORE 15-Mar-2000       internal date* is earlier than the specified date
sent_date      datetime.date  SENTON 15-Mar-2000       rfc2822 Date: header* is within the specified date
sent_date_gte  datetime.date  SENTSINCE 15-Mar-2000    rfc2822 Date: header* is within or later than the specified date
sent_date_lt   datetime.date  SENTBEFORE 15-Mar-2000   rfc2822 Date: header* is earlier than the specified date
size_gt        int >= 0       LARGER 1024              rfc2822 size larger than specified number of octets
size_lt        int >= 0       SMALLER 512              rfc2822 size smaller than specified number of octets
new            True           NEW                      have the Recent flag set but not the Seen flag
old            True           OLD                      do not have the Recent flag set
recent         True           RECENT                   have the Recent flag set
all            True           ALL                      all, criteria by default
uid            iter(str)|str  UID 1,2,17               corresponding to the specified unique identifier set
header         (str, str)     HEADER "AntiSpam" "5.8"  have a header that contains the specified str in the text
=============  =============  =======================  =================================================================

*When searching by dates - email's time and timezone are disregarding.

Actions with emails in folder
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| You can use 2 approaches to perform these operations:
| "by one" - Perform IMAP operation for each message separately per N commands
| "in bulk" - Perform IMAP operation for message set per 1 command
| Result of MailBox.fetch generator will be implicitly converted to uid list
|
.. code-block:: python

    with MailBox('imap.mail.com').login('test@mail.com', 'pwd', initial_folder='INBOX') as mailbox:

        # COPY all messages from current folder to folder1, *by one
        for msg in mailbox.fetch():
            res = mailbox.copy(msg.uid, 'INBOX/folder1')

        # MOVE all messages from current folder to folder2, *in bulk (implicit creation of uid list)
        mailbox.move(mailbox.fetch(), 'INBOX/folder2')

        # DELETE all messages from current folder, *in bulk (explicit creation of uid list)
        mailbox.delete([msg.uid for msg in mailbox.fetch()])

        # FLAG unseen messages in current folder as Answered and Flagged, *in bulk.
        flags = (imap_tools.StandardMessageFlags.ANSWERED, imap_tools.StandardMessageFlags.FLAGGED)
        mailbox.flag(mailbox.fetch('(UNSEEN)'), flags, True)

        # SEEN: mark all messages sent at 05.03.2007 in current folder as unseen, *in bulk
        mailbox.seen(mailbox.fetch("SENTON 05-Mar-2007"), False)

Actions with mailbox folders
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: python

    # LIST
    for folder in mailbox.folder.list('INBOX'):
        print(folder['flags'], folder['delim'], folder['name'])
    # SET
    mailbox.folder.set('INBOX')
    # GET
    current_folder = mailbox.folder.get()
    # CREATE
    mailbox.folder.create('folder1')
    # EXISTS
    is_exists = mailbox.folder.exists('folder1')
    # RENAME
    mailbox.folder.rename('folder1', 'folder2')
    # DELETE
    mailbox.folder.delete('folder2')
    # STATUS
    for status_key, status_val in mailbox.folder.status('some_folder').items():
        print(status_key, status_val)

Reasons
-------

- Excessive low level of imaplib library
- Other libraries contain various shortcomings or not convenient
- Open source projects makes world better

Release notes
-------------
 `release_notes.rst <https://github.com/ikvk/imap_tools/blob/master/release_notes.rst>`_

Thanks to
---------
 | `shilkazx <https://github.com/shilkazx>`_
 | `somepad <https://github.com/somepad>`_
 | `0xThiebaut <https://github.com/0xThiebaut>`_
 | `TpyoKnig <https://github.com/TpyoKnig>`_
 | `parchd-1 <https://github.com/parchd-1>`_
 | `dojasoncom <https://github.com/dojasoncom>`_
 | `RandomStrangerOnTheInternet <https://github.com/RandomStrangerOnTheInternet>`_
