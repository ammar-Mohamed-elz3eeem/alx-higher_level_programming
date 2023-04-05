#!/usr/bin/python3
"""
Defines a peak-find function using 
binary search like algorithm.
"""


def find_peak(ints):
    """Return a peak in a list of unsorted integers."""
    if ints == []:
        return None

    arrlen = len(ints)
    if arrlen == 1:
        return ints[0]
    elif arrlen == 2:
        return max(ints)

    mid = int(arrlen / 2)
    peak = ints[mid]
    if peak > ints[mid - 1] and peak > ints[mid + 1]:
        return peak
    elif peak < ints[mid - 1]:
        return find_peak(ints[:mid])
    else:
        return find_peak(ints[mid + 1:])
