#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return
    for element in reversed(my_list):
        print("{:d}".format(element))


# my_list = []
# print_reversed_list_integer(my_list)
# print(my_list[0])
