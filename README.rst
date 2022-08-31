.. http://docutils.sourceforge.net/docs/user/rst/quickref.html

.. |nbsp| unicode:: 0xA0
   :trim:

imap_tools 📧
=============

High level lib for work with email by IMAP:

- Basic message operations: fetch, uids, numbers
- Parsed email message attributes
- Query builder for search criteria
- Actions with emails: copy, delete, flag, move, append
- Actions with folders: list, set, get, create, exists, rename, subscribe, delete, status
- IDLE commands: start, poll, stop, wait
- Exceptions on failed IMAP operations
- No external dependencies, tested

.. image:: https://img.shields.io/pypi/dm/imap_tools.svg?style=social

===============  ================================================================================================
Python version   3.5+
License          Apache-2.0
PyPI             https://pypi.python.org/pypi/imap_tools/
RFC              `IMAP4.1 <https://tools.ietf.org/html/rfc3501>`_,
                 `EMAIL <https://tools.ietf.org/html/rfc3501>`_,
                 `IMAP related RFCs <https://github.com/ikvk/imap_tools/blob/master/docs/IMAP_related_RFCs.txt>`_
===============  ================================================================================================

.. contents::

Installation
------------
::

    $ pip install imap-tools

Guide
-----

Basic
^^^^^

Info about lib are at: *this page*, docstrings, issues, pull requests, examples, source, stackoverflow.com

.. code-block:: python

    from imap_tools import MailBox, AND

    # Get date, subject and body len of all emails from INBOX folder
    with MailBox('imap.mail.com').login('test@mail.com', 'pwd') as mailbox:
        for msg in mailbox.fetch():
            print(msg.date, msg.subject, len(msg.text or msg.html))

`Description of this^ example <https://github.com/ikvk/imap_tools/blob/master/examples/basic.py>`_.

MailBox, MailBoxTls, MailBoxUnencrypted - for create mailbox client. `TLS example <https://github.com/ikvk/imap_tools/blob/master/examples/tls.py>`_.

BaseMailBox.login, BaseMailBox.login_utf8, MailBox.xoauth2, BaseMailBox.logout - authentication functions, they support context manager.

BaseMailBox.fetch - first searches email nums by criteria in current folder, then fetch and yields `MailMessage <#email-attributes>`_:

* *criteria* = 'ALL', message search criteria, `query builder <#search-criteria>`_
* *charset* = 'US-ASCII', indicates charset of the strings that appear in the search criteria. See rfc2978
* *limit* = None, limit on the number of read emails, useful for actions with a large number of messages, like "move"
* *miss_no_uid* = True, miss emails without uid
* *mark_seen* = True, mark emails as seen on fetch
* *reverse* = False, in order from the larger date to the smaller
* *headers_only* = False, get only email headers (without text, html, attachments)
* *bulk* = False, False - fetch each message separately per N commands - low memory consumption, slow; True - fetch all messages per 1 command - high memory consumption, fast

BaseMailBox.uids - search mailbox for matching message uids in current folder, returns [str | None]

* *criteria* = 'ALL', message search criteria, `query builder <#search-criteria>`_
* *charset* = 'US-ASCII', indicates charset of the strings that appear in the search criteria. See rfc2978
* *miss_no_uid* = True, not add None values to result when uid item not matched to pattern

BaseMailBox.<action> - `copy, move, delete, flag, append <#actions-with-emails>`_

BaseMailBox.folder - `folder manager <#actions-with-folders>`_

BaseMailBox.idle - `idle manager <#idle-workflow>`_

BaseMailBox.numbers - search mailbox for matching message numbers in current folder, returns [str]

BaseMailBox.client - imaplib.IMAP4/IMAP4_SSL client instance.

Email attributes
^^^^^^^^^^^^^^^^

MailMessage and MailAttachment public attributes are cached by functools.lru_cache

.. code-block:: python

    for msg in mailbox.fetch():  # generator: imap_tools.MailMessage
        msg.uid          # str | None: '123'
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
        msg.from_values      # imap_tools.EmailAddress | None
        msg.to_values        # tuple: (imap_tools.EmailAddress,)
        msg.cc_values        # tuple: (imap_tools.EmailAddress,)
        msg.bcc_values       # tuple: (imap_tools.EmailAddress,)
        msg.reply_to_values  # tuple: (imap_tools.EmailAddress,)
        # EmailAddress(name='Ya', email='im@ya.ru')  # "full" property = 'Ya <im@ya.ru>'

Search criteria
^^^^^^^^^^^^^^^

You can use 3 types for "criteria" argument of MailBox methods: fetch, uids, numbers:

.. code-block:: python

    from imap_tools import AND

    mailbox.fetch(AND(subject='weather'))  # query, the str-like object
    mailbox.fetch('TEXT "hello"')          # str
    mailbox.fetch(b'TEXT "\xd1\x8f"')      # bytes, *charset arg is ignored

Use "charset" argument for encode criteria to the desired encoding. If "criteria" is bytes - encoding will be ignored.

.. code-block:: python

    mailbox.uids(A(subject='жёлтый'), charset='utf8')

Query builder implements all search logic described in `rfc3501 <https://tools.ietf.org/html/rfc3501#section-6.4.4>`_.
It uses this classes:

========  =====  ========================================== ======================================
Class     Alias  Description                                Arguments
========  =====  ========================================== ======================================
AND       A      Combine conditions by logical "AND"        Search keys (see table below) | str
OR        O      Combine conditions by logical "OR"         Search keys (see table below) | str
NOT       N      Invert the result of a logical expression  AND/OR instances | str
Header    H      Header value for search by header key      name: str, value: str
UidRange  U      UID range value for search by uid key      start: str, end: str
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

=============  ===============  ======================  ================================================================
Key            Types            Results                 Description
=============  ===============  ======================  ================================================================
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
=============  ===============  ======================  ================================================================

Server side search notes:

* For string search keys a message matches if the string is a substring of the field. The matching is case-insensitive.
* When searching by dates - email's time and timezone are disregarding.

Actions with emails
^^^^^^^^^^^^^^^^^^^

First of all read about uid `at rfc3501 <https://tools.ietf.org/html/rfc3501#section-2.3.1.1>`_.

Action's uid_list arg may takes:

* str, that is comma separated uids
* Sequence, that contains str uids

To get uids, use the maibox methods: uids, fetch.

For actions with a large number of messages imap command may be too large and will cause exception at server side,
use 'limit' argument for fetch in this case.

.. code-block:: python

    with MailBox('imap.mail.com').login('test@mail.com', 'pwd', initial_folder='INBOX') as mailbox:

        # COPY messages with uid in 23,27 from current folder to folder1
        mailbox.copy('23,27', 'folder1')

        # MOVE all messages from current folder to INBOX/folder2
        mailbox.move(mailbox.uids(), 'INBOX/folder2')

        # DELETE messages with 'cat' word in its html from current folder
        mailbox.delete([msg.uid for msg in mailbox.fetch() if 'cat' in msg.html])

        # FLAG unseen messages in current folder as \Seen, \Flagged and TAG1
        flags = (imap_tools.MailMessageFlags.SEEN, imap_tools.MailMessageFlags.FLAGGED, 'TAG1')
        mailbox.flag(mailbox.uids(AND(seen=False)), flags, True)

        # APPEND: add message to mailbox directly, to INBOX folder with \Seen flag and now date
        with open('/tmp/message.eml', 'rb') as f:
            msg = imap_tools.MailMessage.from_bytes(f.read())  # *or use bytes instead MailMessage
        mailbox.append(msg, 'INBOX', dt=None, flag_set=[imap_tools.MailMessageFlags.SEEN])

Actions with folders
^^^^^^^^^^^^^^^^^^^^

BaseMailBox.login/xoauth2 has initial_folder arg, that is "INBOX" by default, use None for not set folder on login.

.. code-block:: python

    with MailBox('imap.mail.com').login('test@mail.com', 'pwd') as mailbox:

        # LIST: get all subfolders of the specified folder (root by default)
        for f in mailbox.folder.list('INBOX'):
            print(f)  # FolderInfo(name='INBOX|cats', delim='|', flags=('\\Unmarked', '\\HasChildren'))

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

IDLE workflow
^^^^^^^^^^^^^

IDLE logic are in mailbox.idle manager, its methods are in the table below:

======== ============================================================================== ================================
Method   Description                                                                    Arguments
======== ============================================================================== ================================
start    Switch on mailbox IDLE mode
poll     Poll for IDLE responses                                                        timeout: |nbsp| Optional[float]
stop     Switch off mailbox IDLE mode
wait     Switch on IDLE, poll responses, switch off IDLE on response, return responses  timeout: |nbsp| Optional[float]
======== ============================================================================== ================================

.. code-block:: python

    from imap_tools import MailBox, A

    # waiting for updates 60 sec, print unseen immediately if any update
    with MailBox('imap.my.moon').login('acc', 'pwd', 'INBOX') as mailbox:
        responses = mailbox.idle.wait(timeout=60)
        if responses:
            for msg in mailbox.fetch(A(seen=False)):
                print(msg.date, msg.subject)
        else:
            print('no updates in 60 sec')

Read docstrings and see `detailed examples <https://github.com/ikvk/imap_tools/blob/master/examples/idle.py>`_.

Exceptions
^^^^^^^^^^

Most lib server actions raises exception if result is marked as not success.

Custom lib exceptions here: `errors.py <https://github.com/ikvk/imap_tools/blob/master/imap_tools/errors.py>`_.

Release notes
-------------

History of important changes: `release_notes.rst <https://github.com/ikvk/imap_tools/blob/master/docs/release_notes.rst>`_

Contribute
----------

If you found a bug or have a question, then:

1. Look for answer at: this page, issues, pull requests, examples, source, RFCs, stackoverflow.com, internet.
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
`Yannik <https://github.com/Yannik>`_,
`pete312 <https://github.com/pete312>`_,
`edkedk99 <https://github.com/edkedk99>`_,
`UlisseMini <https://github.com/UlisseMini>`_,
`Nicarex <https://github.com/Nicarex>`_,
`RanjithNair1980 <https://github.com/RanjithNair1980>`_,
`NickC-NZ <https://github.com/NickC-NZ>`_,
`mweinelt <https://github.com/mweinelt>`_,
`lucbouge <https://github.com/lucbouge>`_,
`JacquelinCharbonnel <https://github.com/JacquelinCharbonnel>`_,
`stumpylog <https://github.com/stumpylog>`_

Donate
------
`✋ I want to help this library <https://github.com/ikvk/imap_tools/blob/master/docs/donate.rst>`_
