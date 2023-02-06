#!/usr/bin/python3

class P:
    def __init__(self, x):
        self.__x = x
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        if value < 0:
            self.__x = 0
        elif value > 1000:
            self.__x = 1000
        else:
            self.__x = value
p = P(-1001)
print(p.x)