#!/usr/bin/python3

def lookup(obj):
    """
    Return a list of attr and methods
    Args:
    Obj: Object to list the methods and attr for
    Returns:
    list: list of attributes and methods
    """
    return dir(obj)

