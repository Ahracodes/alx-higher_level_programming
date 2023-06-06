#!/usr/bin/python3
def islower(c):
    nb = ord(c)
    if nb in range(97, 123):
        return True
    elif nb in range(65, 90):
        return False
