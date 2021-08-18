import re

from . import imap_utf7
from .consts import MailBoxFolderStatusOptions
from .utils import check_command_status, pairs_to_dict, encode_folder
from .errors import MailboxFolderStatusValueError, MailboxFolderSelectError, MailboxFolderCreateError, \
    MailboxFolderRenameError, MailboxFolderDeleteError, MailboxFolderStatusError, MailboxFolderSubscribeError


class MailBoxFolderManager:
    """Operations with mail box folders"""

    def __init__(self, mailbox):
        self.mailbox = mailbox
        self._current_folder = None

    def set(self, folder: str or bytes, readonly: bool = False):
        """Select current folder"""
        result = self.mailbox.box.select(encode_folder(folder), readonly)
        check_command_status(result, MailboxFolderSelectError)
        self._current_folder = folder
        return result

    def exists(self, folder: str) -> bool:
        """Checks whether a folder exists on the server."""
        return len(self.list('', folder)) > 0

    def create(self, folder: str or bytes):
        """
        Create folder on the server.
        Use email box delimiter to separate folders. Example for "|" delimiter: "folder|sub folder"
        """
        result = self.mailbox.box._simple_command('CREATE', encode_folder(folder))
        check_command_status(result, MailboxFolderCreateError)
        return result

    def get(self):
        """Get current folder"""
        return self._current_folder

    def rename(self, old_name: str or bytes, new_name: str or bytes):
        """Renemae folder from old_name to new_name"""
        result = self.mailbox.box._simple_command(
            'RENAME', encode_folder(old_name), encode_folder(new_name))
        check_command_status(result, MailboxFolderRenameError)
        return result

    def delete(self, folder: str or bytes):
        """Delete folder"""
        result = self.mailbox.box._simple_command('DELETE', encode_folder(folder))
        check_command_status(result, MailboxFolderDeleteError)
        return result

    def status(self, folder: str or bytes or None = None, options: [str] or None = None) -> dict:
        """
        Get the status of a folder
        :param folder: mailbox folder, current folder if None
        :param options: [str] with values from MailBoxFolderStatusOptions.all | None - for get all options
        :return: dict with available options keys
        """
        command = 'STATUS'
        if folder is None:
            folder = self.get()
        if not options:
            options = tuple(MailBoxFolderStatusOptions.all)
        for opt in options:
            if opt not in MailBoxFolderStatusOptions.all:
                raise MailboxFolderStatusValueError(str(opt))
        status_result = self.mailbox.box._simple_command(
            command, encode_folder(folder), '({})'.format(' '.join(options)))
        check_command_status(status_result, MailboxFolderStatusError)
        result = self.mailbox.box._untagged_response(status_result[0], status_result[1], command)
        check_command_status(result, MailboxFolderStatusError)
        status_data = [i for i in result[1] if type(i) is bytes][0]  # may contain tuples with encoded names
        values = status_data.decode().split('(')[1].split(')')[0].split(' ')
        return {k: int(v) for k, v in pairs_to_dict(values).items() if str(v).isdigit()}

    def list(self, folder: str or bytes = '', search_args: str = '*', subscribed_only: bool = False) -> list:
        """
        Get a listing of folders on the server
        :param folder: mailbox folder, if empty - get from root
        :param search_args: search arguments, is case-sensitive mailbox name with possible wildcards
            * is a wildcard, and matches zero or more characters at this position
            % is similar to * but it does not match a hierarchy delimiter
        :param subscribed_only: bool - get only subscribed folders
        :return: [dict(
            name: str - folder name,
            delim: str - delimiter, a character used to delimit levels of hierarchy in a mailbox name
            flags: tuple(str) - folder flags,
        )]
        A 'NIL' delimiter means that no hierarchy exists, the name is a "flat" name.
        """
        folder_item_re = re.compile(r'\((?P<flags>[\S ]*)\) (?P<delim>[\S]+) (?P<name>.+)')
        command = 'LSUB' if subscribed_only else 'LIST'
        typ, data = self.mailbox.box._simple_command(
            command, encode_folder(folder), encode_folder(search_args))
        typ, data = self.mailbox.box._untagged_response(typ, data, command)
        result = []
        for folder_item in data:
            if not folder_item:
                continue
            if type(folder_item) is bytes:
                folder_match = re.search(folder_item_re, imap_utf7.decode(folder_item))
                if not folder_match:
                    continue
                folder_dict = folder_match.groupdict()
                if folder_dict['name'].startswith('"') and folder_dict['name'].endswith('"'):
                    folder_dict['name'] = folder_dict['name'][1:-1]
            elif type(folder_item) is tuple:
                # when name has " or \ chars
                folder_match = re.search(folder_item_re, imap_utf7.decode(folder_item[0]))
                if not folder_match:
                    continue
                folder_dict = folder_match.groupdict()
                folder_dict['name'] = imap_utf7.decode(folder_item[1])
            else:
                continue
            folder_dict['flags'] = tuple(folder_dict['flags'].split())  # noqa
            folder_dict['delim'] = folder_dict['delim'].replace('"', '')
            result.append(folder_dict)
        return result

    def subscribe(self, folder: str or bytes, value: bool):
        """subscribe/unsubscribe to folder"""
        method = self.mailbox.box.subscribe if value else self.mailbox.box.unsubscribe
        result = method(encode_folder(folder))
        check_command_status(result, MailboxFolderSubscribeError)
        return result
