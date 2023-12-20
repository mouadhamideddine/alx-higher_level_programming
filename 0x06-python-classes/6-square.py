#!/usr/bin/python3
"""
Square class with size attribute and public instance
method def area(self):
"""


class Square:
    """Square class"""
    def is_valid_position(self, _position):
        """checker for correction self.position attribute"""
        if not isinstance(_position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(_position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in _position:
            if not isinstance(i, int) or i < 0:
                raise TypeError("position must be a tuple of 2 positive "
                                "integers")
        return True

    def __init__(self, size=0, position=(0, 0)):
        """
        Constructor
        size - size of the square (int)
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if self.is_valid_position(position) is True:
            self.__position = position

    def area(self):
        """Squares size"""
        return self.__size**2

    @property
    def size(self):
        """size attribute getter"""
        return self.__size

    @property
    def position(self):
        "position attribute getter"
        return self.__position

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

    @position.setter
    def position(self, value):
        """
        position setter
        """
        self.is_valid_position(value)
        self.__position = value

    def my_print(self):
        """
        prints the square
        """
        if self.__size == 0:
            print()
        print("\n" * self.__position[1], end="")
        for lines in range(self.__size):
            print(" " * self.__position[0], end="")
            for hashtags in range(self.__size):
                print("#", end="")
            print()
