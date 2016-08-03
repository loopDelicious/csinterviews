"""given a string, check if it is a permutation of a palindrome.

>>> is_palindrome("tactcoa")
True

>>> is_palindrome("symian")
False

"""

def is_palindrome(astring):
    """function to check if string is an anagram of a palindrome """



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU'RE GETTING IT!\n"