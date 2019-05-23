"""
Encode and decode UTF-7 string, as described in the RFC 3501

There are variations, specific to IMAP4rev1, therefore the built-in python UTF-7 codec can't be used.
The main difference is the shift character, used to switch from ASCII to base64 encoding context.
This is "&" in that modified UTF-7 convention, since "+" is considered as mainly used in mailbox names.
Full description in the RFC 3501, section 5.1.3.
"""

import binascii


# ENCODING
# --------
def _modified_base64(s):
    return binascii.b2a_base64(s.encode('utf-16be')).rstrip(b'\n=').replace(b'/', b',')


def _do_b64(_in, r):
    if _in:
        r.append(b'&' + _modified_base64(''.join(_in)) + b'-')
    del _in[:]


def encode(s: str) -> bytes:
    res = []
    _in = []
    for c in s:
        ord_c = ord(c)
        if 0x20 <= ord_c <= 0x25 or 0x27 <= ord_c <= 0x7e:
            _do_b64(_in, res)
            res.append(c.encode())
        elif c == '&':
            _do_b64(_in, res)
            res.append(b'&-')
        else:
            _in.append(c)
    _do_b64(_in, res)
    return b''.join(res)


# DECODING
# --------
def _modified_unbase64(s):
    return binascii.a2b_base64(s.replace(b',', b'/') + b'===').decode('utf-16be')


def decode(s: bytes) -> str:
    res = []
    decode_arr = bytearray()
    for c in s:
        if c == ord('&') and not decode_arr:
            decode_arr.append(ord('&'))
        elif c == ord('-') and decode_arr:
            if len(decode_arr) == 1:
                res.append('&')
            else:
                res.append(_modified_unbase64(decode_arr[1:]))
            decode_arr = bytearray()
        elif decode_arr:
            decode_arr.append(c)
        else:
            res.append(chr(c))
    if decode_arr:
        res.append(_modified_unbase64(decode_arr[1:]))
    return ''.join(res)
