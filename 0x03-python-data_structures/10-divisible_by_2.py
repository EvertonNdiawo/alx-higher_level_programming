#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    result_list = [item % 2 == 0 for item in my_list]

    return result_list
