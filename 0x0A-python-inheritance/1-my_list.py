#!/usr/bin/python3
""" my list class """


class MyList(list):
    """
    a custom list class
    """
    def print_sorted(self):
        print(sorted(self))
