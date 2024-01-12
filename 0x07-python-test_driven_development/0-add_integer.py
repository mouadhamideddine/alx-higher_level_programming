#!/usr/bin/python3
def add_integer(a, b=98):
    """
    adds two nums
    >>> add_integer(4, 3)
    7
    >>> add_integer(5.5, 3.1)
    8
    >>> add_integer("string", 3)
    Traceback (most recent call last):
    ...
    TypeError: a must be an integer
    >>> add_integer(4, "string")
    Traceback (most recent call last):
    ...
    TypeError: b must be an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
