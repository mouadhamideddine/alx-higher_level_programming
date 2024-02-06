#!/usr/bin/python3
""" Save Object to a file Module """
import json


def save_to_json_file(my_obj, filename):
    """
    @my_obj : python object
    convert my_obj to json string representation
    and writes it in @filename
    """
    with open(filename, 'w', encoding='utf8') as f:
        f.write(json.dumps(my_obj))
