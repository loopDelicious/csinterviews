"""given an image represented by an NxN matrix, where each pixel in the image is 4 bytes
write a method to rotate the image by 90 degrees.  Can you do this in place?

>>> matrix = [[1, 1, 1, 2],
...           [4, 5, 6, 2],
...           [4, 7, 8, 2],
...           [4, 3, 3, 3]]

>>> rotate(matrix)
[[4, 4, 4, 1], [3, 7, 5, 1], [3, 8, 6, 1], [3, 2, 2, 2]]

"""

def rotate(matrix):
    """function to rotate image in NxN matrix """

    n = len(matrix)

    rotated = []

    for i in range(n):
        rotated.append([])
        for j in range(n):
            rotated[i].append(matrix[n-1-j][i])
    return rotated

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. BONER!\n"

    # top = temp
    # top = left
    # left = bottom
    # bottom = right
    # right = temp

    # matrix[0] = temp
    # matrix[i][0] = [matrix[3][0], matrix[2][0], matrix[1][0], matrix[0][0]]
    # matrix[3] = [matrix[3][3], matrix[3][2], matrix[3][1], matrix[3][0]]
    # matrix[i][3]
    # matrix[0]