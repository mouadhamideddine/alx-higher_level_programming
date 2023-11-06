#!/usr/bin/python3
def element_at(my_list, idx):
    count = -1;# -1 because idx starts from 0
    if idx < 0:
        return (None)
    for element in my_list:
        count += 1
        if count == idx:
            return (element)
    return (None)
# my_list = [1, 2, 3, 4, 5]
# idx = 0
# print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
