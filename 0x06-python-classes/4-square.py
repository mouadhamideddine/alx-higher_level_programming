#!/usr/bin/python3
"""
Square class with size attribute and public instance
method def area(self):
"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """
        Constructor
        size - size of the square (int)
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Squares size"""
        return self.__size**2

    @property
    def size(self):
        """size attribute getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        size attribute setter
        Value : value to replace size attribute with
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
