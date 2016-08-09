"""

Given an array of integers arr, write a function that returns another array at the
same length where the value at each index i is the product of all array values except arr[i].

Solve without using division and analyze the runtime and space complexity

    >>> array_products([2, 7, 3, 4])
    [84, 24, 56, 42]

    [7*3*4, 2*3*4, 2*7*4, 2*7*3]
"""

def array_products(arr):
    """ return an array of the same length as the input array where the value at each index
    is the product of all array vallues except at the current index """

    # Brute force O(n^2)
    # results = []
    # for i in range(len(arr)):
    #     product = 1
    #     for j in range(len(arr)):
    #         if i == j:
    #             continue
    #         product *= arr[j]
    #     results.append(product)
    # return results

    # create new arrays to maintain product to the left and right of each index O(n)
    left = [1] * len(arr)
    for i in range(1,len(arr)):
        left[i] = left[i-1] * arr[i-1]

    right = [1] * len(arr)
    for i in range(len(arr)-1, -1, -1):
        right[i] = right[i+1] * arr[i+1]

    new_array = [1] * len(arr)
    for i in range(len(arr)):
        new_array[i] = left[i] * right[i]

    return new_array

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. WAY TO GO!\n"