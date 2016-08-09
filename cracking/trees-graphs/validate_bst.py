""" implement a function to determine if a binary tree is a binary search tree """

class BinaryNode(object):

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def is_bst(node, min=None, max=None):
    """ is binary tree a binary search tree """

