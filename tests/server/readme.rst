A very simple HTTP server for testing.

SSL
---

No, `key.pem` is not a "real" key.
These keypairs were generated exclusively for testing.

.. code:: bash
    openssl req          \
        -x509            \
        -newkey rsa:2048 \
        -keyout key.pem  \
        -out cert.pem    \
        -days XXX        \
        -nodes
