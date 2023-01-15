#!/usr/bin/python3
"""
This class will be the “base” of all other
classes in this project. The goal of it
is to manage id attribute in all your future classes
and to avoid duplicating the same code
"""


class Base:
    """ Base: the base class for all other classes """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
        else:
            self.id = id
