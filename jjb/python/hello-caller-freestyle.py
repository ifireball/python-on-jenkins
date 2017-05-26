#!/usr/bin/env python
from __future__ import print_function
from os import environ

first_name = environ.get('FIRST_NAME', 'small')
last_name = environ.get('LAST_NAME', 'world')
name = ' '.join([first_name, last_name])

with open('job_params.properties', 'w') as f:
    f.write('YOUR_NAME={0}\n'.format(name))
