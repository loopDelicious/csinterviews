""" design a stack which in addition to push and pop, has a function min which returns the minimum element
push, pop, and min should all operate in O(1) time

    >>> [1,2,3].push(4)
    [1,2,3,4]

    >>> [1,2,3].pop()
    3

    >>> [1,2,3].min()
    1

    """
class Stack(object):

    def __init__(self, starting_list=None):

        if starting_list is None:
            self._list = []
        else:
            self._list = starting_list

    def push(self, item):
        """ adds item to the top of the stack """

        self._list.append(item)

    def pop(self):
        """ removes last item in the stack """

        popped = self._list.pop()
        return popped

    def min(self):
        """ returns the minimum item in the stack """

        minimum = self._list[0]
        while i < len(self._list):
            if self._list[i] < minimum:
                minimum = self._list[i]
        return minimum

        # FIXME wtf? in O(1)???  currently O(n)



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. WAY TO GO!\n"