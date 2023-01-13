#!/usr/bin/python3
""" Module to convert any class instance to json format """


def class_to_json(obj):
    """convert any class instance to json format

    Args:
        obj (object): objected to be converted to json data
    """

    return obj.__dict__
