#!/usr/bin/python3
""" Module for making from_json_string function """
import json


def from_json_string(my_str):
    """from_json_string - deserialize string into dict format

    Args:
        my_str (str): string to be deserialized.
    """
    return json.loads(my_str)
