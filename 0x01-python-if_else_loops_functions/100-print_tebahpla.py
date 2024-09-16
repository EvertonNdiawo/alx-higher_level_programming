#!/usr/bin/python3

def tebahpla(x = 122):
    if x < 97:
        return

    position_from_z = 122 - x

    if position_from_z % 2 == 0:
        print(chr(x), end="")
    else:
        print(chr(x - 32), end="")

    tebahpla(x - 1)

tebahpla()
