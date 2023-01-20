#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
Class rectangle
"""


class Rectangle(BaseGeometry):
    """
    Rectangle implamatation
    """
    def __init__(self, width, height):
        """
        Initiation and validdation
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
