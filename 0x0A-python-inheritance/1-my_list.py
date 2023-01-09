#!/usr/bin/python
"""
    MyList Class: extend functionality of list object
"""
class MyList(list):
    def print_sorted(self):
        print(sorted(self))
