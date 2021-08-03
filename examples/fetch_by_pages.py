from imap_tools import MailBox

with MailBox('imap.mail.com').login('test@mail.com', 'pwd', 'INBOX') as mailbox:
    criteria = 'ALL'
    found_nums = mailbox.numbers(criteria)
    page_len = 3
    pages = int(len(found_nums) // page_len) + 1 if len(found_nums) % page_len else int(len(found_nums) // page_len)
    for page in range(pages):
        print('page {}'.format(page))
        page_limit = slice(page * page_len, page * page_len + page_len)
        print(page_limit)
        for msg in mailbox.fetch(criteria, bulk=True, limit=page_limit):
            print(' ', msg.date, msg.uid, msg.subject)
