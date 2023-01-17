#!/usr/bin/python3
import json
import csv
import turtle
"""
This class will be the “base” of all other
classes in this project. The goal of it
is to manage id attribute in all your future classes
and to avoid duplicating the same code
"""


class Base:
    """ Base: the base class for all other classes """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) <= 0:
            return json.dumps([])
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        with open(cls.__name__+".json", mode="w") as fd:
            if list_objs is not None or len(list_objs) > 0:
                dicts = list(map(lambda o: o.to_dictionary(), list_objs))
                data = cls.to_json_string(dicts)
                json.dump(data, fd)
            else:
                json.dump([], fd)

    @staticmethod
    def from_json_string(json_string):
        if json_string == "[]" or json_string is None:
            return []
        return json.loads(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        created = None
        if dictionary is not None and len(dictionary.keys()) > 0:
            if cls.__name__ == "Rectangle":
                created = cls(1, 1)
            elif cls.__name__ == "Square":
                created = cls(1)
            created.update(**dictionary)
        return created

    @classmethod
    def load_from_file(cls):
        try:
            with open(cls.__name__ + ".json", mode="r") as fd:
                data = Base.from_json_string(fd.read())
                return list(map(lambda obj: cls.create(**obj), data))
        except IOError:
            return []
    @classmethod
    def save_to_file_csv(cls, list_objs):
        fields = None
        with open(cls.__name__ + ".csv", mode="w", encoding="UTF-8") as fd:
            if list_objs is None or len(list_objs) <= 0:
                fd.write("[]")
            else:
                if (cls.__name__ == "Rectangle"):
                    fields = ["id", "width", "height", "x", "y"]
                elif (cls.__name__ == "Square"):
                    fields = ["id", "size", "x", "y"]
                csvWriter = csv.DictWriter(fd, fields)
                for obj in list_objs:
                    csvWriter.writerow(obj.to_dictionary())
    @classmethod
    def load_from_file_csv(cls):
        fields = None
        try:
            with open(cls.__name__ + ".csv", mode="r", encoding="UTF-8") as fd:
                if (cls.__name__ == "Rectangle"):
                    fields = ["id", "width", "height", "x", "y"]
                elif (cls.__name__ == "Square"):
                    fields = ["id", "size", "x", "y"]
                list_objs = csv.DictReader(fd, fields)
                list_objs = [dict([k, int(v)] for (k , v) in obj.items()) for obj in list_objs]
                return [cls.create(**dic) for dic in list_objs]
        except IOError:
            return []
    @staticmethod
    def draw(list_rects, list_sqs):
        drawer = turtle.Turtle()
        drawer.pensize(3)
        drawer.shape("turtle")
        drawer.pensize(5)
        drawer.speed(1)

        drawer.color("#0f0f0f")
        for rect in list_rects:
            drawer.showturtle()
            drawer.up()
            drawer.goto(rect.x, rect.y)
            drawer.down()
            for i in range(2):
                drawer.forward(rect.width)
                drawer.left(90)
                drawer.forward(rect.height)
                drawer.left(90)
            drawer.hideturtle()

        drawer.color("#ff0000")
        for sq in list_sqs:
            drawer.showturtle()
            drawer.up()
            drawer.goto(sq.x, sq.y)
            drawer.down()
            for i in range(4):
                drawer.forward(sq.size)
                drawer.left(90)
        turtle.done()
            
