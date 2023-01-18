#!/usr/bin/python3
"""
Module to custom indentation

errors check and test perform
"""


def text_indentation(text):
    """
    Customs text indentation after ., : and ?
    """
    l = 0
    if not (isinstance(text, str)):
        raise TypeError("text must be a string")
    while (l < len(text)):
        if not (text[l] == '.' or text[l] == ':' or text[l] == '?'):
            print(text[l], end='')
            l += 1
        else:
            print(text[l], end='')
            print('\n')
            l += 1
            while (text[l] == ' '):
                l += 1
            
        
        
        
    