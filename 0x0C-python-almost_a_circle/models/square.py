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

    def update(self, *args, **kwargs):
        """updates attributes based
          on positional arguments"""
        if args and len(args) > 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
            return
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "size" in kwargs:
            self.size = kwargs["size"]
        if "x" in kwargs:
            self.x = kwargs["x"]
        if "y" in kwargs:
            self.y = kwargs["y"]

    def to_dictionary(self):
        """diict repres"""
        return {'x': self.x,
                'y': self.y,
                'id': self.id,
                'size': self.width
                }
