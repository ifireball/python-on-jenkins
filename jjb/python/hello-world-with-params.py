#!/usr/bin/env python
from __future__ import print_function
from os import environ

name = environ.get('YOUR_NAME', 'World')
print('Hello {0}!'.format(name))
