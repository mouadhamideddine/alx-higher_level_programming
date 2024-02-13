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
    
    @staticmethod
    def to_json_string(list_dictionaries):
        "json repr dict"
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """ton json string"""
        json_ready = []
        filename = ""
        for element in list_objs:
            json_ready.append(element.to_dictionary())
        try:
            filename = f"{list_objs[0].__class__.__name__}.json"
        except:
            filename = f"{list_objs.__class__.__name__}.json"

        with open(filename, "w") as json_file:
            json_file.write(cls.to_json_string(json_ready))