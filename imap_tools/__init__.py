# Lib author: Vladimir Kaukin <KaukinVK@ya.ru>
# Project home page: https://github.com/ikvk/imap_tools
# Mirror: https://gitflic.ru/project/ikvk/imap-tools
# License: Apache-2.0

from .query import AND, OR, NOT, Header, UidRange, A, O, N, H, U
from .mailbox import BaseMailBox, MailBox, MailBoxUnencrypted, MailBoxTls
from .message import MailMessage, MailAttachment
from .folder import MailBoxFolderManager, FolderInfo
from .consts import MailMessageFlags, MailBoxFolderStatusOptions, SortCriteria
from .utils import EmailAddress
from .errors import *

__version__ = '1.7.2'
