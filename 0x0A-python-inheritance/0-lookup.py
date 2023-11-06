#!/usr/bin/python3
"""
Return a list of attr and methods.
Args:
    Obj: Object to list the methods and attr for.

Returns:
    list: list of attributes and methods associated with obj.
"""
def lookup(obj):
    """ Returns list of attrs """
    return dir(obj)

