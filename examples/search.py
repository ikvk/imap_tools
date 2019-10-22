from imap_tools import Q, MailBox

# explain
"""
# infix notation
NOT ((FROM='11' OR TO="22" OR TEXT="33") AND CC="44" AND BCC="55")
# prefix notation (imap, Polish notation)
NOT (((OR OR FROM "11" TO "22" TEXT "33") CC "44" BCC "55"))
# python builder 
NOT(AND(OR(from_='11', to='22', text='33'), cc='44', bcc='55'))

# python to prefix steps
1. OR(1=11, 2=22, 3=33) -> "(OR OR FROM "11" TO "22" TEXT "33")"
2. AND("(OR OR FROM "11" TO "22" TEXT "33")", cc='44', bcc='55') -> "AND(OR(from_='11', to='22', text='33'), cc='44', bcc='55')"
3. NOT("AND(OR(from_='11', to='22', text='33'), cc='44', bcc='55')") -> "NOT (((OR OR FROM "1" TO "22" TEXT "33") CC "44" BCC "55"))"
"""

import datetime as dt
from imap_tools import AND, OR, NOT, Q, H

with MailBox('imap.some.ru').login('user', 'pwd', 'INBOX') as mailbox:
    # multi OR
    for msg in mailbox.fetch(NOT(OR(date=[dt.date(2019, 10, 1), dt.date(2019, 10, 10), dt.date(2019, 10, 15)]))):
        print(msg.subject)
