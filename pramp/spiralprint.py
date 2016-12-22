# Given a 2D array (matrix) named M, print all items of M in a spiral order, clockwise.
# For example:
#
# M  =  1   2   3   4   5
#       6   7   8   9  10
#       11  12  13  14  15
#       16  17  18  19  20
#
# The clockwise spiral print is:  1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12

def spiralprint(M):
    '''print clockwise'''

    # declare index placeholders
    top = 0
    right = len(M[0]) - 1
    bottom = len(M) - 1
    left = 0

    while bottom <= top and left <= right:
        for i in range(left, right):
            print M[top][i]
        top += 1
        for j in range(top, bottom):
            print M[j][right]
        right -= 1
        for k in range(right, left):
            print M[bottom][k]
        bottom -= 1
        for l in range(bottom, top):
            print M[l][left]
        left += 1

# Runtime complexity: O (m * n) where they are number of rows * columns)
# Space complexity:  O(1) for 4 placeholder variables
