#!/usr/bin/python3
"""
This module contain classes definition
"""


class Square:
    """
    Define a Square
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
    
    def size(self):
        """
        size getter
        """
        return self.__size
    
    def size(self, value):
        """
        size setter
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        It return the area of the square

        Returns:
            - int: The area of the square
        """

        return (self.__size ** 2)
