#!/usr/bin/python3

for i in range(0, 10):
    for j in range(0, 10):
        if (i * 10 + j) < (j * 10 + i):
            if (i == 8 and j == 9):
                print("{}{}".format(i, j), end="")
            else:
                print("{}{}".format(i, j), end=", ")
        else:
            continue
print()
