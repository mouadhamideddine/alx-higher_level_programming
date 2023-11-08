#!/usr/bin/python3
square = lambda x: x ** 2
def square_matrix_simple(matrix=[]):
    if not matrix:
        return matrix
    squared_nums = []
    matrix_iter = matrix[:]
    for _list in matrix_iter:
        if _list:
            result = list(map(square, _list))
            squared_nums.append(result)
    return squared_nums

'''
matrix = []

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
'''
