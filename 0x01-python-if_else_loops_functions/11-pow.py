#!/usr/bin/python3
def pow(a, b):
    prod = 1
    if (b < 0):
        return 1 / pow(a, abs(b))
    for i in range(0, b):
        prod *= a
    return prod
