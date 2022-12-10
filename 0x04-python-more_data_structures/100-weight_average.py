#!/usr/bin/python3
def weight_average(my_list=[]):
    sum_weight = 0
    sum_all = 0
    for tup in my_list:
        sum_weight += tup[1]
        sum_all += tup[0] * tup[1]
    return sum_all * 1.0 / (sum_weight if sum_weight > 0 else 1)
print(weight_average([]))