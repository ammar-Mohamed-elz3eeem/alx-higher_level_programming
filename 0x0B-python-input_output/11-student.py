#!/usr/bin/python3
""" module to define a class called student """


class Student:
    """ Student Class: class to initialize a new object type (student) """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            newdict = {}
            for attr in attrs:
                if self.__dict__.get(attr):
                    newdict[attr] = self.__dict__[attr]
            return newdict
        return self.__dict__
    
    def reload_from_json(self, json):
        for (k, v) in json.items():
            setattr(self, k, v)
