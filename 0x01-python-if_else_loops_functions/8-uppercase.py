#!/usr/bin/python3

def uppercase(str):
    i = 0
    while i <= len(str) - 1:
        if ord(str[i]) >= 97:
            num = 32
        else:
            num = 0
        print("{}".format(chr(ord(str[i]) - num)), end="")
        i += 1
    print()
