import re

from . import imap_utf7
from .utils import check_command_status, quote, pairs_to_dict


class MailBoxFolderWrongStatusError(Exception):
    """Wrong folder status error"""


class MailBoxFolderManager:
    """Operations with mail box folders"""

    folder_status_options = ('MESSAGES', 'RECENT', 'UIDNEXT', 'UIDVALIDITY', 'UNSEEN')

    def __init__(self, mailbox):
        self.mailbox = mailbox
        self._current_folder = None

    @staticmethod
    def _encode_folder(folder: str or bytes) -> bytes:
        """Encode folder name"""
        if isinstance(folder, bytes):
            return quote(folder)
        else:
            return quote(imap_utf7.encode(folder))

    def set(self, folder: str or bytes):
        """Select current folder"""
        result = self.mailbox.box.select(self._encode_folder(folder))
        check_command_status('box.select', result)
        self._current_folder = folder
        return result

    def exists(self, folder: str) -> bool:
        """Checks whether a folder exists on the server."""
        return len(self.list('', folder)) > 0

    def create(self, folder: str or bytes):
        """
        Create folder on the server. D
        *Use email box delimitor to separate folders. Example for "|" delimitor: "folder|sub folder"
        """
        result = self.mailbox.box._simple_command('CREATE', self._encode_folder(folder))
        check_command_status('CREATE', result)
        return result

    def get(self):
        """Get current folder"""
        return self._current_folder

    def rename(self, old_name: str or bytes, new_name: str or bytes):
        """Renemae folder from old_name to new_name"""
        result = self.mailbox.box._simple_command(
            'RENAME', self._encode_folder(old_name), self._encode_folder(new_name))
        check_command_status('RENAME', result)
        return result

    def delete(self, folder: str or bytes):
        """Delete folder"""
        result = self.mailbox.box._simple_command('DELETE', self._encode_folder(folder))
        check_command_status('DELETE', result)
        return result

    def status(self, folder: str or bytes, options: [str] or None = None) -> dict:
        """
        Get the status of a folder
        :param folder: mailbox folder
        :param options: [str] with values from MailBoxFolderManager.folder_status_options or None,
                by default - get all options
            MESSAGES - The number of messages in the mailbox.
            RECENT - The number of messages with the Recent flag set.
            UIDNEXT - The next unique identifier value of the mailbox.
            UIDVALIDITY - The unique identifier validity value of the mailbox.
            UNSEEN - The number of messages which do not have the Seen flag set.
        :return: dict with available options keys
        """
        command = 'STATUS'
        if not options:
            options = self.folder_status_options
        if not all((i in self.folder_status_options for i in options)):
            raise MailBoxFolderWrongStatusError(str(options))
        status_result = self.mailbox.box._simple_command(
            command, self._encode_folder(folder), '({})'.format(' '.join(options)))
        check_command_status(command, status_result)
        result = self.mailbox.box._untagged_response(status_result[0], status_result[1], command)
        check_command_status(command, result)
        values = result[1][0].decode().split('(')[1].split(')')[0].split(' ')
        return {k: int(v) for k, v in pairs_to_dict(values).items() if str(v).isdigit()}

    def list(self, folder: str or bytes = '', search_args: str = '*', subscribed_only: bool = False) -> list:
        """
        Get a listing of folders on the server
        :param folder: mailbox folder, if empty list shows all content from root
        :param search_args: search argumets, is case-sensitive mailbox name with possible wildcards
            * is a wildcard, and matches zero or more characters at this position
            % is similar to * but it does not match a hierarchy delimiter
        :param subscribed_only: bool - get only subscribed folders
        :return: [dict(
            flags: str - folder flags,
            delim: str - delimitor,
            name: str - folder name,
        )]
        """
        folder_item_re = re.compile(r'\((?P<flags>[\S ]*)\) "(?P<delim>[\S ]+)" (?P<name>.+)')
        command = 'LSUB' if subscribed_only else 'LIST'
        typ, data = self.mailbox.box._simple_command(command, self._encode_folder(folder), search_args)
        typ, data = self.mailbox.box._untagged_response(typ, data, command)
        result = list()
        for folder_item in data:
            if not folder_item:
                continue
            folder_match = re.search(folder_item_re, imap_utf7.decode(folder_item))
            folder = folder_match.groupdict()
            if folder['name'].startswith('"') and folder['name'].endswith('"'):
                folder['name'] = folder['name'][1:len(folder['name']) - 1]
            result.append(folder)
        return result
