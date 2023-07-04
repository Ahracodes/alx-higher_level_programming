#!/usr/bin/python3

#add_integer function def#
def add_integer(a, b):
    #check conditions for a#
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(a) is float:
        a = int(a)
    #check conditions for b#
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(b) is float:
        b = int(b)
    return a + b
