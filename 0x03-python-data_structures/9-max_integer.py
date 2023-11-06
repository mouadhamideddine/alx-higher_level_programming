#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    compare_var = 0
    token = True
    for element in my_list:
        if token:
            compare_var = element
            token = False
        if compare_var < element:
            compare_var = element
    return compare_var


'''
my_list = [1, 90, 2, 13, 34, 5, -13, 3, 9500]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
'''
