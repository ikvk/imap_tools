"""
MailBox traffic through proxy servers using https://github.com/Anorov/PySocks
This logic will not be part of imap_tools
"""
import ssl
import socks
from imaplib import IMAP4

from imap_tools import BaseMailBox, MailBoxUnencrypted


class Imap4Proxy(IMAP4):
    def __init__(self,
                 host: str = "",
                 port: int = 143,
                 p_timeout: int = None,
                 p_source_address: tuple = None,
                 p_proxy_type: socks.PROXY_TYPES = socks.HTTP,
                 p_proxy_addr: str = None,
                 p_proxy_port: int = None,
                 p_proxy_rdns=True,
                 p_proxy_username: str = None,
                 p_proxy_password: str = None,
                 p_socket_options: iter = None,
                 ):
        self._host = host
        self._port = port
        self._p_timeout = p_timeout
        self._p_source_address = p_source_address
        self._p_proxy_type = p_proxy_type
        self._p_proxy_addr = p_proxy_addr
        self._p_proxy_port = p_proxy_port
        self._p_proxy_rdns = p_proxy_rdns
        self._p_proxy_username = p_proxy_username
        self._p_proxy_password = p_proxy_password
        self._p_socket_options = p_socket_options
        super().__init__(host, port)

    def _create_socket(self):
        return socks.create_connection(
            dest_pair=(self._host, self._port),
            timeout=self._p_timeout,
            source_address=self._p_source_address,
            proxy_type=self._p_proxy_type,
            proxy_addr=self._p_proxy_addr,
            proxy_port=self._p_proxy_port,
            proxy_rdns=self._p_proxy_rdns,
            proxy_username=self._p_proxy_username,
            proxy_password=self._p_proxy_password,
            socket_options=self._p_socket_options,
        )


class Imap4SslProxy(Imap4Proxy):
    def __init__(self,
                 host: str = "",
                 port: int = 993,
                 keyfile=None,
                 certfile=None,
                 ssl_context=None,
                 p_timeout: int = None,
                 p_source_address: tuple = None,
                 p_proxy_type: socks.PROXY_TYPES = socks.HTTP,
                 p_proxy_addr: str = None,
                 p_proxy_port: int = None,
                 p_proxy_rdns=True,
                 p_proxy_username: str = None,
                 p_proxy_password: str = None,
                 p_socket_options: iter = None,
                 ):
        self._host = host
        self._port = port
        self._p_timeout = p_timeout
        self._p_source_address = p_source_address
        self._p_proxy_type = p_proxy_type
        self._p_proxy_addr = p_proxy_addr
        self._p_proxy_port = p_proxy_port
        self._p_proxy_rdns = p_proxy_rdns
        self._p_proxy_username = p_proxy_username
        self._p_proxy_password = p_proxy_password
        self._p_socket_options = p_socket_options

        if ssl_context is not None and keyfile is not None:
            raise ValueError("ssl_context and keyfile arguments are mutually exclusive")
        if ssl_context is not None and certfile is not None:
            raise ValueError("ssl_context and certfile arguments are mutually exclusive")
        if keyfile is not None or certfile is not None:
            import warnings
            warnings.warn("keyfile and certfile are deprecated, use ssl_context instead", DeprecationWarning, 2)

        if ssl_context is None:
            ssl_context = ssl._create_stdlib_context(certfile=certfile, keyfile=keyfile)  # noqa

        self.keyfile = keyfile
        self.certfile = certfile
        self.ssl_context = ssl_context

        super().__init__(host, port, p_timeout, p_source_address, p_proxy_type, p_proxy_addr, p_proxy_port,
                         p_proxy_rdns, p_proxy_username, p_proxy_password, p_socket_options)

    def _create_socket(self):
        sock = super()._create_socket()
        server_hostname = self.host if ssl.HAS_SNI else None
        return self.ssl_context.wrap_socket(sock, server_hostname=server_hostname)

    def open(self, host='', port=993):
        super().open(host, port)


class MailBoxUnencryptedProxy(MailBoxUnencrypted):
    """Working with the email box through IMAP4 through proxy"""

    def __init__(self,
                 host: str = "",
                 port: int = 143,
                 p_timeout: int = None,
                 p_source_address: tuple = None,
                 p_proxy_type: socks.PROXY_TYPES = socks.HTTP,
                 p_proxy_addr: str = None,
                 p_proxy_port: int = None,
                 p_proxy_rdns=True,
                 p_proxy_username: str = None,
                 p_proxy_password: str = None,
                 p_socket_options: iter = None,
                 ):
        self._host = host
        self._port = port
        self._p_timeout = p_timeout
        self._p_source_address = p_source_address
        self._p_proxy_type = p_proxy_type
        self._p_proxy_addr = p_proxy_addr
        self._p_proxy_port = p_proxy_port
        self._p_proxy_rdns = p_proxy_rdns
        self._p_proxy_username = p_proxy_username
        self._p_proxy_password = p_proxy_password
        self._p_socket_options = p_socket_options
        super().__init__()

    def _get_mailbox_client(self):
        return Imap4Proxy(
            self._host, self._port,
            self._p_timeout, self._p_source_address, self._p_proxy_type, self._p_proxy_addr, self._p_proxy_port,
            self._p_proxy_rdns, self._p_proxy_username, self._p_proxy_password, self._p_socket_options)


class MailBoxProxy(BaseMailBox):
    """Working with the email box through IMAP4 over SSL connection through proxy"""

    def __init__(self,
                 host: str = "",
                 port: int = 993,
                 keyfile=None,
                 certfile=None,
                 ssl_context=None,
                 p_timeout: int = None,
                 p_source_address: tuple = None,
                 p_proxy_type: socks.PROXY_TYPES = socks.HTTP,
                 p_proxy_addr: str = None,
                 p_proxy_port: int = None,
                 p_proxy_rdns=True,
                 p_proxy_username: str = None,
                 p_proxy_password: str = None,
                 p_socket_options: iter = None,
                 ):
        self._host = host
        self._port = port
        self._keyfile = keyfile
        self._certfile = certfile
        self._ssl_context = ssl_context
        self._p_timeout = p_timeout
        self._p_source_address = p_source_address
        self._p_proxy_type = p_proxy_type
        self._p_proxy_addr = p_proxy_addr
        self._p_proxy_port = p_proxy_port
        self._p_proxy_rdns = p_proxy_rdns
        self._p_proxy_username = p_proxy_username
        self._p_proxy_password = p_proxy_password
        self._p_socket_options = p_socket_options
        super().__init__()

    def _get_mailbox_client(self):
        return Imap4SslProxy(
            self._host, self._port, self._keyfile, self._certfile, self._ssl_context,
            self._p_timeout, self._p_source_address, self._p_proxy_type, self._p_proxy_addr, self._p_proxy_port,
            self._p_proxy_rdns, self._p_proxy_username, self._p_proxy_password, self._p_socket_options)


if __name__ == '__main__':
    with MailBoxProxy(p_proxy_type=socks.HTTP,
                      p_proxy_addr='1.2.3.4',  # zproxy.lum-superproxy.io
                      p_proxy_port=3192,  # 22225
                      p_proxy_username='proxy_username',
                      p_proxy_password='proxy_pwd_123',
                      p_timeout=10,
                      host='imap.host.com').login('mail.user', 'mail_pwd_123', 'INBOX') as mailbox:
        for msg in mailbox.fetch():
            print(msg.subject, msg.date_str)
