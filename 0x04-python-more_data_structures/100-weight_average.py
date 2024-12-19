#!/usr/bin/python3

def weight_average(my_list=[]):
    sum_prod, sum_weights = 0, 0

    if not my_list:
        return 0

    for x, v in my_list:
        sum_prod += x*v
        sum_weights += v

    return sum_prod / sum_weights
