__all__ = [
    'Address', 'SockFilterError', 'enable', 'disable', 'is_enabled',
    'sockfiltering', 'with_sockfiltering'
]

from contextlib import contextmanager
import functools

from .address import Address
from .error import SockFilterError
from . import real, fake


def is_enabled():
    return fake.instance is not None


def enable(predicate):
    if is_enabled():
        disable()
    fake.instance = fake.Fake(predicate)
    fake.instance.apply()


def disable():
    if not is_enabled():
        return
    real.restore()
    fake.instance = None


@contextmanager
def sockfiltering(*args, **kwargs):
    try:
        enable(*args, **kwargs)
        yield
    finally:
        disable()


def with_sockfiltering(*args, **kwargs):
    def decorate(f):
        @functools.wraps(f)
        def wrapped(*wrapped_args, **wrapped_kwargs):
            with sockfiltering(*args, **kwargs):
                return f(*wrapped_args, **wrapped_kwargs)
        return wrapped
    return decorate
