#!/usr/bin/python3
""" Module for making write_file functions """


def write_file(filename="", text=""):
    """write_file - writes the text input into the file given by filename

    Args:
        filename (str, optional): path to the file to read from it.
        text (str, optional): the text to be added to filename
        Defaults to "".
    """
    chars = 0
    with open(filename, mode="a", encoding="UTF-8") as fd:
        chars = fd.write(text)
    return chars
