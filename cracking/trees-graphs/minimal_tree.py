""" given a sorted, ascending array with unique integer elements, write an algorithm to
create a binary search tree with minimal height

"""

class BinaryNode(self):

    def __init__(self, data, left=None, right=None):

        self.data = data
        self.left = left
        self.right = right


    def make_bst(arr):

        while len(arr) > 1:

            mid = len(arr) / 2

            root = BinaryNode(arr[mid])

            root.left = make_bst(arr[:mid]))
            root.right = make_bst(arr[mid+1:])

        return root
