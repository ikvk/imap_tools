# Lib author: Vladimir Kaukin <KaukinVK@ya.ru>
# Project home page: https://github.com/ikvk/imap_tools

from .query import AND, OR, NOT, Header, UidRange, A, O, N, H, U
from .mailbox import BaseMailBox, MailBox, MailBoxUnencrypted
from .message import MailMessage, MailAttachment
from .folder import MailBoxFolderManager
from .consts import MailMessageFlags, MailBoxFolderStatusOptions
from .errors import *

__version__ = '0.46.0'
