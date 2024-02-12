#!/usr/bin/python3
"""Rectangle Module"""
from models.base import Base

class Rectangle(Base):
    """Rectangle Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    @property
    def width(self):
        """width getter"""
        return self.__width
    @property
    def height(self):
        """height getter"""
        return self.__height
    @property
    def x(self):
        """x getter"""
        return self.__x
    @property
    def y(self):
        """y getter"""
        return self.__y

    @width.setter
    def width (self, value):
        """width.setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """height.setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    
    @x.setter
    def x(self, value):
        """x.setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
    
    @y.setter
    def y(self, value):
        """y.setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    
    def area(self):
        """rectangle area"""
        return self.width * self.height
    
    def display(self):
        """prints in stdout the Rectangle
        instance with the character #"""
        rows = ("#" * self.width) + "\n"
        print(rows * self.height, end="")
    
    def __str__(self):
        """override str method"""
        return f"[{type(self).__name__}] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"