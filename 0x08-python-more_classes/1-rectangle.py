#!/usr/bin/python3
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def width(self):
        return self.__width

    def height(self):
        return self.__height

    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('Width must be int')
        if value < 0:
            raise ValueError('Width must be superior to 0')
        self.__width = value

    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be int')
        if value < 0:
            raise ValueError('Height must be superior or equal to 0')
        self.__height = value
