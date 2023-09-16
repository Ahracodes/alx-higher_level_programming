#!/usr/bin/python3
def magic_string():
    magic_string.nb = getattr(magic_string, "nb", 0) + 1
    return "BestSchool" + ", BestSchool" * (magic_string.nb - 1)
