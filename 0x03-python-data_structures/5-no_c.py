#!/usr/bin/env python3
def no_c(my_string):
    str_copy = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            str_copy += char
    return str_copy

# print(no_c("Best School"))
# print(no_c("Chicago"))
# print(no_c("C is fun!"))
