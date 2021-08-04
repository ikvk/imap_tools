class ImapToolsError(Exception):
    """Base lib error"""


class MailboxFolderStatusValueError(ImapToolsError):
    """Wrong folder status value error"""


class UnexpectedCommandStatusError(ImapToolsError):
    """Unexpected status in IMAP command response"""

    def __init__(self, command_result: tuple, expected: str):
        """
        :param command_result: imap command result
        :param expected: expected command status
        """
        self.command_result = command_result
        self.expected = expected

    def __str__(self):
        return 'Response status "{exp}" expected, but "{typ}" received. Data: {data}'.format(
            exp=self.expected, typ=self.command_result[0], data=str(self.command_result[1]))


class MailboxFolderSelectError(UnexpectedCommandStatusError):
    pass


class MailboxFolderCreateError(UnexpectedCommandStatusError):
    pass


class MailboxFolderRenameError(UnexpectedCommandStatusError):
    pass


class MailboxFolderDeleteError(UnexpectedCommandStatusError):
    pass


class MailboxFolderStatusError(UnexpectedCommandStatusError):
    pass


class MailboxFolderSubscribeError(UnexpectedCommandStatusError):
    pass


class MailboxLoginError(UnexpectedCommandStatusError):
    pass


class MailboxLogoutError(UnexpectedCommandStatusError):
    pass


class MailboxNumbersError(UnexpectedCommandStatusError):
    pass


class MailboxUidsError(UnexpectedCommandStatusError):
    pass


class MailboxStarttlsError(UnexpectedCommandStatusError):
    pass


class MailboxFetchError(UnexpectedCommandStatusError):
    pass


class MailboxExpungeError(UnexpectedCommandStatusError):
    pass


class MailboxDeleteError(UnexpectedCommandStatusError):
    pass


class MailboxCopyError(UnexpectedCommandStatusError):
    pass


class MailboxFlagError(UnexpectedCommandStatusError):
    pass


class MailboxAppendError(UnexpectedCommandStatusError):
    pass
