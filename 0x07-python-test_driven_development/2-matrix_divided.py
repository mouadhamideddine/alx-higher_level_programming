#!/usr/bin/python3
"""Module for matrix_divided method."""
def matrix_divided(matrix, div):
    """
    Divides all elements of matrix by div.
    Args:
        matrix: List of lists containing int or float
        div: number to divide matrix by
    Returns:
        list: List of lists representing divided matrix.
    Raises:
        TypeError: If matrix is not list of lists containing int or float.
        TypeError: If sublists are not all same size.
        TypeError: If div is not int or float.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(div, (float, int)):
        raise TypeError ("div must be a number")
    if div == 0:
        raise ZeroDivisionError ("division by zero")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if isinstance(matrix[0], list):
        length = len(matrix[0])
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError ("matrix must be a matrix (list of lists) of integers/floats")
        if length != len(row):
            raise TypeError ("Each row of the matrix must have the same size")
        for number in row:
            if not isinstance(number, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    new_matrix = []
    for i in range(len(matrix)):
        new_row = []
        for j in range(len(matrix[i])):
                new_row.append(round(matrix[i][j] / div, 2))
        new_matrix.append(new_row)
    return new_matrix


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
