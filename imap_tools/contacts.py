import csv
import json
import re
from datetime import datetime
from typing import Dict, Iterable, List, Optional, Set, Tuple, Union

from .folder import FolderInfo
from .mailbox import BaseMailBox
from .message import MailMessage
from .utils import EmailAddress

# RFC 6154 special-use flags (IMAP may return with or without leading backslash in parsed form)
_FOLDER_FLAG_SKIP = frozenset({'\\Trash', '\\Junk', '\\Noselect', '\\NoSelect'})
_FOLDER_FLAG_SENT = frozenset({'\\Sent'})
_FOLDER_FLAG_DRAFTS = frozenset({'\\Drafts'})
_FOLDER_FLAG_INBOX = frozenset({'\\Inbox'})

_NOISE_LOCAL_PART_RE = re.compile(
    r'^(no[-_.]?reply|noreply|mailer-daemon|postmaster|donotreply|do-not-reply)(@|$)',
    re.IGNORECASE,
)


class ContactInfo:
    """Aggregated correspondent data collected from message headers."""

    __slots__ = 'email', 'name', 'inbound_count', 'outbound_count', 'folders', 'first_seen', 'last_seen'

    def __init__(self, email: str, name: str = '') -> None:
        self.email = email
        self.name = name
        self.inbound_count = 0
        self.outbound_count = 0
        self.folders: Set[str] = set()
        self.first_seen: Optional[datetime] = None
        self.last_seen: Optional[datetime] = None

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(email={repr(self.email)}, name={repr(self.name)}, "
            f"inbound_count={self.inbound_count}, outbound_count={self.outbound_count})"
        )


def normalize_email(email: str) -> str:
    return (email or '').strip().lower()


def _flag_set(folder: FolderInfo) -> Set[str]:
    return {f for f in folder.flags if f}


def folder_scan_mode(folder: FolderInfo) -> str:
    """
    How to interpret addresses in a folder.
    :return: 'inbound' | 'outbound' | 'both'
    """
    flags = _flag_set(folder)
    if flags & _FOLDER_FLAG_SENT or flags & _FOLDER_FLAG_DRAFTS:
        return 'outbound'
    if flags & _FOLDER_FLAG_INBOX or folder.name.upper() == 'INBOX':
        return 'inbound'
    return 'both'


def resolve_export_folders(
        mailbox: BaseMailBox,
        folders: Optional[Union[str, Iterable[str]]] = None,
        *,
        skip_special_trash_junk: bool = True,
) -> List[str]:
    """
    Resolve folder names to scan.
    :param folders: None — all folders except trash/junk/noselect; 'auto' — same; str — single folder;
        iterable — explicit list
    """
    if folders is None or folders == 'auto':
        result = []
        for info in mailbox.folder.list():
            if skip_special_trash_junk and _flag_set(info) & _FOLDER_FLAG_SKIP:
                continue
            result.append(info.name)
        return result
    if isinstance(folders, str):
        return [folders]
    return list(folders)


def _is_noise_address(email: str) -> bool:
    if '@' not in email:
        return True
    local = email.split('@', 1)[0]
    return bool(_NOISE_LOCAL_PART_RE.match(local))


def _pick_name(current: str, new: str) -> str:
    if new and (not current or len(new) > len(current)):
        return new
    return current


def _touch_dates(contact: ContactInfo, msg_date: datetime) -> None:
    if contact.first_seen is None or msg_date < contact.first_seen:
        contact.first_seen = msg_date
    if contact.last_seen is None or msg_date > contact.last_seen:
        contact.last_seen = msg_date


def _register(
        contacts: Dict[str, ContactInfo],
        addr: EmailAddress,
        direction: str,
        folder_name: str,
        msg_date: datetime,
        exclude: Set[str],
        skip_noise: bool,
) -> None:
    email = normalize_email(addr.email)
    if not email or email in exclude:
        return
    if skip_noise and _is_noise_address(email):
        return
    contact = contacts.get(email)
    if contact is None:
        contact = ContactInfo(email=email, name=addr.name or '')
        contacts[email] = contact
    else:
        contact.name = _pick_name(contact.name, addr.name or '')
    contact.folders.add(folder_name)
    _touch_dates(contact, msg_date)
    if direction == 'inbound':
        contact.inbound_count += 1
    else:
        contact.outbound_count += 1


def iter_correspondents_from_message(
        msg: MailMessage,
        folder_name: str,
        mode: str,
) -> Iterable[Tuple[str, EmailAddress]]:
    """Yield (direction, EmailAddress) pairs from a single message."""
    if mode in ('inbound', 'both'):
        if msg.from_values and msg.from_values.email:
            yield 'inbound', msg.from_values
    if mode in ('outbound', 'both'):
        for addr in msg.to_values:
            if addr.email:
                yield 'outbound', addr
        for addr in msg.cc_values:
            if addr.email:
                yield 'outbound', addr
        for addr in msg.bcc_values:
            if addr.email:
                yield 'outbound', addr


def collect_from_message(
        contacts: Dict[str, ContactInfo],
        msg: MailMessage,
        folder_name: str,
        mode: str,
        exclude: Set[str],
        skip_noise: bool,
) -> None:
    msg_date = msg.date
    for direction, addr in iter_correspondents_from_message(msg, folder_name, mode):
        _register(contacts, addr, direction, folder_name, msg_date, exclude, skip_noise)


def collect_contacts(
        mailbox: BaseMailBox,
        folders: Optional[Union[str, Iterable[str]]] = None,
        *,
        exclude_emails: Optional[Iterable[str]] = None,
        criteria: str = 'ALL',
        charset: str = 'US-ASCII',
        headers_only: bool = True,
        mark_seen: bool = False,
        limit: Optional[Union[int, slice]] = None,
        bulk: Union[bool, int] = False,
        skip_noise: bool = True,
        folder_modes: Optional[Dict[str, str]] = None,
) -> Dict[str, ContactInfo]:
    """
    Scan IMAP folders and aggregate unique correspondent addresses.

    Uses From for inbound-style folders, To/Cc/Bcc for sent/drafts, both for other folders.
    Override per-folder behavior with folder_modes: folder name -> 'inbound' | 'outbound' | 'both'.
    """
    exclude = {normalize_email(e) for e in (exclude_emails or ())}
    folder_name_list = resolve_export_folders(mailbox, folders)
    folder_infos = {i.name: i for i in mailbox.folder.list()}
    contacts: Dict[str, ContactInfo] = {}
    previous_folder = mailbox.folder.get()

    try:
        for folder_name in folder_name_list:
            info = folder_infos.get(folder_name)
            if folder_modes and folder_name in folder_modes:
                mode = folder_modes[folder_name]
            elif info is not None:
                mode = folder_scan_mode(info)
            else:
                mode = 'both'
            mailbox.folder.set(folder_name)
            for msg in mailbox.fetch(
                    criteria,
                    charset,
                    limit=limit,
                    mark_seen=mark_seen,
                    headers_only=headers_only,
                    bulk=bulk,
            ):
                collect_from_message(contacts, msg, folder_name, mode, exclude, skip_noise)
    finally:
        if previous_folder is not None:
            mailbox.folder.set(previous_folder)

    return contacts


def write_contacts_csv(path: str, contacts: Dict[str, ContactInfo], *, encoding: str = 'utf-8') -> None:
    """Write contacts sorted by email to a CSV file."""
    fieldnames = [
        'email', 'name', 'inbound_count', 'outbound_count', 'folders', 'first_seen', 'last_seen',
    ]
    rows = sorted(contacts.values(), key=lambda c: c.email)
    with open(path, 'w', encoding=encoding, newline='') as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for contact in rows:
            writer.writerow({
                'email': contact.email,
                'name': contact.name,
                'inbound_count': contact.inbound_count,
                'outbound_count': contact.outbound_count,
                'folders': ';'.join(sorted(contact.folders)),
                'first_seen': contact.first_seen.isoformat() if contact.first_seen else '',
                'last_seen': contact.last_seen.isoformat() if contact.last_seen else '',
            })


def write_contacts_json(path: str, contacts: Dict[str, ContactInfo], *, encoding: str = 'utf-8') -> None:
    """Write contacts as a JSON array sorted by email."""
    payload = []
    for contact in sorted(contacts.values(), key=lambda c: c.email):
        payload.append({
            'email': contact.email,
            'name': contact.name,
            'inbound_count': contact.inbound_count,
            'outbound_count': contact.outbound_count,
            'folders': sorted(contact.folders),
            'first_seen': contact.first_seen.isoformat() if contact.first_seen else None,
            'last_seen': contact.last_seen.isoformat() if contact.last_seen else None,
        })
    with open(path, 'w', encoding=encoding) as fh:
        json.dump(payload, fh, indent=2, ensure_ascii=False)
        fh.write('\n')
