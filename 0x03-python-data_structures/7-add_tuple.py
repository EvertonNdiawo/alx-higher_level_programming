#!/usr/bin/python3

def add_tuple(tuple_a = (), tuple_b = ()):
    
    holder = 0
    result = ()
    
    if (tuple_a and tuple_b) == None:
        result = ((holder), (holder))

    elif tuple_a[1] == None:
        result = ((tuple_a[0] + tuple_b[0]), (holder + tuple_b[1]))
    
    elif tuple_b[1] == None:
        result = ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + holder))

    elif (tuple_a[1] and tuple_b[1]) == None:
        result = ((tuple_a[0] + tuple_b[0]), (holder))

    else:
        result = ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))
