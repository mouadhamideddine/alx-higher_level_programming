#!/usr/bin/env python3
def no_c(my_string):
    str_copy = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            str_copy += char
    return str_copy
# strin = ""
# print(no_c("Best School"))

