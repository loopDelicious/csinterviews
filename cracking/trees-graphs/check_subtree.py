""" T1 and T2 are 2 very large binary trees, with T1 much bigger than T2
Create an algorithm to determine if T2 is a subtree of T1.

"""

def is_subtree(T1, T2):
    """ is T2 a subtree of T1?  """

    def is_equal(first, second):
        """ is first tree identical to the second tree? """

        if not first and not second:
            return True

        if first and not second:
            return False

        if second and not first:
            return False

        if first.data == second.data:
            if is_equal(first.left, second.left) and is_equal(first.right, second.right):
                return True
            else:
                 return False

    if not T1:
        return False

    if T1.data == T2.data and is_equal(T1, T2):
        return True
    else:
        return is_subtree(T1.left, T2) and is_subtree(T1.right, T2)