#!/usr/bin/python3
""" text_indentation module """


def whitespace_skip_index(string):
    """
    skips white spaces until a char is found
    @string: string
    return: how many indexes skipped
    """
    i = 0
    while (i < len(string)):
        # print("checking")
        if not string[i].isspace():
            return i
        i = i + 1
    return i


def read(character):
    """
    updates token for text_indentation func
    """
    new_line_sign = [".", "?", ":"]
    if character in new_line_sign:
        return True
    return False


def text_indentation(text):
    """
    provides indentation according to a set
    of speacial characters
    @text: string
    Return: Nothing
    """
    characters = [".?:"]
    token = False
    i = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if len(text) == 0:
        return
    while (i < len(text)):
        token = read(text[i])
        print(text[i], end="")
        if token:
            print("\n"*2)
            # print("new_line")
            j = whitespace_skip_index(text[i+1:])
            i += j
            # print(j)
            token = False
        i = i + 1


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
