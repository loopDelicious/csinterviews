"""Given a list of characters, replace all vowels in the list with *. Return
   the list.

    >>> replace_vowels(['h', 'i',' ', 't','h','e','r','e'])
    ['h', '*', ' ', 't', 'h', '*', 'r', '*']

    >>> replace_vowels([])
    []

    >>> replace_vowels(['o', 'o', 'o'])
    ['*', '*', '*']

    >>> replace_vowels(['z', 'z', 'z'])
    ['z', 'z', 'z']
"""


def replace_vowels(chars):
    """Given a list of characters, replace all vowels in the list with *. Return
       the list.
    """

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!\n"
