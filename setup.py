#!/usr/bin/env python
#
# Usage: python setup.py install
#

from setuptools import setup, find_packages

__version__ = '0.1'

def _read(doc):
    return open(doc, 'rb').read()

setup(name='dipp.awstats',
      version=__version__,
      description="AWStats wrapper",
      long_description=_read('README.md').decode('utf-8'),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Peter Reimer',
      author_email='reimer@hbz-nrw.de',
      url='',
      license='DFSL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['dipp', 'dipp.awstats'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'bda.awstatsparser'
          # -*- Extra requirements: -*-
      ],
     )
