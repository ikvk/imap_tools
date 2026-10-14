This directory (mailnews/test/data) contains various support files for the
testing of mailnews.

Not all files will be documented here, but this will be a place for some
documentation.

signons-mailnews1.8.txt
-----------------------

This is a passwords file from gecko 1.8/gecko 1.9/early 1.9.1
(TB 1.5/2.0/pre 3.0 beta 1, SM 1.0/1.5/early 2.0). It is used as a test input
for several test_*Password.js files to check that we load usernames and
passwords correctly from the legacy file.

abLists1.mab
------------

An address book with 5 cards and 3 lists. The cards only have the email and
prefer mail format set:

test1@invalid.com  unknown
test2@invalid.com  unknown
test3@invalid.com  unknown
test4@invalid.com  plain text
test5@invalid.com  html

There are 3 lists, TestList1, TestList2 and TestList3. They have the following
cards:

TestList1:

test1@invalid.com
test2@invalid.com
test3@invalid.com

TestList2:

test4@invalid.com

TestList3:

test5@invalid.com


abLists2.mab
------------

The same as abLists1.mab, but with com.invalid instead of invalid.com, and ListTestX instead of TestListX.

mime-torture
------------

This is a file which is known as the MIME torture test. It contains several
nested multipart/* and message/* segments; as its explanation describes:

  This is a demonstration of multi-part mail with encapsulated messages.  This
  is a very complex message whose purpose it is to exercise software using the
  new multi-part message standard.

The original source of this file is unknown, but a copy can be found at
<http://sourceforge.net/projects/kmmail/files/MIME%20Torture%20Tests/>.




mbox_modern
-----------

A simple mbox in the form that Thunderbird currently seems to save (as
of Nov 2018).
Separator lines are of the form:

From - Fri Aug 24 11:55:47 2018

Lines beginning with "From " within the message body are escaped
by prefixing a space.


mbox_unquoted
-------------

Old-style mbox. This seems to be what Thunderbird was storing back around
2005, and so there are likely to be a bunch of these out in the wild.

Separator lines are lines containing only: "From "
Lines within the message body beginning with "From " are not escaped in
any way.


mbox_mboxrd
-----------

Example of the mboxrd variant, taken from the wikipedia mbox page.
Separator lines are of the form:

From MAILER-DAEMON Fri Jul  8 12:08:34 2011

(note that MAILER-DAEMON is a special case - this is where an
email address usually goes, but MAILER-DAEMON can be used instead).

"From " lines within the message body are escaped by prefixing with
a '>' char.

