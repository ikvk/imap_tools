"""
Export unique email correspondents (inbound + outbound) from an IMAP mailbox to CSV or JSON.

Configuration (first match wins for each variable):
    * CLI flags
    * Environment variables
    * .env file (see --env-file)

.env keys: IMAP_HOST, IMAP_PORT, IMAP_USER, IMAP_PASSWORD, IMAP_OUTPUT, IMAP_FOLDERS

Example:
    python export_contacts.py --host imap.example.com --user me@example.com --password secret -o contacts.csv
"""
import argparse
import os
import sys

from imap_tools import MailBox
from imap_tools.contacts import collect_contacts, write_contacts_csv, write_contacts_json


def _load_env_file(path: str, override: bool = False) -> None:
    """Load KEY=VALUE lines into os.environ (no external dependencies)."""
    with open(path, encoding='utf-8') as fh:
        for raw_line in fh:
            line = raw_line.strip()
            if not line or line.startswith('#'):
                continue
            if line.startswith('export '):
                line = line[7:].strip()
            key, sep, value = line.partition('=')
            if not sep:
                continue
            key = key.strip()
            value = value.strip()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in '"\'':
                value = value[1:-1]
            if key and (override or key not in os.environ):
                os.environ[key] = value


def _resolve_env_file(explicit: str) -> str:
    if explicit:
        return os.path.normpath(explicit)
    for candidate in (
            os.path.join(os.getcwd(), '.env'),
            os.path.join(os.path.dirname(__file__), '.env'),
            os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '.env')),
    ):
        if os.path.isfile(candidate):
            return candidate
    return ''


def main(argv=None) -> int:
    pre_parser = argparse.ArgumentParser(add_help=False)
    pre_parser.add_argument('--env-file', default='', help='Path to .env (default: auto-detect)')
    pre_args, remaining = pre_parser.parse_known_args(argv)

    env_path = _resolve_env_file(pre_args.env_file)
    if env_path:
        _load_env_file(env_path)

    parser = argparse.ArgumentParser(description='Export IMAP correspondents to a file')
    parser.add_argument('--env-file', default=env_path or '', help='Path to .env file')
    parser.add_argument('--host', default=os.environ.get('IMAP_HOST'), help='IMAP host')
    parser.add_argument(
        '--port',
        type=int,
        default=int(os.environ.get('IMAP_PORT', '993')),
        help='IMAP SSL port (default: 993 or IMAP_PORT)',
    )
    parser.add_argument('--user', default=os.environ.get('IMAP_USER'), help='Login / email')
    parser.add_argument('--password', default=os.environ.get('IMAP_PASSWORD'), help='Password or app token')
    parser.add_argument(
        '-o', '--output',
        default=os.environ.get('IMAP_OUTPUT', 'contacts.csv'),
        help='Output path (.csv or .json)',
    )
    parser.add_argument(
        '--folders',
        default=os.environ.get('IMAP_FOLDERS', ''),
        help='Comma-separated folder names (default: all folders except Trash/Junk)',
    )
    parser.add_argument(
        '--exclude',
        default='',
        help='Comma-separated addresses to skip (defaults include login user if set)',
    )
    parser.add_argument('--no-skip-noise', action='store_true', help='Include noreply / mailer-daemon addresses')
    args = parser.parse_args(remaining)

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
