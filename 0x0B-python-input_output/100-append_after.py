#!/usr/bin/python3
""" module to add add new string according to citeria """


def append_after(filename="", search_string="", new_string=""):
    """ append_after
    Insert text after each line containing a given string in a file

    Args:
        filename (str, optional): filename to search on. Defaults to "".
        search_string (str, optional): search string
        to add new string after it. Defaults to "".
        new_string (str, optional): string that should be added
        when found the search string. Defaults to "".
    """
    text = ""
    with open(filename, mode="r", encoding="utf-8") as fd:
        for line in fd:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, mode="w", encoding="utf-8") as fd:
        fd.write(text)
