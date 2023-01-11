#!/usr/bin/python3
"""
This module contain file oparations
"""


def write_file(filename="", text=""):
    """
    Function that write to a file and returns number of charater written
    """

    with open(filename, mode='w', encoding='utf-8') as a_file:
        return a_file.write(text)
