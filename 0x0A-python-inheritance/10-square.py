#!/usr/bin/python3
"""
Module for the class Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """"
    Class Square
    """

    def __init__(self, size):
        """
        Initiation
        """

        self.__size = size
        self.integer_validator("size", self.__size)

    def __str__(self):
        """
        Show information about the rectangle
        """

        return "[Rectangle] {}/{}".format(self.__size, self.__size)

    def area(self):
        """
        Square area implementation
        """

        return self.__size ** 2
        
        
        