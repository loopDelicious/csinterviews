"""
>>> calc("+ 1 2")  # 1 + 2
3
>>> calc("* 2 + 1 2")  # 2 * (1 + 2)
6
>>> calc("+ 9 * 2 3")   # 9 + (2 * 3)
15
>>> calc("- 1 2")  # 1 - 2
-1
>>> calc("- 9 * 2 3")  # 9 - (2 * 3)
3
>>> calc("/ 6 - 4 2")  # 6 / (4 - 2)
3
"""

def calc(s):
    """Evaluate expression."""
    


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. EXCELLENT GAME!\n"



