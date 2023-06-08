#!/usr/bin/python3
import sys

if __name__ == "__main__":
    lgt = len(sys.argv) - 1
    sum = 0
    for x in range(lgt):
        sum += int(sys.argv[x + 1])
    print("{}".format(sum))
