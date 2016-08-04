class Tree(object):
    """Tree"""

    def __init__(self, root):
        self.root = root

    def find_BFS(self, node):
        """ find node in tree, using breadth first search (queue) """

        to_visit = [self.root]

        while to_visit:
            current = to_visit.pop(0)
            if current == node:
                return current
            else:
                to_visit.extend(current.children)

    def find_DFS(self, node):
        """ find node in tree, using depth first search (stack) """
        to_visit = [self.root]

        while to_visit:
            current = to_visit.pop()
            if current == node:
                return current
            else:
                to_visit.extend(current.children)

    def height(self):
        """ find height of the tree (non-BST) FIXME"""

        node = self
        heights = 0

        if not node:
            return 0

        for child in node.children:


    def list_nodes(self):
        """ list all nodes at each level of the tree """

        node = self

        if not node:
            return None
        node_list = []
        print node_list + list_nodes(node.left) + list_nodes(node.right)


class Node(object):
    """Node for Tree"""

    def __init__(self, data):
        self.data = data
        self.children = []

#################################################

class BinaryNode(object):
    """Node for Binary Tree"""

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def find_bst(self, sought):
        """ FIXME """

        current = self

        if not current:
            return None

        if current == sought:
            return current
        elif current > sought:
            find_bst(node.left, sought)
        else:
            find_bst(node.right, sought)

    def height_bst(self):
        """ find height of the tree """

        if not self.data:
            return 0

        left = height_bst(node.left)
        right = height_bst(node.right)

        return max(left, right) + 1

    def is_balanced(self):
        """ return True if tree is balanced within 1 level"""

        def _num_descendants(node):
            """ helper function to return number of levels of children for a BinaryNode """

            if not node:
                return 0

            left = _num_descendants(node.left)
            right = _num_descendants(node.right)

            if abs(left-right) > 1:
                return False

            return max(left, right) + 1

        return _num_descendants(self) is not None

    def is_subtree(self, bigger):
        """ determines if tree is a subtree of a larger tree """

        def _is_equal(first, second):
            """ determines if first tree is identical to second tree """

            if not first and not second:
                return True
            if first and not second:
                return False
            if second and not first:
                return False

            if first.data != second.data:
                return False

            return _is_equal(first.left, second.left) and _is_equal(first.right, second.right)

        node = self

        if not node:
            return False

        if node.data == bigger.data and _is_equal(node, bigger):
            return True
        else:
            return is_subtree(node, bigger.left) and is_subtree(node, bigger.right)

#################################################
class Graph(object):
