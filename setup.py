#!/usr/bin/python

import sys
from distutils.core import setup
import larvotto


setup(name='Larvotto',
      version=larvotto.__version__,
      url=larvotto.__url__,
      license=larvotto.__license__,
      scripts=['scripts/larvotto.py','scripts/larvotto'],
      author=larvotto.__author__,
	  author_email=larvotto.__contact__,
      packages=['larvotto'])
      
