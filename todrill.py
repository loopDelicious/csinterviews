####################################################
#### Trees
# height of binary tree recursively
def height(node):
    if not node:
        return 0
    left = height(node.left)
    right = height(node.right)
    return max(left, right) + 1
# create a list of all nodes at each depth of a tree
def list_nodes(node):
    if not node:
        return 
    node_list = []
    return node_list + list_nodes(node.right) + list_nodes(node.left)

# check subtree, if subtree is in bigger tree
def is_equal(first, second):
    if not first and not second:
        return True
    if first and not second:
        return False
    if second and not first:
        return False
    if first.data == second.data:
        if is_equal(first.right, second.right) and is_equal(first.left, second.left):
            return True
        else:
            return False
def check_subtree(bigger, smaller):
    if not bigger:
        return False
    if bigger.data == smaller.data and is_equal(bigger, smaller):
        return True
    else:
        return check_subtree(bigger.right, smaller) and check_subtree(bigger.left, smaller)

####################################################
#### Linked Lists
# reverse a linked list
def rev_ll(node):
    out_head = None
    n = node
    while n:
        out_head = Node(n.data, out_head)
        n = n.next
    return out_head

# reverse a linked list in place
def rev_ll_in_place(node):
    previous = None
    current = node.head
    while current:
        next = current.next # set placeholder for next
        current.next = previous # turn pointer backwards
        previous = current
        current = next
    node.head = previous

# remove node from linked list
def remove(node):
    node.data = node.next.data
    node.next = node.next.next

####################################################
#### Recursion
# Fibonacci(n)
def Fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return Fib(n-1) + Fib(n-2)
# multiplier w/o using multiplication
def multiply(x,y):
    if x == 0:
        return 0
    return multiply(x-1, y) + y

####################################################
#### General
# is_balanced for () (stack)
# is_balanced for (),[],{}


# draw H-tree
# given center x,y
# drawLine takes ((x1,y1),(x2,y2))
# Runtime:  O(4^n)
# Space: O(d)
def h_tree(x,y,starting_length,depth):

    if depth == 0:
        return

    halfway = starting_length / 2

    upper_left = (x - halfway, y + halfway)
    lower_left = (x - halfway, y - halfway)
    upper_right = (x + halfway, y + halfway)
    lower_right = (x + halfway, y - halfway)
    center_left = (x - halfway, y)
    center_right = (x + halfway, y)

    drawLine(center_left, center_right) # center
    drawLine(upper_left, lower_left) # left
    drawLine(upper_right, lower_right) # right

    h_tree(upper_left, starting_length, depth - 1) 
    h_tree(upper_right, starting_length, depth - 1)
    h_tree(lower_right, starting_length, depth - 1)
    h_tree(lower_left, starting_length, depth - 1)

# find i where index is equal to the value at that index, otherwise return -1
# [-8,0,2,8] arr
#  0, 1,2,3  index
def binary_search(arr):

    guess_index = None
    lowest_index = 0
    highest_index = len(arr) - 1

    while arr[guess] != guess_index:
        guess_index = (highest_index - lowest_index) / 2 + lowest_index
        if arr[guess_index] < guess_index:
            lowest_index = guess_index
        elif arr[guess_index] > guess_index:
            highest_index = guess_index
        else:
            return guess_index
    return -1

# Nim game https://leetcode.com/problems/nim-game/
def canWinGame(stones):
    if stones % 4 == 0:
        return False
    return True
    # return !(stones % 4 == 0) 
    # if your opponent can be left with 4, you win!
# count number of islands in world (array of arrays)
def num_islands(world):
    """ Islands are land surrounded on ordinal sides by water.

        [
            [O,X,O,O,O],
            [O,O,X,O,O],
            [O,O,X,X,O],
            [O,O,O,O,O]
        ]
        Solution:  2 islands

    """

    land = "X"
    water = "O"
    # first tile is expressed as world[0][0]
    # world[i][j]
    i = 0  # index of array in master array (which row)
    j = 0  # index of slot in each array (which column)
    # last tile is expressed as world[3][4]

    num_islands = 0

    while j < len(world[i]):
        if tile == water:
            continue
        else:
            work_surround(world[i][j])
 # increment indices

    def work_surround(tile):
        """ check tiles surrounding input land tile for more land.
        if land, turn to water."""

        if world[]


# invert binary tree
    def invert_binary(self,root):
        if root is not None:
            temp = root.left
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(temp)
        return root
# Xinran's questions: Round 2:
# find 3 numbers in an unsorted array that sum to S
def find_three1(arr, S): # O(n^3)

    for i, val1 in enumerate(arr):
        for j, val2 in enumerate(arr[1:]):
            for k, val3 in enumerate(arr[2:]):
                if arr[i] + arr[j] + arr[k] == S:
                    return [arr[i], arr[j], arr[k]]
    return "no numbers sum to " + S
def find_three2(arr, S): 
    for i, val1 in enumerate(arr):
        for j, val2 in enumerate(arr[1:]):
            if S - 

# given matrix of sorted rows and columns, find kth smallest
def kth_smallest(matrix, k):

# output all possibilities that sum to 100 using [+,-,nothing] and single digit integers [1-9]
def sum_to_100():

