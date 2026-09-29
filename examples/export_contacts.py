"""
Export unique email correspondents (inbound + outbound) from an IMAP mailbox to CSV or JSON.

Environment variables (optional): IMAP_HOST, IMAP_USER, IMAP_PASSWORD, IMAP_OUTPUT

Example:
    python export_contacts.py --host imap.example.com --user me@example.com --password secret -o contacts.csv
"""
import argparse
import os
import sys

from imap_tools import MailBox
from imap_tools.contacts import collect_contacts, write_contacts_csv, write_contacts_json


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description='Export IMAP correspondents to a file')
    parser.add_argument('--host', default=os.environ.get('IMAP_HOST'), help='IMAP host')
    parser.add_argument('--port', type=int, default=993, help='IMAP SSL port (default: 993)')
    parser.add_argument('--user', default=os.environ.get('IMAP_USER'), help='Login / email')
    parser.add_argument('--password', default=os.environ.get('IMAP_PASSWORD'), help='Password or app token')
    parser.add_argument(
        '-o', '--output',
        default=os.environ.get('IMAP_OUTPUT', 'contacts.csv'),
        help='Output path (.csv or .json)',
    )
    parser.add_argument(
        '--folders',
        default='',
        help='Comma-separated folder names (default: all folders except Trash/Junk)',
    )
    parser.add_argument(
        '--exclude',
        default='',
        help='Comma-separated addresses to skip (defaults include login user if set)',
    )
    parser.add_argument('--no-skip-noise', action='store_true', help='Include noreply / mailer-daemon addresses')
    args = parser.parse_args(argv)

    if not args.host or not args.user or not args.password:
        parser.error('--host, --user, and --password are required (or set IMAP_* env vars)')

    exclude = [e.strip() for e in args.exclude.split(',') if e.strip()]
    if args.user and args.user not in exclude:
        exclude.append(args.user)

    folders = None
    if args.folders.strip():
        folders = [f.strip() for f in args.folders.split(',') if f.strip()]

    with MailBox(args.host, port=args.port).login(args.user, args.password) as mailbox:
        contacts = collect_contacts(
            mailbox,
            folders=folders,
            exclude_emails=exclude,
            headers_only=True,
            mark_seen=False,
            skip_noise=not args.no_skip_noise,
        )

    output = args.output.lower()
    if output.endswith('.json'):
        write_contacts_json(args.output, contacts)
    else:
        write_contacts_csv(args.output, contacts)

    print(f'Wrote {len(contacts)} unique addresses to {args.output}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
