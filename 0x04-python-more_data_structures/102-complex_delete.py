#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    idx = True
    while idx:
        idx = False
        for k, v in a_dictionary.items():
            if v == value:
                del a_dictionary[k]
                idx = True
                break
    return a_dictionary
