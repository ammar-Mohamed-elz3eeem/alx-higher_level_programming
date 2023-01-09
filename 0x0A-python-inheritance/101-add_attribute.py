#!/usr/bin/python3
"""
module to add feature to classes even custom or built in
by making them able to recieve new attributes
"""


def add_attribute(obj, attr, value):
    """
    add_attribute - function that adds new attributes
    with thier values to built in or custom classes in python

    Args:
        obj (object): class object that we need to add attribute to
        attr (string): attribute to be added to the class
        value (string): value of the attribute

    Raises:
        TypeError: if can't add new attributes to class

    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    type(obj).__setattr__(obj, attr, value)
