""" implement a function to determine if a binary tree is a binary search tree """


def validate_bst(node, min=None, max=None):

    if not node:  # base case for recursion
        return None

    if (min is not None and node.data <= min) or (max is not None and node.data > max):
        return False

    if not validate_bst(node.left, min, node.data) or not validate_bst(node.right, node.data, max):
        return False

