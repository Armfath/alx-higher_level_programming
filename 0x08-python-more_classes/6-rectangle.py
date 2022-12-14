#!/usr/bin/python3
"""
This module contain classes definition
"""


class Rectangle:
    """
    Empty definition of class Rectangle
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if (width < 0):
            raise ValueError("width must be >= 0")
        self.__width = width
        if type(height) != int:
            raise TypeError("height must be an integer")
        if (height < 0):
            raise ValueError("height must be >= 0")
        self.__height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        rectangle = ""
        if (self.__width == 0 or self.__height == 0):
            return (rectangle)
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle += "#"
            rectangle += '\n'
        return (rectangle[:-1])

    def __repr__(self):
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        pr = (self.__width + self.__height) * 2
        return (pr if (self.__width > 0 and self.__height > 0) else 0)
