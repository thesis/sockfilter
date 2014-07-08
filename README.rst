sockfilter
==========

Block socket creation based on hostname/port to suppress unwanted
network activity.

.. pypi - Everything below this line goes into the description for PyPI.


Usage
-----

The intended use is for making sure your unit tests don't make network
connections. Activate `sockfilter` with a predicate like:

.. code:: python
    # only allow http connections to localhost
    def socket_address_allowed(address):
        return (address.host in ['localhost', '127.0.0.1'] and
                address.port == 80)

    sockfilter.enable(socket_address_allowed)

Any subsequent attempts to open a connection at an address not satisfying
the predicate will raise `sockfilter.SockFilterError`.


`with_sockfiltering` decorator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    from sockfilter import with_sockfiltering

    @with_sockfiltering(socket_address_allowed)
    def test_foo():
        foo()


`sockfiltering` context manager
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    from sockfilter import sockfiltering

    def test_foo():
        with sockfiltering(socket_address_allowed):
            foo()


`enable` and `disable`
~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    import sockfilter
    from unittest import TestCase

    class FooTest(TestCase):

        def setUp(self):
            sockfilter.enable(socket_address_allowed)

        def tearDown(self):
            sockfilter.disable()

        def test_foo(self):
            foo()


Under the hood
--------------

Sockfilter works by monkey-patching Python's `socket` library,
inspired by HTTPretty_.

.. _HTTPretty: https://github.com/gabrielfalcao/HTTPretty
