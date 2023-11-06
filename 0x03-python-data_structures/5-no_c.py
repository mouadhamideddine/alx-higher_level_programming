#!/usr/bin/env python3
def no_c(my_string):
    str_copy = ""
    for character in my_string:
        if character != 'c' and character != 'C':
            str_copy += character
    return str_copy
# strin = ""
# print(no_c("Best School"))
