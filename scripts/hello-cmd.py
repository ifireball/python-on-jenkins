#!/usr/bin/env python
"""hello-cmd.py - Command to say Hello
"""
from __future__ import print_function
import argparse


def main():
    args = parse_args()
    print("Hello {}".format(args.who))


def parse_args():
    """Parse command line arguments
    """
    parser = argparse.ArgumentParser(
        description='Tool that says hello'
    )
    parser.add_argument(
        'who', default='world', nargs='?'
    )
    return parser.parse_args()


if __name__ == '__main__':
    exit(main())
