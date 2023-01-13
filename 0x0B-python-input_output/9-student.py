#!/usr/bin/python3
""" module to define a class called student """


class Student:
    """ Student Class: class to initialize a new object type (student) """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__