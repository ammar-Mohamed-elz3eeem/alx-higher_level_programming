#!/usr/bin/python3
"""
module that contains a function to check if the type of
the input is same as the type specified in function or not
"""


def is_kind_of_class(obj, a_class):
    """ return true if obj class name exactly equal to the a_class name """
    return isinstance(obj, a_class)
