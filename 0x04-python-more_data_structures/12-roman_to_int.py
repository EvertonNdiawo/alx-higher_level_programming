#!/usr/bin/python3

def roman_to_int(roman_string):
    # Roman numeral single digits and substractive combinations
    roman_dict = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
    }
    roman_sub = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

    # Handle invalid input
    if not roman_string or not isinstance(roman_string, str):
        return 0

    # Split input string into valid pairs or singles
    numerals = []
    i = 0

    while i < len(roman_string):
        # Checks for two character match
        if i + 1 < len(roman_string) and roman_string[i:i+2] in roman_sub:
            numerals.append(roman_string[i:i+2])
            i += 2  # Character found in a pair,skip it,move to next one.
        else:
            numerals.append(roman_string[i])
            i += 1  # Move to next character

    # Iterate through list and calculate total
    total = 0

    for numeral in numerals:
        if numeral in roman_sub:
            total += roman_sub[numeral]
        else:
            total += roman_dict[numeral]

    return total
