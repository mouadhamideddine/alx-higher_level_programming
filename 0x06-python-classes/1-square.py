#!/usr/bin/python3
"""this adds Private instance attribute: size to Square class"""


class Square:
    def __init__(self, size):
        """
        init a Square with a given size
        """
        self.__size = size
