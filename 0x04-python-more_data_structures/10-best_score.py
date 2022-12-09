#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None: 
        return None
    i = 0
    best_score = 0
    for key, val in a_dictionary.items():
        if i == 0: best_score = val
        if best_score < val: 
            best_score = val
            winner = key
        i+=1
    return winner

a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))
