.. http://docutils.sourceforge.net/docs/user/rst/quickref.html

imap_tools
==========

Effective working with email messages using IMAP protocol.

===================  ====================================================
Python version       3.3+
License              MIT
PyPI                 https://pypi.python.org/pypi/imap_tools/
IMAP                 VERSION 4rev1 - https://tools.ietf.org/html/rfc3501
===================  ====================================================

Features
--------
- transparent work with letter attributes
- work with letters in directories (copy, delete, flag, move, seen)
- work with directories (list, set, get, create, exists, rename, delete, status)
- no dependencies

Installation
------------
::

    $ pip install imap_tools

Quick guide
-----------

Init:
^^^^^
.. code-block:: python

    from imap_tools import MailBox
    mailbox = MailBox('imap.mail.com')
    mailbox.login('test@mail.com', 'password')

Message attributes:
^^^^^^^^^^^^^^^^^^^
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
        # any message attribute: message.obj['Message-ID'], message.obj['X-Google-Smtp-Source'] ...

Actions with messages in folder:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: python

    # NOTE: You can use 2 approaches to perform these operations
    # "by one" - Perform operation for each message separately per N commands
    # "in bulk" - Perform operation for message set per 1 command

    # COPY all messages from current dir to folder1, *by one
    for msg in mailbox.fetch():
        res = mailbox.copy(msg.uid, 'INBOX/folder1')

    # DELETE all messages from current dir to folder1, *in bulk
    mailbox.delete([msg.uid for msg in mailbox.fetch()])

    # FLAG unseen messages in current folder as Answered and Flagged, *in bulk
    mailbox.flag(mailbox.fetch('(UNSEEN)'), ['Answered', 'Flagged'], True)

    # MOVE all messages from current dir to folder2, *in bulk
    mailbox.move(mailbox.fetch(), 'INBOX/folder2')

    # mark SEEN all messages sent at 05.03.2007 in current folder as unseen, *in bulk
    mailbox.seen(mailbox.fetch("SENTON 05-Mar-2007"), False)

Actions with folders:
^^^^^^^^^^^^^^^^^^^^^
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

Fetch params
^^^^^^^^^^^^

MailBox.fetch - Mail message generator

* *search_criteria*: message search criteria (see examples at ./doc/imap_search_criteria.txt)
* *limit*: limit on the number of read emails, useful for actions with a large number of messages, like "move"
* *miss_defect*: miss emails with defects
* *miss_no_uid*: miss emails without uid
* *mark_seen*: mark emails as seen on fetch

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
 | `thiebautdotdev <https://github.com/thiebautdotdev>`_
 | `TpyoKnig <https://github.com/TpyoKnig>`_
 | `parchd-1 <https://github.com/parchd-1>`_
 | `dojasoncom <https://github.com/dojasoncom>`_
