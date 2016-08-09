"""
Merging 2 Packages

Given a package with a weight limit and an array arr of item weights,
how can you most efficiently find two items with sum of weights that equals the weight limit?

Your function should return 2 such indices of item weights or -1 if such pair doesn't exist.
What is the runtime and space complexity of your solution?

    >>> sorted(merging(10, [-10, 10, 20, 15, 6]))
    [0, 2]

"""

def merging(limit, arr):
    """ find 2 items with sum of weights that equals the weight limit """

    # Brute Force O(n^2)

    # for i in range(len(arr)):
    #     for j in range(len(arr)):
    #         if arr[i] + arr[j] == limit:
    #             return [i, j]
    #
    # return -1

    # Make a hash table to keep track of what we've seen O(n)
    weight_dict = {}
    for i in range(len(arr)):

        if arr[i] not in weight_dict:
            weight_dict[arr[i]] = i

        target = limit - arr[i]

        if target in weight_dict and i != weight_dict[target]:
            return [i, weight_dict[target]]

    return -1


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. WAY TO GO!\n"

