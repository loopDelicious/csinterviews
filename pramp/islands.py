"""
Given a 2D matrix M, filled with either 0s or 1s, count the number of islands of 1s in M.
An island is a group of adjacent values that are all 1s. Every cell in M can be adjacent to
the 4 cells that are next to it on the same row or column.

matrix = [
       [ 0  1  0  x  0 ],
       [ 0  0  1  1  1 ],
       [ 1  0  0  1  0 ],
       [ 0  1  1  0  0 ],
       [ 1  0  1  0  1 ],
        ]

"""
def count_islands(M):

    if M is None or len(M) == 0:
        return 0

    r = len(M)
    c = len(M[0])
    islands = 0

    for i in range(r):
        for j in range(c):
            if M[i,j] == 1:
                islands += 1
                look_around(M, r, c, i, j)


def look_around(M, r, c, i, j):

    queue = []
    queue.push([i,j])

    while len(queue) != 0:
        item = queue.pop()
        x = item[0]
        y = item[1]

        if M[x,y] == 1:

            M[x,y] = 0

            pushIfValid(queue, r, c, x-1,y)
            pushIfValid(queue, r, c, x, y+1)
            pushIfValid(queue, r, c, x+1, y)
            pushIfValid(queue, r, c, x, y-1)


def pushIfValid(queue, r, c, x, y):

    if x >= 0 and y >= 0 and x < len(r) and y < len(c):
        queue.push([x,y])


# Runtime complexity is O(r*c) where r is number of rows and c is number of columns