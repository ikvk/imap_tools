.. http://docutils.sourceforge.net/docs/user/rst/quickref.html

imap_tools
==========

Effective working with email using IMAP protocol.

===================  ====================================================
Python version       3.3+
License              MIT
PyPI                 https://pypi.python.org/pypi/imap_tools/
IMAP                 VERSION 4rev1 - https://tools.ietf.org/html/rfc3501
===================  ====================================================

.. contents::

Features
--------
- Transparent work with email message attributes
- Work with emails in directories (copy, delete, flag, move, seen)
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

    from imap_tools import MailBox

    mailbox = MailBox('imap.mail.com')
    mailbox.login('test@mail.com', 'password', initial_folder='INBOX')
    subjects = [msg.subject for msg in mailbox.fetch()]  # get list of email subjects from INBOX folder
    mailbox.logout()
    # OR the same otherwise
    with MailBox('imap.mail.com').login('test@mail.com', 'password') as mailbox:
        subjects = [msg.subject for msg in mailbox.fetch()]

MailBox.fetch - email message generator, params:

* *criteria*: message search criteria, `examples <https://github.com/ikvk/imap_tools/tree/master/examples>`_
* *limit*: limit on the number of read emails, useful for actions with a large number of messages, like "move"
* *miss_defect*: miss emails with defects
* *miss_no_uid*: miss emails without uid
* *mark_seen*: mark emails as seen on fetch

Email attributes
^^^^^^^^^^^^^^^^
.. code-block:: python

    # NOTE: All message properties are cached by functools.lru_cache

    for message in mailbox.fetch():
        message.id
        message.uid
        message.subject
        message.from_
        message.to
        message.cc
        message.bcc
        message.date
        message.text
        message.html
        message.flags
        message.from_values
        message.to_values
        message.cc_values
        message.bcc_values
        for filename, payload in message.attachments:
            filename, payload
        # Any message attribute: message.obj['Message-ID'], message.obj['X-Google-Smtp-Source'] ...

Actions with emails in folder
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: python

    # NOTE: You can use 2 approaches to perform these operations
    # "by one" - Perform IMAP operation for each message separately per N commands
    # "in bulk" - Perform IMAP operation for message set per 1 command

    with MailBox('imap.mail.com').login('test@mail.com', 'pwd', initial_folder='INBOX') as mailbox:

        # COPY all messages from current dir to folder1, *by one
        for msg in mailbox.fetch():
            res = mailbox.copy(msg.uid, 'INBOX/folder1')

        # MOVE all messages from current dir to folder2, *in bulk (implicit creation of uid list)
        mailbox.move(mailbox.fetch(), 'INBOX/folder2')

        # DELETE all messages from current dir, *in bulk (explicit creation of uid list)
        mailbox.delete([msg.uid for msg in mailbox.fetch()])

        # FLAG unseen messages in current folder as Answered and Flagged, *in bulk.
        flags = (imap_tools.StandardMessageFlags.ANSWERED, imap_tools.StandardMessageFlags.FLAGGED)
        mailbox.flag(mailbox.fetch('(UNSEEN)'), flags, True)

        # SEEN: mark all messages sent at 05.03.2007 in current folder as unseen, *in bulk
        mailbox.seen(mailbox.fetch("SENTON 05-Mar-2007"), False)

Actions with mailbox folders
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: python

    mailbox.login('test@mail.com', 'pwd')

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

    mailbox.logout()

Reasons
-------
There are many different libraries for working with e-mail via the imap protocol. Including imaplib library.
However, these libraries contain various shortcomings, such as:

- excessive low level
- returned results are not ready to work with them
- no convenient tools for working with: directories, letters in directories

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
