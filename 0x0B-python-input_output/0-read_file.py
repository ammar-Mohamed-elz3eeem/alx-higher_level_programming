#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, mode="r", encoding="UTF-8") as fd:
        print(fd.read())
