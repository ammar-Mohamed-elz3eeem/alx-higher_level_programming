#!/usr/bin/python3
""" Module for making to_json_string function """
import json


def to_json_string(my_obj):
    """to_json_string - serialize objects into json format

    Args:
        filename (object): object to be serialized.
    """
    return json.dumps(my_obj)
