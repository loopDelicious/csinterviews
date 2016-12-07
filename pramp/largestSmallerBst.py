# Given a root of a binary search tree and a key x, find the largest key in the tree that is smaller than x.
#
# Example: if an in-order list of all keys in the tree is {2, 3, 4, 7, 17, 19, 21, 35, 89} and x is 19, the
# biggest key that is smaller than x is 17.

def findLargestSmallerKey(root, x):

    result = None

    while root is not None:

        # if key is smaller than x
        if root.key < x:
            result = root.key
            # keep looking for a larger key
            root = root.right

        # otherwise traverse to left (to again consider if key is smaller than x)
        else:
            root = root.left

    return result

# Runtime complexity:  if the tree is balanced O(log n) because you are halving your search
# if the tree is not balanced, up to O(n) where n is depth of the tree