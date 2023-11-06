#!/usr/bin/python3
"""Class MyList"""

class MyList(list):
    """
    Custom list class
    Public Methods:
        print_sorted(self): prints list in ascending order
    """

    def print_sorted(self):
        """ Sortes in ascending order """
        print(sorted(self))
