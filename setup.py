from setuptools import setup
from os import path
import re


def packagefile(*relpath):
    return path.join(path.dirname(__file__), *relpath)


def read(*relpath):
    with open(packagefile(*relpath)) as f:
        return f.read()


def get_version(*relpath):
    match = re.search(
        r'''^__version__ = ['"]([^'"]*)['"]''',
        read(*relpath),
        re.M
    )
    if not match:
        raise RuntimeError('Unable to find version string.')
    return match.group(1)


setup(
    name='get_firefox_urls',
    version=get_version('get_firefox_urls.py'),
    description='Utility to print the URLs currently open in Firefox.',
    long_description=read('README.rst'),
    url='https://github.com/luismsgomes/get-firefox-urls',
    author='Luís Gomes',
    author_email='luismsgomes@gmail.com',
    license='MIT',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='firefox util commandline',
    install_requires=['lz4'],
    py_modules=['get_firefox_urls'],
    entry_points={
        'console_scripts': [
            'get-firefox-urls=get_firefox_urls:main',
        ],
    },
)
