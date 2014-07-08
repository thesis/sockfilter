

def raises(f, expected):
    try:
        f()
    except Exception as actual:
        if actual != expected:
            raise
    else:
        assert False, 'Expected: {}'.format(expected)
