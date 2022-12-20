#!/usr/bin/python3
"""
Define Square Class with private attribute size
with some verfications that size attribute is correct
"""


class Square:
    """ Square Class is used to create
    squares with size == self.size """

    def __init__(self, s=0):
        if isinstance(s, int):
            if (s < 0):
                raise ValueError("size must be >= 0")
            self.__size = s
        else:
            raise TypeError("size must be an integer")
