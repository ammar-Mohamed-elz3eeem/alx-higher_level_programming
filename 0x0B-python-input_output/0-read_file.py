#!/usr/bin/python3
""" Module for making read_file functions """


def read_file(filename=""):
    """read_file - reads the text content from the file

    Args:
        filename (str, optional): path to the file to read from it.
        Defaults to "".
    """
    with open(filename, mode="r", encoding="UTF-8") as fd:
        print(fd.read())
