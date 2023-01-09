#!/usr/bin/python3
"""
    module that contains an extended version of the list object class
"""


class MyList(list):
    """ MyList Class: extend functionality of list object
        adding the ability to print sorted lists
    """
    def print_sorted(self):
        print(sorted(self))
