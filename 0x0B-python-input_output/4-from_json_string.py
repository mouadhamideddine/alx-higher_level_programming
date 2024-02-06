#!/usr/bin/python3
"""     JSON STRING TO OBJECT       """
import json


def from_json_string(my_str):
    """
    deserialize json string to python object
    and RETURNS IT
    """
    return (json.loads(my_str))
