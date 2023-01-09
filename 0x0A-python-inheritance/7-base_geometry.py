#!/usr/bin/python3
"""
BaseGeometry module: class BaseGeometry implementation
"""


class BaseGeometry:
    """
    BaseGeometry Class: class with non implemented function area,
    function integer_validator that validate if value is not int
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if value.__class__.__name__ == int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
