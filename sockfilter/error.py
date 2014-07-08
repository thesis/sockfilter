__all__ = ['SockFilterError']

import collections


class SockFilterError(Exception):

    Tuple = collections.namedtuple('SockFilterError', ['address'])

    def __init__(self, address):
        self.address = address

    def __repr__(self):
        return repr(self._tuple)

    def __str__(self):
        return str(self._tuple)

    def __unicode__(self):
        return unicode(self._tuple)

    def __eq__(self, other):
        if not hasattr(other, '_tuple'):
            return False
        return self._tuple == other._tuple

    def __ne__(self, other):
        if not hasattr(other, '_tuple'):
            return False
        return self._tuple != other._tuple

    @property
    def _tuple(self):
        return self.Tuple(address=self.address)
