"""
>>> translate_leet("hi balloonicorn")
'hi ba1100nic0rn'

>>> translate_leet("hackbright is the shizzle")
'hackbrigh7 i5 7h3 5hizz13'

"""


def translate_leet(str):
    """Translates input into l33t.
    Translate to 1337 speak (replace o w 0, e w 3, L w 1, s w 5, t w 7)"""




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. HOORAY!\n"
