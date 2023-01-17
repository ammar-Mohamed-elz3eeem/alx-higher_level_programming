#!/usr/bin/python3
from models.rectangle import Rectangle
"""
This class will be used to create square shapes
and will be inherited from Rectangle class
"""


class Square(Rectangle):
    """
    Square: Sqaure class will be used to create Square shapes
    """

    keys = ["id", "size", "x", "y"]

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, val):
        self.width = val
        self.height = val

    def to_dictionary(self):
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }

    def __str__(self):
        return "[{}] ({}) {}/{} - {}".format(
            type(self).__name__,
            self.id,
            self.x,
            self.y,
            self.width
        )
