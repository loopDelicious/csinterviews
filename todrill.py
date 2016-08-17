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

def pramp():
   print "Practice Makes Perfect"

pramp()

arr =  [2, 7, 3, 4]
res =  [7*3*4, 2*3*4, 2*7*4, 2*7*3]

def products(arr):
   
    results = []
    for i in range(len(arr)):
        product = 1
        for j in range(len(arr)):
            if i == j:
                continue
            product *= arr[j]
        results.append(product)
    return results
     

arr = [0, 3, 4]
i == 1

left = []
left[0] = 1
#general forumula
left[i] = left[i-1]*arr[i-1]

Refael/Rafi
rafi@pramp.com

product = 3

product = product*5

def products2(arr):
   left = [1]
   for i in range(1,len(arr)):
      left[i] = left[i-1]*arr[i-1]

   right = [1] * len(arr)   
   for i in range(len(arr)-1,-1,-1):
      right[i] = right[i+1]*arr[i+1]
   
   #result = []
   for i in range(len(arr)):
      left[i] = left[i]*right[i]
      #result.append(left[i]*right[i])
   return left

# Given a package with a weight limit and an array arr of item weights, 
# how can you most efficiently find two items with sum of weights that equals the weight limit?
# Your function should return 2 such indices of item weights or -1 if such pair doesn't exist.
# What is the runtime and space complexity of your solution?
# in: limit, arr
# out: 2 indices
def find_two(limit, arr):  # O(n^2) nested for loops
    for i, item in enumerate(arr):
        for j, item2 in enumerate(arr):
            if item + item2 == limit:
                return [i,j]
    return -1
def find_two2(limit, arr): # O(n) create dict, and loop through arr to find complementary weight
    weight_dict = {weight: index for index, weight in enumerate(arr)}
    for i, w in enumerate(arr):
        if limit-w in weight_dict:
            return i, weight_dict[limit-w]
    return -1
    # alternative way to create dict
    weight_dict = {}
    for i, w in enumerate(arr):
        if w in weight_dict:
            continue
        else:
            weight_dict[w] = i
    # but wait, we don't want to hash the weight before checking if the complement exists (could pick the same weight)
    weight_dict = {}
    for i, w in enumerate(arr):
        if limit - w in weight_dict:
            return i, weight_dict[limit-w]
        else:
            weight_dict[w] = i
    return -1

# chicken wings (word_positions) keep 2 pointers of indices in each array
word_positions = {
    "chicken": [29, 35, 46, 59, 67, 99],
    "wings": [30, 47, 78, 100],
}
def find_phrase(word_positions):
    """given a dictionary of words and their positions in a corpus, return occurrences of "chicken wings"""
    
    chicken = word_positions[chicken]
    wings = word_positions[wings]

    results = []

    # O(n^2) runtime O(n*m)
    # for integer in chicken:
    #     if integer + 1 in wings:
    #         results.append(integer)
    index = 0
    while index < len(chicken):
        if chicken[index] == wings[index] + 1:
            results.append(chicken[index])
        if
    

# find 3 numbers that sum to 0, return True (use set of seen, set of sum) - Kara github study hall
# find 3 numbers with the highest product
# keep track of things you've seen from the array so you don't have to loop through again (save runtime)

# model a pinball machine - keep track of 10 highest scores, data types, data model, one to many and many to many, association tables
# data algorithms in binary heaps
# is_bst = is a binary tree a binary search tree
# coins
# spiral print a matrix
# rabbit eating carrots on a matrix, max number of carrots, and only stepping on places that have carrots (asana)

def pramp():
   print "Practice Makes Perfect"

pramp()

# In: { time: 1440084737,  count: 5,  type: "enter" }
# In: { time: 1440084737,  count: -4,  type: "exit" }
# In: { time: 1440084738,  count: 3,  type: "enter" }
#[ In: { time: 1440084738,  count: -2,  type: "exit" }]
# Out: [1440084737, 1440084738]

# if the max count is in the last second:
# # Out: [1440084738, 1440084738]

# sort array (by time) 
# initialize population variable that incr enter and decr exit
# iterate over sorted array: 
# if population at current time > curr_pop, update var

def busy(arr):
   """ determine the second of maximum population in the mall. """
   
   sorted(arr)
   
   population = 0
   max_population = 0
   time_stamp = arr[0][0]
   
   for i, timeslot in enumerate(arr):
      
      if arr[i][2] == "enter":
          population += arr[i][1]
      else:
         population -= arr[i][1]
      if population > max_population:
         max_population = population
         time_stamp = arr[i][0]
         
   return [time_stamp, time_stamp + 1]
      



   [(time: x, count: y, type: z),...]
   
   
   
#    know timsort complexity

# [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ', 'm', 'a', 'k', 'e', 's', '  ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]
# [ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ', 'm', 'a', 'k', 'e', 's', '  ', 'p', 'e', 'r', 'f', 'e', 'c', 't' ]
# ['practice', ...]

Language:Python
End Interview

def sentence_reverse(arr):
   """ reverse the words, separated by space """
   
   word = ""
   new_arr = []
   #curr_index = range(len(arr))
   #start_index = range(len(arr))
   
   
   for i, char in range(len(arr)-1, 0, -1):
      if char != " ":
         word += char
      else:
         word = reverse(word)
         if curr_index > 0:
            word += " "
         new_arr.append(word)
   return new_arr



# def reverseWord():
#    while word[start_index] != " ":
#          start_index -= 1      
#       new_arr.append(word[start_index+1:curr_index])   


