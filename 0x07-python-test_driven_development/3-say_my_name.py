#!/usr/bin/python3
""" say_my_name module"""


def say_my_name(first_name, last_name=""):
    """
    a function given @first_name and @last_name args
    will print my name is followed by @first_name or @last_name if provided
    @first_name : str
    @last_name : str
    returns: Nothing
    """
    if not first_name:
        raise TypeError("first_name must be a string")
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if last_name:
        print("My name is {} {}".format(first_name, last_name))
        return
    if not last_name:
        print("My name is {}".format(first_name))
        return


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
