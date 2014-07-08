__all__ = ['Address']

import collections

Address = collections.namedtuple('Address', ['host', 'port'])
