""" given a binary tree, design an algorithm that creates a linked list of all the nodes at each depth
if you have a tree with depth D, you'll have D linked lists

"""

def linked_list_nodes(node):
    """ list all nodes in a linked list at each depth """

    if not node.left and not node.right:
        return None

    node.list = []

    return node.list + linked_list_nodes(node.left) + linked_list_nodes(node.right)

# FIXME need linked list not lists


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED! GO GO GO!\n"