#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {"M": 1000, "D": 500, "C": 100,
              "L": 50, "X": 10, "V": 5, "I": 1}
    number = 0
    idx = 0
    
    if (not isinstance(roman_string, str)):
        return 0

    while idx in range(0, len(roman_string)):
        if idx < (len(roman_string) - 1) and \
           romans[roman_string[idx]] < romans[roman_string[idx + 1]]:
            number += romans[roman_string[idx + 1]] \
                      - romans[roman_string[idx]]
            idx += 1
        else:
            number += romans[roman_string[idx]]
        idx += 1
    return number
