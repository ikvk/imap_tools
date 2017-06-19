imap_tools
==========

Effective working with email messages using IMAP protocol.

:Python version: 3.3+
:License: MIT
:PyPI: https://pypi.python.org/pypi/imap_tools/

Features
--------
- transparent work with letter attributes
- work with letters in directories (copy, delete, flag, move, seen)
- work with directories (list, set, get, create, exists, rename, delete, status)
- no external dependencies

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

    for message in mailbox.fetch():
        message.id
        message.uid
        message.subject
        message.from_
        message.to
        message.date
        message.text
        message.html
        message.flags
        for filename, payload in message.get_attachments():
            filename, payload

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
    mailbox.flag([msg.uid for msg in mailbox.fetch('(UNSEEN)')], ['Answered', 'Flagged'], True)

    # MOVE all messages from current dir to folder2, *in bulk
    mailbox.move([msg.uid for msg in mailbox.fetch()], 'INBOX/folder2')

    # mark SEEN all messages sent at 05.03.2007 in current folder as unseen, *in bulk
    mailbox.seen([msg.uid for msg in mailbox.fetch("SENTON 05-Mar-2007")], False)

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


Reasons
-------
There are many different libraries for working with e-mail via the imap protocol. Including imaplib library.
However, these libraries contain various shortcomings, such as:

- excessive low level
- returned results are not ready to work with them
- no convenient tools for working with: directories, letters in directories
