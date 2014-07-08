from nose.tools import eq_ as equals
import requests

from sockfilter import with_sockfiltering, SockFilterError, Address

from .server import with_server
from .util import raises

HOST = '127.0.0.1'
PORT = 8003
ADDRESS = Address(host=HOST, port=PORT)


def http(host=HOST, port=PORT):
    url = 'http://{}:{}'.format(host, port)
    return requests.get(url).text


def https(host=HOST, port=PORT):
    url = 'https://{}:{}'.format(host, port)
    return requests.get(url, verify=False).text


@with_sockfiltering(lambda x: x.port == PORT)
@with_server(port=PORT)
def test_allow():
    """An allowed HTTP request."""
    equals(http(), 'abc')


@with_sockfiltering(lambda x: x.port == PORT)
@with_server(port=PORT, use_ssl=True)
def test_allow_ssl():
    """An allowed HTTPS request."""
    equals(https(), 'abc')


@with_sockfiltering(lambda x: x.port == PORT + 1)
@with_server(port=PORT)
def test_disallow():
    """A disallowed HTTP request."""
    raises(http, SockFilterError(address=ADDRESS))


@with_sockfiltering(lambda x: x.port == PORT + 1)
@with_server(port=PORT, use_ssl=True)
def test_disallow_ssl():
    """A disallowed HTTPS request."""
    raises(https, SockFilterError(address=ADDRESS))
