#!/usr/bin/python3

def tebahpla():

    for x in range(122, 96, -1):
        position_from_z = 122 - x

        if position_from_z % 2 == 0:
            control_value = 0
        else:
            control_value = 32
        print("{}".format(chr(x - control_value)), end="")


tebahpla()
