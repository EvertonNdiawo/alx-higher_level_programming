#!/usr/bin/python3

def best_score(a_dictionary):
    temp_v = 0
    temp_k = ""

    if a_dictionary != None:
        for key, value in a_dictionary.items():
             if value >= temp_v:
                temp_v = value
                temp_k = key
   
        return temp_k
    
    else:
        return None
