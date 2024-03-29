#!/usr/bin/python3

""" Area and perimeter """


class Rectangle:
    """
    definition of a Rectangle
    """
    def __init__(self, width=0, height=0):
        """initializer"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of rectangle"""
        return self.height * self.width

    def perimeter(self):
        """returns perimeter of rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height + self.width) * 2
