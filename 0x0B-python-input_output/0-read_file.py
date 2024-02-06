#!/usr/bin/python3
"""
read file module
"""


def read_file(filename=""):
    with open(filename, 'r', encoding='utf8') as openfile:
        file_content = openfile.read()
        print(file_content)
