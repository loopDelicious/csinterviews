class LinkedList(object):
    """LinkedList"""

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def reverse_ll(self):
        """ reverse linked list while creating a new linked list """

        current = self.head
        previous = None

        while current is not None:
            out_head = Node(n.data, previous)
            previous = out_head

        return out_head

    def reverse_ll_in_place(self):
        """ reverse linked list without creating a new linked list """

        previous = None
        current = self.head

        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next

        self.head = previous

    def remove_node(self, node):
        """ remove node from linked list """

        node.data = node.next.data
        node.next = node.next.next


class Node(object):
    """Class in a linked list"""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next