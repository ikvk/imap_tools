import time
from imap_tools import MailBox, A

# 1
# SIMPLE
# waiting for msg in 60 sec, then print unseen if any update
with MailBox('imap.far.mars').login('acc', 'pwd') as mailbox:
    # in idle mode
    mailbox.idle.start()
    responses = mailbox.idle.poll(timeout=60)
    mailbox.idle.stop()
    # in not idle mode
    if responses:
        for msg in mailbox.fetch(A(seen=False)):
            print(msg.date, msg.subject)
    else:
        print('no any updates')

# 2
# reliable console notificator
# *some mail servers do not like multiple connections, you may close web mailbox interface for reduce connection errors
import time, socket, imaplib, traceback
from imap_tools import A, MailBox, MailboxLoginError, MailboxLogoutError

done = False
while not done:
    connection_start_time = time.monotonic()
    connection_live_time = 0.0
    try:
        with MailBox('imap.my.moon').login('acc', 'pwd', 'INBOX') as mailbox:
            print('@@ new connection', time.asctime())
            while connection_live_time < 29 * 60:
                try:
                    responses = mailbox.idle.wait(timeout=3 * 60)
                    print(time.asctime(), 'IDLE responses:', responses)
                    if responses:
                        for msg in mailbox.fetch(A(seen=False)):
                            print('->', msg.date, msg.subject)
                except KeyboardInterrupt:
                    print('~KeyboardInterrupt')
                    done = True
                    break
                connection_live_time = time.monotonic() - connection_start_time
    except (TimeoutError, ConnectionError,
            imaplib.IMAP4.abort, MailboxLoginError, MailboxLogoutError,
            socket.herror, socket.gaierror, socket.timeout) as e:
        print(f'## Error\n{e}\n{traceback.format_exc()}\nreconnect in a minute...')
        time.sleep(60)

# 3
# context manager
from imap_tools import MailBox, A

with MailBox('imap.sun.mw').login('acc', 'pwd', 'INBOX') as mailbox:
    with mailbox.idle as idle:
        responses = idle.poll(timeout=10)
    if responses:
        for msg in mailbox.fetch(A(seen=False)):
            print(msg.date, msg.subject)
    else:
        print('no any updates')
