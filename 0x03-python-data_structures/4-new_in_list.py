#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)
    newl = [0] * length

    for i in range(0, length):
        if i == idx:
            newl[i] = element
        else:
            newl[i] = my_list[i]
    return newl
