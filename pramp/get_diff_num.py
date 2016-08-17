"""
Given an array arr of n unique non-negative integers, how can you most efficiently find a
non-negative integer that is not in the array?

Your solution should return such an integer or null if arr contains all possible integers.
Analyze the runtime and space complexity of your solution.

    >>> get_diff([0,3,4,5])
    6

    >>> get_diff([1,6])
    7

"""

def get_diff(arr):
    """ find a number that is not in the input array """

    # won't work if max integers
    # max = arr[0]
    # for item in arr:
    #     if item > max:
    #         max = item
    # return max + 1

    

if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED! GO GO GO!\n"