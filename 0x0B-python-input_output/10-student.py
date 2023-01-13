#!/usr/bin/python3
""" Student module
"""


class Student:
    """ The class Student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        list = {}
        for attr in attrs:
            if attr in self.__dict__:
                list[attr] = self.__dict__[attr]
        return list
