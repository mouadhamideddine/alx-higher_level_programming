#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_copy = my_list[:]
    if (idx < 0 or idx > len(my_list) - 1 or not my_list):
        return list_copy
    list_copy[idx] = element
    return list_copy

# my_list = ['a']
# idx = 3
# new_element = 9
# new_list = new_in_list(my_list, idx, new_element)

# print(new_list)
# print(my_list)
