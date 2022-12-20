#!/usr/bin/python3
"""
This module contain classes definition
"""


class Square:
    """
    Define a Square
    """
    def __init__(self, size=0):
        self.__size = size
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        if (self.__size < 0):
            raise ValueError("size must be >= 0")
    def area(self):
        """
        It return the area of the square

        Returns:
            - int: The area of the square
        """
        return (self.__size * self.__size)
