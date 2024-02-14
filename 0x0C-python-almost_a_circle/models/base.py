#!/usr/bin/python3
""" BASE CLASS """
import json
import os


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
        """save to file class method"""
        json_ready = []
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as file:
            if not list_objs:
                file.write(cls.to_json_string([]))
                return
            for element in list_objs:
                json_ready.append(element.to_dictionary())
            file.write(cls.to_json_string(json_ready))

    @staticmethod
    def from_json_string(json_string):
        """from json to string"""
        if not json_string or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes."""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """load from a file"""
        file_name = cls.__name__ + ".json"
        file_content = ""
        instances_list_original = []
        instances_list_creation = []
        if os.path.exists(file_name):
            with open(file_name, "r") as file:
                file_content = file.read()
            instances_list_original = cls.from_json_string(file_content)
            for element in instances_list_original:
                instances_list_creation.append(cls.create(**element))
            return (instances_list_creation)
        else:
            return []
