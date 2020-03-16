#! /usr/bin/env python
"""
    Super-fast, efficiently stored Trie for Python.
    Depends on (and tested with) libdatrie 0.2.12
    https://github.com/tlwg/libdatrie/releases
"""

import glob
import os

from setuptools import setup, Extension

__version__ = '0.8.1'

# make setuptools happy with PEP 440-compliant post version
# (enable this for patch releases)
# REL_TAG = __version__.replace('-', 'p')

DATRIE_DOWNLOAD_URL = (
    'https://github.com/freepn/datrie/tarball/' + __version__
)

DESCRIPTION = __doc__
LONG_DESCRIPTION = open('README.rst').read() + open('CHANGES.rst').read()
LICENSE = 'LGPLv2+'

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
    'Programming Language :: Cython',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: Implementation :: CPython',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Scientific/Engineering :: Information Analysis',
    'Topic :: Text Processing :: Linguistic'
]


setup(name="datrie",
      version=__version__,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      url='https://github.com/pytries/datrie',
      author='Mikhail Korobov',
      author_email='kmike84@gmail.com',
      license=LICENSE,
      download_url=DATRIE_DOWNLOAD_URL,
      classifiers=CLASSIFIERS,
      ext_modules=[
          Extension("datrie", [
              'src/datrie.c',
              'src/cdatrie.c',
              'src/stdio_ext.c'
          ], libraries=['datrie'],
          include_dirs=['/usr/include/datrie'])
      ],

      tests_require=["pytest", "hypothesis"])
