#!/usr/bin/python3
""" Defines an empty class """


class Rectangle:
    """defines rectangle with its arguments

    Args:
        width (int): width of rctngl.
        height (int): height of rctngl.
    """
    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height

    @property
    def width(self):
        """ sets width """
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """sets height"""
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height  must be >= 0")
        self._height = value
