#!/usr/bin/python3

def print_list(_list):
    if not _list:
        return
    length = len(_list)
    count = 0
    for element in _list:
        count += 1
        if count == length:
            print("{:d}".format(element))
            return
        print("{:d}".format(element), end=" ")
    return



def print_matrix_integer(matrix=[[]]):
    for _list in matrix:
        print_list(_list)
    return
'''
matrix = [
            [1, 2, 3,5],
                [4, 5, 6],
                    [7, 8, 9]
                    ]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
'''
