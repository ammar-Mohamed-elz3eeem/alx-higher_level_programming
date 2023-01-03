#!/usr/bin/python3
""" class Rectangle:
    This class is aimed for creating rectangles
"""


class Rectangle:
    """ class Rectangle:
        This class is aimed for creating rectangles
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, wid):
        if isinstance(wid, int):
            if wid < 0:
                raise ValueError("width must be >= 0")
            self.__width = wid
        else:
            raise TypeError("width must be an integer")
        
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, high):
        if isinstance(high, int):
            if high < 0:
                raise ValueError("width must be >= 0")
            self.__height = high
        else:
            raise TypeError("width must be an integer")
