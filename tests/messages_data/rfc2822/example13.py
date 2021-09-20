import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='',
    from_='',
    to=(),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(1900, 1, 1, 0, 0),
    date_str='',
    text='To    : Mary Smith\r\n__\r\n          <mary@example.net>\r\nSubject     : Saying Hello\r\nDate  : Fri, 21 Nov 1997 09(comment):   55  :  06 -0600\r\nMessage-ID  : <1234   @   local(blah)  .machine .example>\r\n\r\nThis is a message just to say hello.\r\nSo, "Hello".\r\n',
    html='',
    headers={},
    attachments=[],
    from_values=None,
    to_values=(),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)