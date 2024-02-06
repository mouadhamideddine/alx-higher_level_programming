#!/usr/bin/python3
""" write file module """


def write_file(filename="", text=""):
    """
    overwrite file with @text string
    create file if @filename doesn't exist
    return number of characters written
    """
    if not filename:
        return
    with open(filename, 'w', encoding='utf8') as f:
        chars_written = f.write(text)
    return chars_written
