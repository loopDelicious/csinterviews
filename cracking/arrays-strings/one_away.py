"""there are 3 types of edits that can be performed on strings:
insert a character, remove a character, or replace a character.
given 2 strings, check if they are one edit (or zero edits) away.

>>> one_away("pale","ple")
True

>>> one_away("pales","pale")
True

>>> one_away("pale","bale")
True

>>> one_away("pale","bake")
False

"""

def one_away(str1, str2):
    """function to check if 2 strings are 1 (or less) edits away """



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. WOOHOO!\n"