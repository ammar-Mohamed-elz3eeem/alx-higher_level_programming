#!/usr/bin/python3
""" Module for making append_write functions """


def append_write(filename="", text=""):
    """append_write - writes the text input into the file given by filename

    Args:
        filename (str, optional): path to the file to read from it.
        text (str, optional): the text to be added to filename
        Defaults to "".
    """
    chars = 0
    with open(filename, mode="a", encoding="UTF-8") as fd:
        chars = fd.write(text)
    return chars
