#!/usr/bin/python3
""" is same class module """


def is_same_class(obj, a_class):
    """ is same class function
    @obj : object
    @a_class : class to check if object is instance
    return : BOOLEAN
    """
    if type(obj) is a_class:
        return True
    return False
