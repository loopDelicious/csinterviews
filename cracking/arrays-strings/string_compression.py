"""perform basic string compression using the counts of repeated characters.

>>> compress("aabcccccaaa")
a2b1c5a3

>>> compress("aabbccaaa")
a2b2c2a3

"""

def compress(astring):
    """function to compress string using counts of repeated characters """



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YIPPEE!\n"