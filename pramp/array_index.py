"""
Given an array of sorted distinct integers named arr, write a function that
returns an index i in arr for which arr[i] = i or -1 if no such index exists.

Implement the most efficient solution possible, prove the correctness of your solution
and analyze its runtime complexity (in terms of n - the length of arr).

    >>> index([-8,0,2,5])
    2

    >>> index([-1,0,3,6])
    -1

"""

def index(arr):
    """ return an index for which the index and element are equal """

    # Brute force O(n) where n is the length of the array
    # for i in range(len(arr)):
    #     if arr[i] == i:
    #         return i
    # return -1

    # using binary search for O(log n)
    while len(arr) > 1:
        midpoint = len(arr) / 2
        if arr[midpoint] == midpoint:
            return midpoint
        elif arr[midpoint] > midpoint:
            arr = arr[:midpoint]
        else:
            arr = arr[midpoint+1:]
    return -1


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. WAY TO GO!\n"