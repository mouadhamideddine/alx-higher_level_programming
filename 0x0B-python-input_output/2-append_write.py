#!/usr/bin/python3
""" append write to file module """


def append_write(filename="", text=""):
    """
    append to file with @text string
    create file if @filename doesn't exist
    return number of characters written
    """
    if not filename:
        return
    with open(filename, 'w', encoding='utf8') as f:
        chars_written = f.write(text)
    return chars_written
