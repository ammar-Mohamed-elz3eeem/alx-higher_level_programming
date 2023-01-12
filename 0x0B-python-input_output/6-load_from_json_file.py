#!/usr/bin/python3
""" Module for making load_from_json_file function """
import json


def load_from_json_file(filename):
    """load_from_json_file - read json format from filename

    Args:
        filename (str): file to read the json format from.
    """
    with open(filename, mode="r", encoding="UTF-8") as fd:
        data = json.load(fd)
    return data
