#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ordered = list(a_dictionary.keys())
    ordered.sort()
    for x in ordered:
        print("{}: {}".format(x, a_dictionary.get(x)))
