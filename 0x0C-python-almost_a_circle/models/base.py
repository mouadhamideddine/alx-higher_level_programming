#!/usr/bin/python3
""" BASE CLASS """
import json


class Base:
    """ base class """
    __nb_objects = 0

    def __init__(self, id=None):
        "constructor method"
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        "json repr dict"
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
