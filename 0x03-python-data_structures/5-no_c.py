#!/usr/bin/env python3

def no_c(my_string):
    new_string = ""
    for elements in my_string:
        if elements != "c" and elements != "C":
            new_string += elements
    return new_string


# print(no_c("Best School"))
# print(no_c("Chicago"))
# print(no_c("C is fun!"))
# input_string = "This is a test string with some Cs and Cs."
# result = no_c(input_string)
# print(result)
