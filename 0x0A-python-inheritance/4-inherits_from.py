#!/usr/bin/python3
""" 4. Only sub class of """


def inherits_from(obj, a_class):
    """
    inherited (directly or indirectly)
    check
    """
    if issubclass(type(obj), a_class):
        return True
    return False
