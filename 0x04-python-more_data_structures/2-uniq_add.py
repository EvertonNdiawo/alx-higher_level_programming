#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_list = [i for i in set(my_list)]
    sum = 0

    for i in new_list:
        sum += i

    return sum
