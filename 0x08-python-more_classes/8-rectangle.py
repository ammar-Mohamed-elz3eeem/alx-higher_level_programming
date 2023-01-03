#!/usr/bin/python3
""" class Rectangle:
    This class is aimed for creating rectangles
"""


class Rectangle:
    """ class Rectangle:
        This class is aimed for creating rectangles
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
                newstr += str(self.print_symbol)
            if i < self.__height - 1:
                newstr += "\n"
        return newstr

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
