#!/usr/bin/python3
""" Defines an empty class """


class Rectangle:
    """defines rectangle with its arguments

    Args:
        width (int): width of rctngl.
        height (int): height of rctngl.
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ sets width """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """sets height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height  must be >= 0")
        self.__height = value

    def area(self):
        """calculates area"""
        return self.width * self.height

    def perimeter(self):
        """calculates perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """changes str function"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rct = []
        for i in range(self.__height):
            rct.append("#" * self.__width)
        return "\n".join(rct)
