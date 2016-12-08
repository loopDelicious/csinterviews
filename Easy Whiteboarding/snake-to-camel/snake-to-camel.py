"""
>>> snake_to_camel("hi_balloonicorn")
'hiBalloonicorn'

>>> snake_to_camel("snake_case is_out")
'snakeCase isOut'

"""


def snake_to_camel(str):
    """Given a string in snake_case, return the same string in camelCase"""


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. HOORAY!\n"
