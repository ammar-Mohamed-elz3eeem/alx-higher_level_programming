#!/usr/bin/python3
"""
module that contains a function to check if the type of
the input is inherited from the type specified in function or not
"""
def inherits_from(obj, a_class):
    """
    function to check if the type of
    the input is inherited from the type specified in function or not
    """
    return obj.__class__.__name__ != a_class.__name__ and isinstance(obj, a_class)
