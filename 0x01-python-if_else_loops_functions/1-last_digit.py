#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
denom = 10 if number >= 0 else -10
if number % denom > 5:
    print(f"Last digit of {number:d} is \
{number % denom} and is greater than 5")
elif number % denom < 6 and number != 0:
    print(f"Last digit of {number:d} is \
{number % denom} and is less than 6 and not 0")
else:
    print(f"Last digit of {number:d} is {number % denom} and is 0")
