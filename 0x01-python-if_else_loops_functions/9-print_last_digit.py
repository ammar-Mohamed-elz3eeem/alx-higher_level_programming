#!/usr/bin/python3
def print_last_digit(number):
    denom = 10 if number >= 0 else -10
    print("{:d}".format(abs(number % denom)), end="")
    return abs(number % denom)
