#!/usr/bin/python3
"""
Module to custom indentation

errors check and test perform
"""


def text_indentation(text):
    """
    Customs text indentation after ., : and ?
    """
    size = 0
    if not (isinstance(text, str)):
        raise TypeError("text must be a string")
    while (size < len(text)):
        if not (text[size] == '.' or text[size] == ':' or text[size] == '?'):
            print(text[size], end='')
            size += 1
        else:
            print(text[size], end='')
            print('\n')
            size += 1
            while (text[size] == ' '):
                size += 1
