#!/usr/bin/python3
import sys

if __name__ == "__main__":
    result = 0
    if len(sys.argv) < 2:
        print(int(result))
    else:
        for i in range(1, len(sys.argv)):
            result += int(sys.argv[i])
        print("{}".format((result)))
