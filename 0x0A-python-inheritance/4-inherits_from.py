#!/usr/bin/python3
def inherits_from(obj, a_class):
    return obj.__class__.__name__ != a_class.__name__ and isinstance(obj, a_class)
