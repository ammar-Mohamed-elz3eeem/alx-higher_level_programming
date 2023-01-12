#!/usr/bin/python3
""" Module for making save_to_json_file function """
import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file - convert my_obj to json
    then writes it to filename.

    Args:
        my_obj (object): object to be converted to json.
        filename (str): file to write the json format to.
    """
    with open(filename, mode="a", encoding="UTF-8") as fd:
        json.dump(my_obj, fd)
