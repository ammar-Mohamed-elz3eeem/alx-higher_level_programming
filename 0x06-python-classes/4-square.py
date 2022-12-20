#!/usr/bin/python3
"""
Define Square Class with private attribute size
with some verfications that size attribute is correct
"""


class Square:
    """ Square Class is used to create
    squares with size == self.size """

    def __init__(self, s=0):
        self.size = s

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if (value < 0):
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    """Function to get area of Square object"""
    def area(self):
        return self.__size * self.__size
