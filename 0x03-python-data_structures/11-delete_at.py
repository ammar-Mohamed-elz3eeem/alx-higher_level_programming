#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    arrlen = len(my_list)
    if idx < 0 or idx > arrlen:
        return my_list
    i = 0
    while i < arrlen:
        if i == idx:
            my_list[i] = my_list[i+1]
            del my_list[i]
            arrlen -= 1
        i += 1
    return my_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)
