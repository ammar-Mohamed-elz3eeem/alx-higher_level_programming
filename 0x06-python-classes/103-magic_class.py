#!/usr/bin/python3
"""
MagicClass: resolved from python bytecode


"""
import math


class MagicClass:
    """MagicClass to calc area and circumference"""
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius
