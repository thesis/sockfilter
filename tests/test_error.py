from sockfilter import SockFilterError


def test_error_equality():
    assert SockFilterError(address=('google.com', 80)) \
        == SockFilterError(address=('google.com', 80))


def test_error_inequality():
    assert SockFilterError(address=('google.com', 80)) \
        != SockFilterError(address=('google.com', 81))
