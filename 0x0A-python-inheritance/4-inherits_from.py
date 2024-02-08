#!/usr/bin/python3
""" 4. Only sub class of """


def inherits_from(obj, a_class):
    """
    inherited (directly or indirectly)
    check
    """
    return isinstance(obj, a_class) or issubclass(a_class, obj)
