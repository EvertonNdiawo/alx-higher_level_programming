#!/usr/bin/python3
from functools import reduce

def roman_to_int(roman_string):
    # Roman numeral single digits and substractive combinations
    roman_dict = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
    roman_sub = { 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900 }

    # Split input string into valid pairs or singles
    numerals = []
    i = 0

    while i < len(roman_string):
        # Checks for two character match
        if i + 1 < len(roman_string) and roman_string[i:i+2] in roman_sub:
            numerals.append(roman_string[i:i+2])
            i += 2 # Character found in a pair, so skip it and move to the next one.
        else:
            numerals.append(roman_string[i])
            i += 1 # Move to next character

    # Map each element to its value
    values = map(lambda x: roman_sub[x] if x in roman_sub else roman_dict[x], numerals)

    # Reduce() to calculate the total sum
    total = reduce(lambda acc, val: acc + val, values, 0)

    return total


