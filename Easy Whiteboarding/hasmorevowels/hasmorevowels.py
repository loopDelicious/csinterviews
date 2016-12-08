"""Given a word in English, return True if that word contains more
   vowels than consonants. Return False otherwise.

    >>> has_more_vowels("Balloonicorn")
    False

    >>> has_more_vowels("moose")
    True

    >>> has_more_vowels(" ")
    False

    >>> has_more_vowels("")
    False
"""


def has_more_vowels(word):
    """Given a word in English, return True if that word contains more
       vowels than consonants. Return False otherwise.
    """


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. HOORAY!\n"
