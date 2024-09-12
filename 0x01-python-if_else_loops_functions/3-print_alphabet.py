#!/usr/bin/python3
for code in range(97, 123):
    alpha = chr(code)
    if alpha == 'e':
        continue
    elif alpha == 'q':
        continue
    else:
        print('{}'.format(alpha), end="")
