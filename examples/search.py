"""
Query builder examples.

NOTES:

# Infix notation (natural to humans)
    NOT ((FROM='11' OR TO="22" OR TEXT="33") AND CC="44" AND BCC="55")
# Prefix notation (Polish notation, IMAP version)
    NOT (((OR OR FROM "11" TO "22" TEXT "33") CC "44" BCC "55"))
# Python query builder
    NOT(AND(OR(from_='11', to='22', text='33'), cc='44', bcc='55'))

# python to prefix notation steps:
1. OR(from_=11, to=22, text=33) ->
    "(OR OR FROM "11" TO "22" TEXT "33")"
2. AND("(OR OR FROM "11" TO "22" TEXT "33")", cc='44', bcc='55') ->
    "AND(OR(from_='11', to='22', text='33'), cc='44', bcc='55')"
3. NOT("AND(OR(from_='11', to='22', text='33'), cc='44', bcc='55')") ->
    "NOT (((OR OR FROM "1" TO "22" TEXT "33") CC "44" BCC "55"))"
"""

import datetime as dt
from imap_tools import AND, OR, NOT, A, H, U

# date in the date list (date=date1 OR date=date3 OR date=date2)
q1 = OR(date=[dt.date(2019, 10, 1), dt.date(2019, 10, 10), dt.date(2019, 10, 15)])
# '(OR OR ON 1-Oct-2019 ON 10-Oct-2019 ON 15-Oct-2019)'

# date not in the date list (NOT(date=date1 OR date=date3 OR date=date2))
q2 = NOT(OR(date=[dt.date(2019, 10, 1), dt.date(2019, 10, 10), dt.date(2019, 10, 15)]))
# 'NOT ((OR OR ON 1-Oct-2019 ON 10-Oct-2019 ON 15-Oct-2019))'

# subject contains "hello" AND date greater than or equal dt.date(2019, 10, 10)
q3 = A(subject='hello', date_gte=dt.date(2019, 10, 10))
# '(SUBJECT "hello" SINCE 10-Oct-2019)'

# from contains one of the address parts
q4 = OR(from_=["@spam.ru", "@tricky-spam.ru"])
# '(OR FROM "@spam.ru" FROM "@tricky-spam.ru")'

# marked as seen and not flagged
q5 = AND(seen=True, flagged=False)
# '(SEEN UNFLAGGED)'

# (text contains tag15 AND subject contains tag15) OR (text contains tag10 AND subject contains tag10)
q6 = OR(AND(text='tag15', subject='tag15'), AND(text='tag10', subject='tag10'))
# '(OR (TEXT "tag15" SUBJECT "tag15") (TEXT "tag10" SUBJECT "tag10"))'

# (text contains tag15 OR subject contains tag15) OR (text contains tag10 OR subject contains tag10)
q7 = OR(OR(text='tag15', subject='tag15'), OR(text='tag10', subject='tag10'))
# '(OR (OR TEXT "tag15" SUBJECT "tag15") (OR TEXT "tag10" SUBJECT "tag10"))'

# header IsSpam contains '++' AND header CheckAntivirus contains '-'
q8 = A(header=[H('IsSpam', '++'), H('CheckAntivirus', '-')])
# '(HEADER "IsSpam" "++" HEADER "CheckAntivirus" "-")'

# UID range
q9 = A(uid=U('1034', '*'))
# '(UID 1034:*)'

# complex from README
q10 = A(OR(from_='from@ya.ru', text='"the text"'), NOT(OR(A(answered=False), A(new=True))), to='to@ya.ru')
# '((OR FROM "from@ya.ru" TEXT "\\"the text\\"") NOT ((OR (UNANSWERED) (NEW))) TO "to@ya.ru")'
