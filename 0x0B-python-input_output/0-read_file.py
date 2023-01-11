#!/usr/bin/python3
"""
This module contain file oparations
"""


def read_file(filename=""):
    """
    Function that read a file and print its contains in stdout
    """

    with open(filename, encoding='utf-8') as a_file:
        print(a_file.read(), end='')
