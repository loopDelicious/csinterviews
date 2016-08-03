"""write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0

    >>> zero([[1, 0, 3], [4, 5, 6], [7, 8, 9]])
    [[0, 0, 0], [4, 0, 6], [7, 0, 9]]

    >>> zero([[1, 0, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    [[0, 0, 0, 0], [5, 0, 7, 8], [9, 0, 11, 12]]

"""

def zero(matrix):
    """function to zero out row and columns in MxN matrix """

    nrows = len(matrix)     #y
    ncols = len(matrix[0])  #x

    if not matrix:
        return []

    clear_rows = [False] * nrows
    clear_cols = [False] * ncols

    for y in range(nrows):
        for x in range(ncols):
            if matrix[y][x] == 0:
                clear_rows[y] = True
                clear_cols[x] = True
    for y in range(nrows):
        for x in range(ncols):
            if clear_rows[y] or clear_cols[x]:
                matrix[y][x] = 0
    return matrix


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. PHEW!\n"