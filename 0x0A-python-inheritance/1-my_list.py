#!/usr/bin/python
"""
    MyList Class: extend functionality of list object
"""


class MyList(list):
    """ MyList Class: extend functionality of list object
        adding the ability to print sorted lists
    """
    def print_sorted(self):
        print(sorted(self))
