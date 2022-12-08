#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    first = 0
    second = 0
    lentupa = len(tuple_a)
    lentupb = len(tuple_b)
    if (lentupa == 0):
        first = tuple_b[0]
        second = tuple_b[1]
        return (first, second)
    if (lentupb == 0):
        first = tuple_a[0]
        second = tuple_a[1]
        return (first, second)
    if (lentupa == 1):
        first = tuple_a[0]
        second = 0
        if (lentupb == 1):
            first += tuple_b[0]
            second += 0
        else:
            first += tuple_b[0]
            second += tuple_b[1]
        return first, second
    if (lentupb == 1):
        first = tuple_b[0]
        second = 0
        if (lentupa == 1):
            first += tuple_a[0]
            second += 0
        else:
            first += tuple_a[0]
            second += tuple_a[1]
        return first, second
    first = tuple_a[0] + tuple_b[0]
    second = tuple_b[1] + tuple_a[1]
    return (first, second)
