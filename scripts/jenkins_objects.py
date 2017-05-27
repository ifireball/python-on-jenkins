#!/usr/bin/env python
"""jenkins_objects.py - Utility functions for handling python object on Jenkins
"""
from __future__ import print_function
from six.moves import cPickle
from base64 import b64decode, b64encode
from bz2 import compress, decompress
from contextlib import contextmanager


def param_str_to_object(param_str):
    """Convert a string that came from a job parameter into an object
    """
    return cPickle.loads(decompress(b64decode(param_str.encode('utf8'))))


def object_to_param_str(obj):
    """Convert an object into a format suitable for passing in job parameters
    """
    return b64encode(compress(cPickle.dumps(obj))).decode('utf8')


def object_from_artifact(artifact_file, fallback_cls=None):
    try:
        with open(artifact_file) as fd:
            return cPickle.load(fd)
    except IOError as e:
        # errno 2 is 'No such file or directory'
        if e.errno == 2 and fallback_cls is not None:
            return fallback_cls()
        raise


def object_to_artifact(obj, artifact_file):
    with open(artifact_file, 'w') as fd:
        cPickle.dump(obj, fd)


@contextmanager
def persist_in_artifacts(artifact_file, fallback_cls=None):
    obj = object_from_artifact(artifact_file, fallback_cls)
    yield obj
    object_to_artifact(obj, artifact_file)
