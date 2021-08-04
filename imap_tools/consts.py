"""Lib constants"""
import re

SHORT_MONTH_NAMES = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

UID_PATTERN = re.compile(r'(^|\s+|\W)UID\s+(?P<uid>\d+)')


class MailMessageFlags:
    """
    System email message flags
    All system flags begin with "\"
    """
    SEEN = '\\Seen'
    ANSWERED = '\\Answered'
    FLAGGED = '\\Flagged'
    DELETED = '\\Deleted'
    DRAFT = '\\Draft'
    RECENT = '\\Recent'
    all = (
        SEEN, ANSWERED, FLAGGED, DELETED, DRAFT, RECENT
    )


class MailBoxFolderStatusOptions:
    """Valid mailbox folder status options"""
    MESSAGES = 'MESSAGES'
    RECENT = 'RECENT'
    UIDNEXT = 'UIDNEXT'
    UIDVALIDITY = 'UIDVALIDITY'
    UNSEEN = 'UNSEEN'
    all = (
        MESSAGES, RECENT, UIDNEXT, UIDVALIDITY, UNSEEN
    )
    description = (
        (MESSAGES, "The number of messages in the mailbox"),
        (RECENT, "The number of messages with the Recent flag set"),
        (UIDNEXT, "The next unique identifier value of the mailbox"),
        (UIDVALIDITY, "The unique identifier validity value of the mailbox"),
        (UNSEEN, "The number of messages which do not have the Seen flag set"),
    )
