"""
Explanation:

# infix notation
NOT ((FROM='11' OR TO="22" OR TEXT="33") AND CC="44" AND BCC="55")
# prefix notation (Polish notation, IMAP version)
NOT (((OR OR FROM "11" TO "22" TEXT "33") CC "44" BCC "55"))
# python builder
NOT(AND(OR(from_='11', to='22', text='33'), cc='44', bcc='55'))

# python to prefix steps
1. OR(1=11, 2=22, 3=33) ->
    "(OR OR FROM "11" TO "22" TEXT "33")"
2. AND("(OR OR FROM "11" TO "22" TEXT "33")", cc='44', bcc='55') ->
    "AND(OR(from_='11', to='22', text='33'), cc='44', bcc='55')"
3. NOT("AND(OR(from_='11', to='22', text='33'), cc='44', bcc='55')") ->
    "NOT (((OR OR FROM "1" TO "22" TEXT "33") CC "44" BCC "55"))"
"""

import datetime as dt
from imap_tools import AND, OR, NOT, Q, H

# date in the date list (date=date1 OR date=date3 OR date=date2)
q1 = OR(date=[dt.date(2019, 10, 1), dt.date(2019, 10, 10), dt.date(2019, 10, 15)])

# date not in the date list (NOT(date=date1 OR date=date3 OR date=date2))
q2 = NOT(OR(date=[dt.date(2019, 10, 1), dt.date(2019, 10, 10), dt.date(2019, 10, 15)]))

# subject contains "hello" AND date greater than or equal dt.date(2019, 10, 10)
q3 = Q(subject='hello', date_gte=dt.date(2019, 10, 10))

# from contains one of the address parts
q4 = OR(from_=["@spam.ru", "@tricky-spam.ru"])

# marked as seen and flagged
q5 = AND(seen=True, flagged=True)

# (text contains tag15 AND subject contains tag15) OR (text contains tag10 AND subject contains tag10)
q6 = OR(AND(text='tag15', subject='tag15'), AND(text='tag10', subject='tag10'))

# (text contains tag15 OR subject contains tag15) OR (text contains tag10 OR subject contains tag10)
q7 = OR(OR(text='tag15', subject='tag15'), OR(text='tag10', subject='tag10'))

# header IsSpam contains '++' AND header CheckAntivirus contains '-'
q8 = Q(header=[H('IsSpam', '++'), H('CheckAntivirus', '-')])
