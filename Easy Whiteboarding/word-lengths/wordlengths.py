"""Given a sentence as a string, return a dictionary containing
   length: list of words of that length as key: value pairs.

    >>> word_lengths("Hi, I'm Ballonicorn!")
    {3: ['Hi,', "I'm"], 12: ['Ballonicorn!']}

    >>> word_lengths("")
    {0: ['']}

    >>> word_lengths("Cute cats chase fuzzy rats.")
    {4: ['Cute', 'cats'], 5: ['chase', 'fuzzy', 'rats.']}

    >>> word_lengths("Coffee!")
    {7: ['Coffee!']}
"""


def word_lengths(sentence):
    """Given a sentence, return a dictionary of word lengths and the words
    in the sentence of each length.
    """


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NOTHING ESCAPES YOU!\n"