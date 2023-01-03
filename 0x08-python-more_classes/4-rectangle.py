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
                raise ValueError("height must be >= 0")
            self.__height = high
        else:
            raise TypeError("height must be an integer")

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        newstr = ""
        if self.__width == 0 or self.__height == 0:
            return newstr
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                newstr += "#"
            if i < self.__height - 1:
                newstr += "\n"
        return newstr
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.__width}, {self.__height})"
