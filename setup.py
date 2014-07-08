from setuptools import setup


def long_description():
    from os.path import join, dirname
    import re
    text = open(join(dirname(__file__), 'README.rst')).read()
    return re.split('\n\.\. pypi [^\n]*\n', text, 1)[1]


def test_requirements():
    from os.path import join, dirname
    return open(join(dirname(__file__), 'test_requirements.txt')).readlines()


setup(
    name='sockfilter',
    version='1.1',
    py_modules=['sockfilter'],
    description='Block socket creation by host/port.',
    long_description=long_description(),
    author='Chris Martin',
    author_email='ch.martin@gmail.com',
    url='https://github.com/cardforcoin/sockfilter',
    license='MIT',
    tests_require=test_requirements(),
    test_suite='nose.collector',
)
