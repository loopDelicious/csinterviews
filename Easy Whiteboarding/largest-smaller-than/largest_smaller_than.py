"""
    >>> find_largest_smaller_than([-5, 8, 12, 32], 10)
    1

    >>> find_largest_smaller_than([-5, 8, 12, 32], 33)
    -1

    >>> find_largest_smaller_than([-5, 8, 12, 32], -7)

"""

def find_largest_smaller_than(nums, xnumber):
    """ In a sorted list of nums, find largest number that is smaller than xnumber,
    returns None if not found"""



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU ARE A TREE GENIUS!\n"


