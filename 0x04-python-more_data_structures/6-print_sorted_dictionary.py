#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    new_dic = sorted(a_dictionary.items())

    for i in new_dic:
        print("{}: {}".format(i[0], i[1]))
