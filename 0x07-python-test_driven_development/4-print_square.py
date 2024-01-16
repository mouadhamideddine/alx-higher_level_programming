#!/usr/bin/python3
""" print_square module """


def print_square(size):
    """
    prints a square
    @size: size of the square
    return: nothing
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
    # squareprinting
    for rows in range(size):
        for lines in range(size):
            print("#", end="")
        print()


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
