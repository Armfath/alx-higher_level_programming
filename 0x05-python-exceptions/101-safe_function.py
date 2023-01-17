#!/usr/bin/python3
import sys
"""
Exception raising module
"""


def safe_function(fct, *args):
    """
    Execute a funct safetly
    """
    try:
        return fct(args[0], args[1])
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return None
