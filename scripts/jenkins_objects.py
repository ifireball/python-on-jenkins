#!/usr/bin/env python
"""jenkins_objects.py - Utility functions for handling python object on Jenkins
"""
from __future__ import print_function
from six.moves import cPickle
from base64 import b64decode, b64encode
from bz2 import compress, decompress, BZ2File
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
    fd = None
    try:
        fd = BZ2File(artifact_file)
        return cPickle.loads(fd.read())
    except IOError as e:
        # errno 2 is 'No such file or directory'
        if e.errno == 2 and fallback_cls is not None:
            return fallback_cls()
        raise
    finally:
        if fd is not None:
            fd.close()


def object_to_artifact(obj, artifact_file):
    fd = None
    try:
        fd = BZ2File(artifact_file, 'w')
        fd.write(cPickle.dumps(obj))
    finally:
        if fd is not None:
            fd.close()


@contextmanager
def persist_in_artifacts(artifact_file, fallback_cls=None):
    obj = object_from_artifact(artifact_file, fallback_cls)
    yield obj
    object_to_artifact(obj, artifact_file)
