#!/usr/bin/env python
"""calculator_processor.py - This code is invoked by the calculator-processor
                             pipeline
"""
from __future__ import print_function
from jenkins_objects import param_str_to_object, persist_in_artifacts
from os import environ


class CalculatorStatus(object):
    def __init__(self):
        self.current_value = 0


status_file = environ['CALCULATOR_STATUS']
action = param_str_to_object(environ['ACTION'])

with persist_in_artifacts(status_file, CalculatorStatus) as status:
    status.current_value = action[0](status.current_value, action[1])

print("Calculator result is: {0}".format(status.current_value))
