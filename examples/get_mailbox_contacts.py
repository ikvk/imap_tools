"""
Collect unique addresses from all folders of the mailbox.
"""
import re
from typing import Dict, Iterable, Optional, Tuple

from imap_tools import BaseMailBox

# Folders we never scan: trash, junk and non-selectable containers.
SKIP_FOLDERS = {'\\Trash', '\\Junk', '\\Noselect', '\\NoSelect'}

# Local parts of system addresses that are not real correspondents.
NOISE_RE = re.compile(
    r'^(no[-_.]?reply|noreply|mailer-daemon|postmaster|donotreply|do-not-reply)@',
    re.IGNORECASE,
)


def collect_contacts(
        mailbox: BaseMailBox,
        *,
        exclude_emails: Optional[Iterable[str]] = None,
        skip_noise: bool = True,
) -> Tuple[Dict[str, str], Dict[str, str], Dict[str, int]]:
    """
    Collect unique addresses from all folders of the mailbox.

    Addresses are split by direction:
        * inbound  - From     (someone wrote to you)
        * outbound - To/Cc/Bcc (you wrote to someone)

    Additionally, a frequency map is built: how many messages
    contained the address in any header (From/To/Cc/Bcc).

    :param mailbox: opened mailbox, will be switched between folders
    :param exclude_emails: addresses to skip (e.g. your own address)
    :param skip_noise: skip noreply / mailer-daemon / postmaster addresses
    :return: (inbound, outbound, frequency)
        inbound   - {email: name}
        outbound  - {email: name}
        frequency - {email: count of messages where the address appeared}
    """
    exclude = {_normalize(e) for e in (exclude_emails or ())}
    inbound: Dict[str, str] = {}
    outbound: Dict[str, str] = {}
    frequency: Dict[str, int] = {}

    # Remember current folder to restore it after scanning.
    previous = mailbox.folder.get()

    try:
        for info in mailbox.folder.list():
            # Skip trash, junk and non-selectable folders.
            if {f for f in info.flags if f} & SKIP_FOLDERS:
                continue

            mailbox.folder.set(info.name)

            # headers_only=True - do not download bodies, only headers.
            # mark_seen=False - do not mark messages as read.
            for msg in mailbox.fetch(headers_only=True, mark_seen=False):
                # Collect all addresses of this message first,
                # so frequency counts each address once per message.
                msg_emails = set()

                # From - inbound correspondent.
                if msg.from_values and msg.from_values.email:
                    email = _add(inbound, msg.from_values, exclude, skip_noise)
                    if email:
                        msg_emails.add(email)

                # To/Cc/Bcc - outbound correspondents.
                for addr in (*msg.to_values, *msg.cc_values, *msg.bcc_values):
                    if addr and addr.email:
                        email = _add(outbound, addr, exclude, skip_noise)
                        if email:
                            msg_emails.add(email)

                # Increment frequency once per message.
                for email in msg_emails:
                    frequency[email] = frequency.get(email, 0) + 1
    finally:
        # Restore folder even if something went wrong.
        if previous is not None:
            mailbox.folder.set(previous)

    return inbound, outbound, frequency


def _normalize(email: str) -> str:
    return (email or '').strip().lower()


def _add(
        contacts: Dict[str, str],
        addr,
        exclude: set,
        skip_noise: bool,
) -> Optional[str]:
    """
    Add an address to the dict, keeping the longest name seen so far.

    :return: normalized email if it was added, None if skipped.
    """
    email = _normalize(addr.email)
    if not email or email in exclude:
        return None
    if skip_noise and NOISE_RE.match(email):
        return None

    # Prefer the longest non-empty name: it usually carries more detail.
    current = contacts.get(email, '')
    if addr.name and len(addr.name) > len(current):
        contacts[email] = addr.name
    elif email not in contacts:
        contacts[email] = addr.name or ''

    return email
