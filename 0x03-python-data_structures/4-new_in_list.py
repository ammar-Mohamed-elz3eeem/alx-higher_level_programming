#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newl = []

    if idx < 0:
        return None

    if idx >= len(my_list):
        return None

    for i in range(0, len(my_list)):
        if i == idx:
            newl[idx] = element
        else:
            newl[i] = my_list[i]
