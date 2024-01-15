#/usr/bin/python3
def matrix_divided(matrix, div):
    """
    divides all elements of @matrix by @div
    >>> matrix_divided(7, 10)
    Traceback (most recent call last):
    ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats
    >>> matrix_divided([[1, 2, 3], [1, 2, "vim"]], 10)
    Traceback (most recent call last):
    ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats
    """
    if not isinstance(div, (float, int)):
        raise TypeError ("div must be a number")
    if div == 0:
        raise TypeError ("division by zero")
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
