#!/usr/bin/python3
"""square module"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """sqaure class inherits rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """init square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """str method"""
        return f"[square] ({self.id}) {self.x}/{self.y} - {self.size}"
    