#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    orglen = len(my_list)
    new_list = [False] * orglen
    for idx in range(0, orglen):
        if my_list[idx] % 2 == 0:
            new_list[idx] = True
    return new_list
