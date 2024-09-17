#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
import sys
from sys import argv

if __name__ == "__main__":

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(argv[1])
    b = int(argv[3])

    if argv[2] not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    operator = argv[2]

    if (operator == '+'):
        result = add(a, b)
        print("{} + {} = {}".format(a, b, result))

    if (operator == '-'):
        result = sub(a, b)
        print("{} - {} = {}".format(a, b, result))

    if (operator == '*'):
        result = mul(a, b)
        print("{} * {} = {}".format(a, b, result))

    if (operator == '/'):
        result = div(a, b)
        print("{} / {} = {}".format(a, b, result))
