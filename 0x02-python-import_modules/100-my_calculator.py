#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    argv = argv[1:]
    if len(argv) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[1] not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    op = argv[1]
    a = int(argv[0])
    b = int(argv[2])
    if op == '+':
        res = add(a, b)
    elif op == '-':
        res = sub(a, b)
    elif op == '*':
        res = mul(a, b)
    else:
        res = div(a, b)

    print("{} {:s} {} = {}".format(argv[0], op, argv[2], res))
