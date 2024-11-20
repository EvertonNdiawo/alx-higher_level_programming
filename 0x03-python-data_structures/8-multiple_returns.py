#!/usr/bin/python3

def multiple_returns(sentence):

    first_char = ""
    length_s = len(sentence)

    if not sentence:
        first_char = None

    else:
        first_char = sentence[0]

    return (length_s, first_char)
