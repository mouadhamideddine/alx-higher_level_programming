#!/usr/bin/python3
""" 10. Student to JSON with filter """


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        """init method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ return dict reprensenation"""
        if attrs is None:
            return self.__dict__
        new_dict = dict()
        if all(isinstance(elem, str) for elem in attrs):
            for element in attrs:
                if element in self.__dict__:
                    new_dict.update({element: self.__dict__[element]})
            return new_dict
        return self.__dict__
