#!/usr/bin/python3
import sys
"""
Exception raising module
"""


def safe_print_integer_err(value):
    """
    Print int safetly
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return False
