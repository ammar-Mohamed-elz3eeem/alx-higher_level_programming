#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    sum = 0
    argv = argv[1:]
    for i in argv:
        sum += int(i)
    print(sum)