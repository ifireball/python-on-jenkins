#!/usr/bin/env python
from __future__ import print_function
import operator
from jenkins_objects import object_to_param_str
from os import environ

number = int(environ['NUMBER'])
print("got number: {0}".format(number))
action = (operator.add, number)
print("Created addition action")

with open('job_params.properties', 'w') as f:
    f.write('ACTION={0}\n'.format(object_to_param_str(action)))
