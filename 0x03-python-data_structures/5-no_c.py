#!/usr/bin/env python3
def no_c(my_string):
    if not my_string:
        return my_string
    str_copy = ""
    for character in my_string:
        if character != 'c' and character != 'C':
            str_copy += character
    my_string = str_copy
    return my_string
# strin = ""
# print(no_c("Best School"))
