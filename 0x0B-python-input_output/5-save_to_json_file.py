#!/usr/bin/python3
""" Save Object to a file Module """
import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'w', encoding='utf8') as f:
        f.write(json.dumps(my_obj))
