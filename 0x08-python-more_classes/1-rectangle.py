#!/usr/bin/python3
""" class Rectangle:
    This class is aimed for creating rectangles
"""


class Rectangle:
    """ class Rectangle:
        This class is aimed for creating rectangles
    """
    def __init__(self, width):
        self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if (not isinstance(width, int)):
            raise TypeError("width must be an integer")
        if (width < 0):
            raise ValueError("width must be >= 0")
        self.__width = width
