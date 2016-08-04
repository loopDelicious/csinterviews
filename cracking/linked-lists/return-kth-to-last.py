""" find the kth to last element of a singly linked list

>>> find_kth_to_last(ll=, 2))
4

"""

class LinkedList(object):
    """pointers to head, tail"""

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail


class Node(object):
    """Class in a linked list"""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def find_kth_to_last(ll):
    """find kth to the last element of a singly linked list"""

    previous = None




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. WAY TO GO!\n"