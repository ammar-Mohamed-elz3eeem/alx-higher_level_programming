#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    i = 0
    best_score = 0
    winner = None
    for key, val in a_dictionary.items():
        if i == 0:
            best_score = val
            winner = key
        if best_score < val:
            best_score = val
            winner = key
        i += 1
    return winner
