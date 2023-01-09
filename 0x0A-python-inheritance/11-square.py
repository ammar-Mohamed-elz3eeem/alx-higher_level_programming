#!/usr/bin/python3
"""
module that contain class Rectangle that is inherited from BaseGeometry class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Rectangle class: inherits features from BaseGeometry class
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return super().area()
