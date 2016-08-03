"""given an image represented by an NxN matrix, where each pixel in the image is 4 bytes
write a method to rotate the image by 90 degrees.  Can you do this in place?

matrix = [
    [0,1,1,1],
    [0,0,1,1],
    [0,0,0,1],
    [0,0,0,0]
]

matrix_rotation = [
    [0,0,0,0],
    [0,0,0,1],
    [0,0,1,1],
    [0,1,1,1]
]

"""

def rotate(image):
    """function to rotate image in NxN matrix """

# top = temp
# top = left
# left = bottom
# bottom = right
# right = temp

    matrix[0] = temp
    matrix[0] = matrix[3][0], matrix[2][0], matrix[1][0], matrix[0][0]


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. BONER!\n"