"""write a method to replace all spaces in as tring with '%20'.

>>> URLify("Mr John Smith")
"Mr%20John%20Smith"

>>> URLify("hello there")
"hello%20there"

"""

def URLify(astring):
    """method to replace all spaces in a string with '%20' """


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. DO IT!\n"


