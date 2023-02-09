#!/usr/bin/env python3
"""
Module containing Rectangle
"""
from .base import Base


class Rectangle(Base):
    """
    Class Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self._y = y

    @property
    def width(self):
        """
        width getter
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        width setter
        """
        self.__width = value

    @property
    def height(self):
        """
        height getter
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        width setter
        """
        self.__height = value

    @property
    def x(self):
        """
        x getter
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """
        x setter
        """
        self.__x = value

    @property
    def y(self):
        """
        y getter
        """
        return (self.__y)

    @y.setter
    def y(self, value):
        """
        width setter
        """
        self.__y = value