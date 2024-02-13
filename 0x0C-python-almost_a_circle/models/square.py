#!/usr/bin/python3
"""square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """sqaure class inherits rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """init square"""
        super().__init__(size, size, x, y, id)
    
    @property
    def size(self):
        """size getter"""
        return self.width
    
    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """Overloading str function"""
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                             self.id, self.x, self.y,
                                             self.width)