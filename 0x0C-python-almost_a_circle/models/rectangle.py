#!/usr/bin/python3
"""
Module containing Rectangle
"""
from .base import Base


class Rectangle(Base):
    """
    Class Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Validate and Initiate
        """
        super().__init__(id)
        self._validate_integer_input(width, "width")
        self._validate_positive_integer_input(width, "width")
        self.__width = width
        self._validate_integer_input(height, "height")
        self._validate_positive_integer_input(height, "height")
        self.__height = height
        self._validate_integer_input(x, "x")
        self._validate_non_negative_integer_input(x, "x")
        self.__x = x
        self._validate_integer_input(y, "y")
        self._validate_non_negative_integer_input(y, "y")
        self.__y = y

    def _validate_integer_input(self, value, attr_name):
        """
        Is integer
        """
        if type(value) != int:
            raise TypeError(f"{attr_name} must be an integer")

    def _validate_positive_integer_input(self, value, attr_name):
        """
        Is positive (> 0)
        """
        if value <= 0:
            raise ValueError(f"{attr_name} must be > 0")

    def _validate_non_negative_integer_input(self, value, attr_name):
        """
        Is no-negative (>= 0)
        """
        if value < 0:
            raise ValueError(f"{attr_name} must be >= 0")

    def __str__(self):
        """
        Overriding __str__
        """
        str_1 = "{}/{} - ".format(self.__x, self.__y)
        str_2 = "{}/{}".format(self.__width, self.__height)
        return "[Rectangle] ({}) ".format(self.id) + str_1 + str_2

    @property
    def width(self):
        """
        width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        """
        self._validate_integer_input(value, "width")
        self._validate_positive_integer_input(value, "width")
        self.__width = value

    @property
    def height(self):
        """
        height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        """
        self._validate_integer_input(value, "height")
        self._validate_positive_integer_input(value, "height")
        self.__height = value

    @property
    def x(self):
        """
        x getter
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        x setter
        """
        self._validate_integer_input(value, "x")
        self._validate_non_negative_integer_input(value, "x")
        self.__x = value

    @property
    def y(self):
        """
        y getter
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        y setter
        """
        self._validate_integer_input(value, "y")
        self._validate_non_negative_integer_input(value, "y")
        self.__y = value

    def area(self):
        """
        Return area of rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Display rectangle
        """
        for i in range(self.__y):
            print("")
        for i in range(self.__height):
            for j in range(self.__width):
                for k in range(self.__x):
                    if j == 0:
                        print(" ", end='')
                print("#", end='')
            print("")

    def _update_w(self, id, width):
        """update id, w"""
        self.id = id
        self._validate_integer_input(width, "width")
        self._validate_positive_integer_input(width, "width")
        self.__width = width

    def _update_w_h(self, id, width, height):
        """update id, w, h"""
        self._update_w(id, width)
        self._validate_integer_input(height, "height")
        self._validate_positive_integer_input(height, "height")
        self.__height = height

    def _update_w_h_x(self, id, width, height, x):
        """update id, w, h, x"""
        self._update_w_h(id, width, height)
        self._validate_integer_input(x, "x")
        self._validate_non_negative_integer_input(x, "x")
        self.__x = x

    def _update_w_h_x_y(self, id, width, height, x, y):
        """update id, w, h, x, y"""
        self._update_w_h_x(id, width, height, x)
        self._validate_integer_input(y, "y")
        self._validate_non_negative_integer_input(y, "y")
        self.__y = y

    def update(self, *args):
        """
        Update rectangle attrs
        """
        num = len(args)
        if len == 0:
            return
        if num == 1:
            self.id = args[0]
        elif num == 2:
            self._update_w(args[0], args[1])
        elif num == 3:
            self._update_w_h(args[0], args[1], args[2])
        elif num == 4:
            self._update_w_h_x(args[0], args[1], args[2], args[3])
        elif num == 5:
            self._update_w_h_x_y(args[0], args[1], args[2], args[3], args[4])
