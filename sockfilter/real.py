__all__ = ['restore', 'socket', 'socks', 'socket__socket']

import socket

socket__socket = socket.socket

socks__socksocket = None
try:
    import socks
    socks__socksocket = socks.socksocket
except ImportError:
    socks = None

from .util import apply_attr_and_dict


def restore():
    apply_attr_and_dict(socket, 'socket', socket__socket)
    apply_attr_and_dict(socket, 'SocketType', socket__socket)
    apply_attr_and_dict(socket, '_socketobject', socket__socket)
    apply_attr_and_dict(socks, 'socksocket', socks__socksocket)
