#!/usr/bin/python3
""" TO JSON STRING MODULE """


def to_json_string(my_obj):
    """
    converts python object @my_obj
    to json string representation
    of it
    return: json string reprensentation
    """
    return (json.dumps(my_obj))
