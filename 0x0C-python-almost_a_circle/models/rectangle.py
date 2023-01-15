#!/usr/bin/python3
from models.base import Base
"""
This class will be used to create rectangle shape
and will be the “base” of Square class
"""


class Rectangle(Base):
    """
    Rectangle: the base class of the Sqaure class,
    aslo will be used to create rectangle shapes
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        if type(w) is not int:
            raise TypeError("width must be an integer")
        if w <= 0:
            raise ValueError("width must be > 0")
        self.__width = w

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h):
        if type(h) is not int:
            raise TypeError("height must be an integer")
        if h <= 0:
            raise ValueError("height must be > 0")
        self.__height = h

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        if type(val) is not int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        if type(val) is not int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        return (self.__width * self.__height)

    def display(self):
        [print("") for i in range(self.__y)]
        for i in range(self.__height):
            [print(" ", end="") for j in range(self.__x)]
            [print("#", end="") for j in range(self.__width)]
            print("")

    def update(self, *args, **kwargs):
        keys = ["id", "width", "height", "x", "y"]

        for idx in range(len(args)):
            setattr(self, keys[idx], args[idx])
        if len(args) <= 0 or args is None:
            for attr, val in kwargs.items():
                setattr(self, attr, val)

    def __str__(self):
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__,
                                                self.id,
                                                self.__x, self.__y,
                                                self.__width,
                                                self.__height)
