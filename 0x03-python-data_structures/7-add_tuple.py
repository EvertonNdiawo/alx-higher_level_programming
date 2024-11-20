#!/usr/bin/python3

def add_tuple(tuple_a = (), tuple_b = ()):

    
    holder = 0
    result = ()
    
    if (tuple_a and tuple_b):

        if len(tuple_a) < 2:
            result = ((tuple_a[0] + tuple_b[0]), (holder + tuple_b[1]))
        
    
        elif len(tuple_b) < 2:
            result = ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + holder))
         

        elif (len(tuple_a) < 2) and (len(tuple_b) < 2):
            result = ((tuple_a[0] + tuple_b[0]), (holder))
          

        else:
            result = ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))
    
    elif (tuple_b) == ():
        result = ((tuple_a[0]), (tuple_a[1]))

    elif (tuple_a) == ():
        result = ((tuple_b[0]), (tuple_b[1]))

    else:
        result = ((holder), (holder))
    

    return result
