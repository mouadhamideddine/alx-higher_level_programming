#!/usr/bin/python3
"""
read file module
"""


def read_file(filename=""):
    """
    this function reads a file and prints its content to stdout
    @filename: string
    """
    if not filename:
        return
    with open(filename, 'r', encoding='utf8') as openfile:
        file_content = openfile.read()
        print(file_content)
