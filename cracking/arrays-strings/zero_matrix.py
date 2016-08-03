"""write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0

matrix = [
    [0,1,1,1],
    [1,0,1,1],
    [1,1,1,1],
    [1,1,1,1]
]

matrix_zeroed = [
    [0,0,0,0],
    [0,0,1,1],
    [0,0,1,1],
    [0,0,1,1]
]

"""

def zero(matrix):
    """function to zero out row and columns in MxN matrix """



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. PHEW!\n"