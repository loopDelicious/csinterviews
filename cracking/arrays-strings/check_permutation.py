"""given 2 strings, write a method to decide if one is a permutation of the other

>>> check_permutation("dog","cat")
False

>>> check_permutation("dog","god")
True

>>> check_permutation("God    ", "dog")
False

"""

def check_permutation(str1, str2):
    """return True or False if 2 strings are permutations of each other"""


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NICE JOB!\n"
