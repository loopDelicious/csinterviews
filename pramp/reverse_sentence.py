# You are given an array of characters arr, which consists of sequences of characters (words)
# separated by space characters.
# How can you most efficiently reverse the order of words in the sentence?
# Explain and code your solution and analyze the runtime and space complexity.
#
# For example:
# [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ', 'm', 'a', 'k', 'e', 's', '  ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]
#
# would turn into:
# [ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ', 'm', 'a', 'k', 'e', 's', '  ', 'p', 'e', 'r', 'f', 'e', 'c', 't' ]


def reverse_sentence(arr):
    """ reverse array of characters by space separated words """

    new_word = []
    results = []
    i = len(arr)

    while i > len(arr):
        if arr[i] != " ":
            new_word.append(arr[i])
            i -= 1
        else:
            results.append(new_word[::-1] + " ")
            new_word = []

    results.append(new_word[::-1])

    return results

# Runtime O(n) where n is the length of the original array
# Space O(1) for temporary variables and index
