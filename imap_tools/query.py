"""IMAP Query builder"""
import datetime
import collections

from .utils import cleaned_uid_set


class LogicOperator(collections.UserString):
    def __init__(self, *args, **kwargs):
        self.converted = args
        self.unconverted = kwargs
        for val in self.converted:
            if not any(isinstance(val, t) for t in (str, collections.UserString)):
                raise ValueError('Unexpected type "{}" for converted part, str like obj expected'.format(type(val)))
        converted_as_str = ' '.join((str(i) for i in self.converted))
        unconverted_as_str = ParamConverter(self.unconverted).to_str()
        self.full_str = ' '.join((unconverted_as_str, converted_as_str)).strip()
        super().__init__(self._build_query())

    def _build_query(self):
        raise NotImplementedError


class AND(LogicOperator):
    """When multiple keys are specified, the result is the intersection of all the messages that match those keys."""

    def _build_query(self):
        return self.full_str


class OR(LogicOperator):
    """OR <search-key1> <search-key2> Messages that match either search key."""

    def _build_query(self):
        return '(OR {})'.format(self.full_str)


class NOT(LogicOperator):
    """NOT <search-key> Messages that do not match the specified search key."""

    def _build_query(self):
        return '(NOT {})'.format(self.full_str)


Q = AND  # Short alias for AND


class ParamConverter:
    """Convert search params to IMAP format"""

    short_month_names = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov')

    def __init__(self, params):
        self.params = params

    def to_str(self) -> str:
        converted = []
        for key, val in self.params.items():
            convert_func = getattr(self, 'convert_{}'.format(key), None)
            if not convert_func:
                raise ValueError('"{}" parameter not found.'.format(key))
            converted.append(convert_func(key, val))
        return ' '.join(converted)

    def format_date(self, value: datetime.date) -> str:
        return '{}-{}-{}'.format(value.day, self.short_month_names[value.month - 1], value.year)

    @staticmethod
    def cleaned_str(key, value) -> str:
        if type(value) is not str:
            raise ValueError('"{}" expected str value, "{}" received'.format(key, type(value)))
        return str(value)

    @staticmethod
    def cleaned_date(key, value) -> datetime.date:
        if type(value) is not datetime.date:
            raise ValueError('"{}" expected datetime.date value, "{}" received'.format(key, type(value)))
        return value

    @staticmethod
    def cleaned_bool(key, value) -> bool:
        if type(value) is not bool:
            raise ValueError('"{}" expected bool value, "{}" received'.format(key, type(value)))
        return bool(value)

    @staticmethod
    def cleaned_true(key, value) -> True:
        if value is not True:
            raise ValueError('"{}" expected "True", "{}" received'.format(key, type(value)))
        return True

    @staticmethod
    def cleaned_int(key, value) -> int:
        if type(value) is not int:
            raise ValueError('"{}" expected int value, "{}" received'.format(key, type(value)))
        return int(value)

    @staticmethod
    def cleaned_uid(key, value) -> str:
        try:
            uid_set = cleaned_uid_set(value)
        except ValueError as e:
            raise ValueError('{} parse error: {}'.format(key, str(e)))
        return uid_set

    def convert_answered(self, key, value):
        """Messages [with/without] the Answered flag set. (ANSWERED, UNANSWERED)"""
        return 'ANSWERED' if self.cleaned_bool(key, value) else 'UNANSWERED'

    def convert_seen(self, key, value):
        """Messages that [have/do not have] the Seen flag set. (SEEN, UNSEEN)"""
        return 'SEEN' if self.cleaned_bool(key, value) else 'UNSEEN'

    def convert_flagged(self, key, value):
        """Messages [with/without] the Flagged flag set. (FLAGGED, UNFLAGGED)"""
        return 'FLAGGED' if self.cleaned_bool(key, value) else 'UNFLAGGED'

    def convert_draft(self, key, value):
        """Messages that [have/do not have] the Draft flag set. (DRAFT, UNDRAFT)"""
        return 'DRAFT' if self.cleaned_bool(key, value) else 'UNDRAFT'

    def convert_deleted(self, key, value):
        """Messages that [have/do not have] the Deleted flag set. (DELETED, UNDELETED)"""
        return 'DELETED' if self.cleaned_bool(key, value) else 'UNDELETED'

    def convert_keyword(self, key, value):
        """Messages with the specified keyword flag set. (KEYWORD)"""
        return 'KEYWORD {}'.format(self.cleaned_str(key, value))

    def convert_no_keyword(self, key, value):
        """Messages that do not have the specified keyword flag set. (UNKEYWORD)"""
        return 'UNKEYWORD {}'.format(self.cleaned_str(key, value))

    def convert_from_(self, key, value):
        """Messages that contain the specified string in the envelope structure's FROM field."""
        return 'FROM {}'.format(self.cleaned_str(key, value))

    def convert_to(self, key, value):
        """Messages that contain the specified string in the envelope structure's TO field."""
        return 'TO {}'.format(self.cleaned_str(key, value))

    def convert_subject(self, key, value):
        """Messages that contain the specified string in the envelope structure's SUBJECT field."""
        return 'SUBJECT {}'.format(self.cleaned_str(key, value))

    def convert_body(self, key, value):
        """Messages that contain the specified string in the body of the message."""
        return 'BODY {}'.format(self.cleaned_str(key, value))

    def convert_text(self, key, value):
        """Messages that contain the specified string in the header or body of the message."""
        return 'TEXT {}'.format(self.cleaned_str(key, value))

    def convert_bcc(self, key, value):
        """Messages that contain the specified string in the envelope structure's BCC field."""
        return 'BCC {}'.format(self.cleaned_str(key, value))

    def convert_cc(self, key, value):
        """Messages that contain the specified string in the envelope structure's CC field."""
        return 'CC {}'.format(self.cleaned_str(key, value))

    def convert_date(self, key, value):
        """
        Messages whose internal date (disregarding time and timezone)
        is within the specified date. (ON)
        """
        return 'DATE {}'.format(self.format_date(self.cleaned_date(key, value)))

    def convert_date_gt(self, key, value):
        """
        Messages whose internal date (disregarding time and timezone)
        is within or later than the specified date. (SINCE)
        """
        return 'SINCE {}'.format(self.format_date(self.cleaned_date(key, value)))

    def convert_date_lt(self, key, value):
        """
        Messages whose internal date (disregarding time and timezone)
        is earlier than the specified date. (BEFORE)
        """
        return 'BEFORE {}'.format(self.format_date(self.cleaned_date(key, value)))

    def convert_sent_date(self, key, value):
        """
        Messages whose [RFC-2822] Date: header (disregarding time and timezone)
        is within the specified date. (SENTON)
        """
        return 'SENTON {}'.format(self.format_date(self.cleaned_date(key, value)))

    def convert_sent_date_gt(self, key, value):
        """
        Messages whose [RFC-2822] Date: header (disregarding time and timezone)
        is within or later than the specified date. (SENTSINCE)
        """
        return 'SENTSINCE {}'.format(self.format_date(self.cleaned_date(key, value)))

    def convert_sent_date_lt(self, key, value):
        """
        Messages whose [RFC-2822] Date: header (disregarding time and timezone)
        is earlier than the specified date. (SENTBEFORE)
        """
        return 'SENTBEFORE {}'.format(self.format_date(self.cleaned_date(key, value)))

    def convert_size_gt(self, key, value):
        """Messages with an [RFC-2822] size larger than the specified number of octets. (LARGER)"""
        return 'LARGER {}'.format(self.cleaned_int(key, value))

    def convert_size_lt(self, key, value):
        """Messages with an [RFC-2822] size smaller than the specified number of octets. (SMALLER)"""
        return 'SMALLER {}'.format(self.cleaned_int(key, value))

    def convert_new(self, key, value):
        """
        Messages that have the Recent flag set but not the Seen flag.
        This is functionally equivalent to "(RECENT UNSEEN)".
        """
        return 'NEW {}'.format(self.cleaned_true(key, value))

    def convert_old(self, key, value):
        """
        Messages that do not have the Recent flag set.
        This is functionally equivalent to "NOT RECENT" (as opposed to "NOT NEW").
        """
        return 'OLD {}'.format(self.cleaned_true(key, value))

    def convert_recent(self, key, value):
        """Messages that have the Recent flag set."""
        return 'RECENT {}'.format(self.cleaned_true(key, value))

    def convert_all(self, key, value):
        """All messages in the mailbox; the default initial key for ANDing."""
        return 'ALL {}'.format(self.cleaned_true(key, value))

    def convert_header(self, key, value):
        """
        Messages that have a header with the specified field-name (as defined in [RFC-2822])
        and that contains the specified string in the text of the header (what comes after the colon).
        If the string to search is zero-length, this matches all messages that have a header line
        with the specified field-name regardless of the contents.
        """
        return 'HEADER {} {}'.format(
            self.cleaned_str('{} field-name'.format(key), value),
            self.cleaned_str('{} field-value'.format(key), value))

    def convert_uid(self, key, value):
        """Messages with unique identifiers corresponding to the specified unique identifier set."""
        return 'UID {}'.format(self.cleaned_uid(key, value))


"""
# Messages [with/without] the \Answered flag set. (ANSWERED, UNANSWERED)
ANSWERED=bool
# Messages that [have/do not have] the \Seen flag set. (SEEN, UNSEEN)
SEEN=bool
# Messages [with/without] the \Flagged flag set. (FLAGGED, UNFLAGGED)
FLAGGED=bool
# Messages that [have/do not have] the \Draft flag set. (DRAFT, UNDRAFT)
DRAFT=bool
# Messages that [have/do not have] the \Deleted flag set. (DELETED, UNDELETED)
DELETED=bool 
# Messages with the specified keyword flag set. (KEYWORD)
KEYWORD=str <flag> 
# Messages that do not have the specified keyword flag set. (UNKEYWORD)
NO_KEYWORD=str <flag>

# Messages that contain the specified string in the envelope structure's FROM field.
FROM=str
# Messages that contain the specified string in the envelope structure's TO field.
TO=str
# Messages that contain the specified string in the envelope structure's SUBJECT field.
SUBJECT=str
# Messages that contain the specified string in the body of the message.
BODY=str
# Messages that contain the specified string in the header or body of the message.
TEXT=str
# Messages that contain the specified string in the envelope structure's BCC field.
BCC=str
# Messages that contain the specified string in the envelope structure's CC field.
CC=str

# Messages whose internal date (disregarding time and timezone) is within the specified date. (ON)
DATE=date
# Messages whose internal date (disregarding time and timezone) is within or later than the specified date. (SINCE)
DATE_GT=date
# Messages whose internal date (disregarding time and timezone) is earlier than the specified date. (BEFORE)
DATE_LT=date
# Messages whose [RFC-2822] Date: header (disregarding time and timezone) is within the specified date. (SENTON)
SENT_DATE=date
# Messages whose [RFC-2822] Date: header (disregarding time and timezone) is within or later than the specified date. (SENTSINCE)
SENT_DATE_GT=date
# Messages whose [RFC-2822] Date: header (disregarding time and timezone) is earlier than the specified date. (SENTBEFORE)
SENT_DATE_LT=date

# Messages with an [RFC-2822] size larger than the specified number of octets. (LARGER)
SIZE_GT=int
# Messages with an [RFC-2822] size smaller than the specified number of octets. (SMALLER)
SIZE_LT=int

# Messages that have the \Recent flag set but not the \Seen flag. This is functionally equivalent to "(RECENT UNSEEN)".
NEW=True
# Messages that do not have the \Recent flag set. This is functionally equivalent to "NOT RECENT" (as opposed to "NOT NEW").
OLD=True
# Messages that have the \Recent flag set.
RECENT=True
# by default ALL 
ALL=True

# Messages that have a header with the specified field-name (as defined in [RFC-2822]) 
# and that contains the specified string in the text of the header (what comes after the colon).  
# If the string to search is zero-length, this matches all messages that have a header line 
# with the specified field-name regardless of the contents.
HEADER=(<field-name>:str, str)

Messages with unique identifiers corresponding to the specified unique identifier set. Sequence set ranges are permitted.
UID=<uid_list>: list

Example: C: A282 SEARCH FLAGGED SINCE 1-Feb-1994 NOT FROM "Smith"
 S: * SEARCH 2 84 882
 S: A282 OK SEARCH completed
 C: A283 SEARCH TEXT "string not in mailbox"
 S: * SEARCH
 S: A283 OK SEARCH completed
 C: A284 SEARCH CHARSET UTF-8 TEXT {6}
 C: XXXXXX
 S: * SEARCH 43
 S: A284 OK SEARCH completed
 
KEYWORD
https://stackoverflow.com/questions/3632102/imap-custom-keywords
"""
