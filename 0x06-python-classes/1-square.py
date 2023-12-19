#!/usr/bin/python3
"""this adds Private instance attribute: size to Square class"""


class Square:
    def __init__(self, size):
        """Constructor.
        Args:
            size: length of size of the square
        """
        self.__size = size
