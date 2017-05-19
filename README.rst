imap_tools
==========

Tool for work with e-mail messages and not with the imap protocol.

===================  ===============================================
Python version       3.3+
License              MIT
PyPI                 #TODO https://pypi.python.org/pypi/imap_tools/
===================  ===============================================

About
-----
There are many different libraries for working with e-mail via the imap protocol. Including the standard imaplib library.
However, these libraries contain various shortcomings, such as:

- excessive low level
- returned results are not ready to work with them
- lack of convenient tools for working with directories
- lack of convenient tools for working with letters in directories

This library takes into account the shortcomings of other libraries.
Main features:

- transparent work with letter attributes
- work with letters in directories (copy, delete, flag, move, seen)
- work with directories (list, set, get, create, exists, rename, delete, status)
- absence of external dependencies

Installation
------------

Install from Python Package Index (PyPI), using ``pip``:
::

    $ pip install -U imap_tools

Quick guide
-----------

Init:
^^^^^
.. code-block:: python

    mailbox = MailBox('imap.mail.com')
    mailbox.login('test@mail.com', 'password')

Message:
^^^^^^^^
.. code-block:: python

    for message in mailbox.fetch():
        message.id
        message.uid
        message.subject
        message.from_
        message.to
        message.date
        message.text
        message.html

Mailbox:
^^^^^^^^
.. code-block:: python

    # COPY all messages from current dir to folder1, by one
    for msg in mailbox.fetch():
        res = mailbox.copy(msg.uid, 'INBOX/folder1')

    # DELETE all messages from current dir to folder1, in bulk
    mailbox.delete([msg.uid for msg in mailbox.fetch()])

    # FLAG unseen messages in current folder as Answered and Flagged, in bulk
    mailbox.flag([msg.uid for msg in mailbox.fetch('(UNSEEN)')], ['Answered', 'Flagged'], True)

    # MOVE all messages from current dir to folder2, in bulk
    mailbox.move([msg.uid for msg in mailbox.fetch()], 'INBOX/folder2')

    # mark SEEN all messages sent at 05.03.2007 in current folder as unseen, in bulk
    mailbox.seen([msg.uid for msg in mailbox.fetch("SENTON 05-Mar-2007")], False)

Folders:
^^^^^^^^
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

