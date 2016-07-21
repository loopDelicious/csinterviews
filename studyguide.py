
# print every item in a list recursively  
def print_recursive(list):
    if list is not None:
        return 0
    print list[0]
    print_recusive(list[1:])
    
# is 1 string an anagram of another string?   
# 1) create a dictionary of each string (key is character, value is occurrences), compare if dictionaries are equivalent - O(n)
def is_anagram(str1, str2):
    str1dict = {}
    str2dict = {}
    for letter in str1:
        if str1dict[letter]:
            str1dict[letter] += 1
        else:
            str1dict[letter] = 1
    ....for str2dict
    if str1dict == str2dict:
        return True

# 2) sort each string and compare if equivalent - ?"

# find the depth of a binary tree?    
# recursion, find max of node.left and node.right - O(2n) -> O(n)
def find_height(node):
    if node.left is not None and node.right is not None:
        return 1
    return max(find_height(node.left), find_height(node.right)) + 1

# is a linked list a palindrome?  
# 1) keep track of head and end and incr/dec towards the center - O(n)
Start = ll.head
while ll.head.next is not None:
    End = ll.head
    ll.head = ll.head.next

# is string a palindrome? 

# Suppose we could access yesterday's stock prices as a list, where:
    # The indices are the time in minutes past trade opening time, which was 9:30am local time.
    # The values are the price in dollars of Apple stock at that time.
    # So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.
# Write an efficient function that takes stock_prices_yesterday and returns the best profit I could have made 
# from 1 purchase and 1 sale of 1 Apple stock yesterday.

def max_profit(stock_prices_yesterday):
    """Calculates maximum profit from trading yesterday."""

    buy = stock_prices_yesterday[0]
    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]

    for index, current_price in enumerate(stock_prices_yesterday[1:]):
        
        potential_profit = current_price - buy
        max_profit = max(max_profit, potential_profit)

        buy = min(buy, current_price)

    return max_profit

# how does your app work in terms of response and request?    

# phone screen - order a string by words and number of occurrences    create a dictionary of {word: num_occurrences}, dicts are unordered, so convert to a list of tuples and sort by 2nd element of each tuple

# Traversing a tree   "stacks (depth first), queues (breadth first)
# using a class to init the traversal (vs. doing it every time function is called)
# find an item in a tree recursively"

# Take in a list of integers, and create a new list where x < y > b in a repeating pattern
# circular buffer, ring buffer using linked list to save time with fixed bounds to save memory
# parse a string like "1+1+1-3" to execute function?  by using priority queue of integer and priority queue of operands,
# order of operations fo * and / should be executed immediately
# sudoku with list of lists (1-9)

# Is a node in a graph cyclical   will you find yourself again

# InterviewCake:  You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.
def get_products_of_all_ints_except_at_index(list):
    results = []
    for i, num in enumerate(list):
        popped = list.pop(i)
        new_num = 1
        for num in list:
            new_num *= num
        results.append(new_num)
        list.insert(i, popped)
    return results

# O(n^2) - nested for loops
# O(n) solution to keep track of product before int, and product after int

# InterviewCake: Given a list_of_ints, find the highest_product you can get from three of the integers.
def highest_product(list_of_ints):
    results = 1
    new_list = sorted(list_of_ints, reverse=True)
    for num in new_list[0:3]:
        results *= num
    return results

# Cracking Ch1.1: implement algo to find out if a string has all unique characters, what if you can't use add'l data structures?
# O(n)
def all_unique(str):
    str_dict = {}
    for char in str:
        if str_dict[char]:
            return False
        else:
            str_dict[char] = 1
    return True
# w/o add'l data structures - O(n^2)
def all_unique2(str):
    for char in str:
        if str.count(char) > 1:
            return False
    return True

# Cracking Ch1.2: given 2 strings, write a method to decide if one is a permutation of the other
# O(n)
# check character counts of both strings
def is_anagram(str1, str2):
    str1_dict = {}
    str2_dict = {}
    for letter in str1:
        if str1_dict[letter]:
            str1_dict[letter] += 1
        else:
            str1_dict[letter] = 1
    for letter in str2:
        if str2_dict[letter]:
            str2_dict[letter] +=1
        else:
            str2_dict[letter] = 1
    if str1_dict == str2_dict:
        return True
    else:
        return False
# sort both strings
# timsort is O(nlogn)
def is_anagram2(str1, str2):
    str1.sort()
    str2.sort()
    if str1 == str2:
        return True
    else:
        return False

# Cracking Ch1.3:  replace all spaces in a string with '%20'
def replacer(my_string):
    my_string.replace(' ', '%20')
def replacer2(my_string):
    new_string = ""
    for char in my_string:
        if char == ' ':
            new_string += '%20'
        else:
            new_string += char
    return new_string

# Cracking Ch1.4:  given a string, is it a permutation of a palindrome
# create a hash table with char counts and make sure no more than 1 char has an odd count
# O(n) where n is the length of the string
def is_pal_perm(my_string):
    char_dict = {}
    for char in my_string:
        if char_dict[char]:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    odds = []
    for key in char_dict:
        if len(odds) > 1:
            return False
        if char_dict[key] % 2 == 0:
            continue
        else:
            odds.append(char_dict[key])
    return True
def is_pal_perm2(my_string):
    odds = []
    for char in my_string:
        if len(odds) > 1:
            return False
        if my_string.count(char) % 2 == 0:
            continue
        else:
            odds.append(char)

# Cracking Ch1.5:  assuming 3 types of string edits (insert, remove, replace), given 2 strings, are they one-edit away
# FIXME - MUCH HARD
# def is_one_away(str1, str2):
    if str1 == str2:
        return True
    if len(str1) < len(str2)

# DemandForce:
# Problem 5: It is not necessary to actually generate any of the possible palindromes if there are any. 
# You only need to determine whether it is possible. Think through what the requirements are to generate a palindrome and 
# make sure they are available in the input string

# Problem 6: Try generating the output in a straightforward way, then test your algorithm on sequentially increasing numbers 
# to see if you can detect a pattern that can be used for a more efficient solution

# Problem 7: Pay attention to the constraints on this problem. Knowing the values will always be in a small enough range 
# will often let you trade memory for execution speed

# Problem 8: While the examples show the work by saving discount amounts, these aren't necessary for solving the problem. 
# You only need to return a single total and a list of the undiscounted indexes

# Problem 9: There is both a naive O(n^2) and efficient O(n) solution to this problem. If you can't think of the O(n) 
# solution quickly, try to implement the O(n^2) solution to get partial credit and move on to other problems

# Problem 10: In order to interpolate between prices and quantities, you can think of price and quantity as an x and y 
# coordinate on a graph. Since you are interpolating based on two points, you can find an equation of the line between 
# them in the form of y = mx + b by first finding m with the equation (y2 - y1) / (x2 - x1), then plugging either of those 
# points to find b. Finally, plug the new value you are looking for into x to get the interpolated y. This problem is still 
# difficult even with that hint. Make sure to read the instructions carefully to handle all the potential cases. 

# Yahoo whiteboarding:  Fibonaci number at nth index
# [0,1,1,2,3,5,8,13,21] at index
# Recursively
def Fib(n):
    """Given a positive integer, find the Fibonacci number at nth index."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return Fib(n-1) + Fib(n-2)

# Iteratively
def Fib1(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    i = 1
    n1 = 0
    n2 = 1
    while i <= n:
        current = n1 + n2
        n1 = n2
        n2 = current
        i++
    return current

# parenthesis is balanced checker
def is_balanced(my_string):
    index = 0
    balanced = True
    s = Stack()
    for index, item in enumerate(my_string):
        if item == "(":
            s.push(item)
        else:
            if s.isEmpty():
                balanced =False
            else:
                s.pop(item)
    if balanced and s.isEmpty():
        return True
    else:
        False

# symbol balanced checker
def is_balanced(my_string):
    index = 0
    balanced = True
    s = Stack()
    opens = ['(', '[', '{']
    closes = [')', ']', '}']
    for index, item in enumerate(my_string):
        if item in opens:
            s.push(item)
        else:
            if s.isEmpty():
                balanced = False
            if item == ')':
                opener = '('
            if item == ']':
                opener = '['
            if item == '}':
                opener = '{'
            if closes.index[item] == opens.index[opener]
                balanced = True
                s.pop()
    if balanced and s.isEmpty():
        return True
    else:
        return False

# implement Stack, Queue, Deque
# init, isEmpty, size, push, pop, peek, enqueue, dequeue, removeFront, removeRear, addFront, addRear
class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
class Queue:
    def __init__(self):
        self.items = []
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
class Deque:
    def __init__(self):
        self.items = []
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.items == []
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
    def addFront(self, item):
        self.items.append(item)
    def addRear(self, item):
        self.items.insert(0, item)
# implement unordered list (linked list)
# add(item), remove(item), search(item), append(item), index(item), insert(pos, item), pop(), pop(pos), size, isEmpty
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class UnorderedList:
    def __init__(self):
        self.head = None
    def size(self):
        counter = 0
        current = self.head
        while current != None:
            counter += 1
            current = current.next
        return counter
    def add(self, item): # O(n)
        temp = Node(item)
        temp.next = self.head
        self.head = temp
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.data == item:
                found = True
            else:
                current = current.next
        return found
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.next
        if previous == None:
            # if item to be removed is the first item in the list
            self.head = current.next
        else:
            previous.next = current.next
# recursive sum of a list of numbers
def listSum(list):
    if len(list) == 1:
        return list[0]
    return list[0] + listSum(list[1:])
# recurisve factorial of a number
def fact(n):
    if n <= 1:  # n == 0 would work too, but ending at n == 1 is more efficient and still need to account for fact(0)
        return 1
    return n * fact(n-1)
# sequential search for an item in a list
def search(my_list, item):
    return item in my_list
def search2(my_list, item):
    found = False
    for thing in my_list:
        if thing == item:
            found = True
    return found
# binary search for an item in a list
def bin_search(my_list, item):
    found = False
    first = 0
    last = len(my_list)-1
    midpoint = (first + last) / 2
    if item == my_list[midpoint]:
        found = True
    else:
        if item > my_list[midpoint]:
            first = midpoint + 1 # item is not the midpoint, lop off the left side of the list
        else:
            last = midpoint - 1
    return found
# recursive binary search for an item in a list
def bin_search2(my_list, item):
    if len(my_list) == 0:
        return False
    midpoint = len(my_list) / 2
    if my_list[midpoint] == item:
        return True
    if my_list[midpoint] > item:
        return bin_search2(my_list[:midpoint], item)
    else:
        return bin_search2(my_list[midpoint:], item)
# bubble sort O(n^2), but swaps everytime there's an exchange possibility, each pass bubbles the largest item to the top
def bubble(my_list):
    for passnum in range(len(my_list)-1, 0, -1): #passnum = index position? traversing backwards
        for i in range(passnum):
            if item[i] > item[i+1]:
                temp = item[i]
                item[i] = item[i+1]
                item[i+1] = temp
# selection sort O(n^2), like bubble but makes fewer swaps, on each pass the largest item is selected and placed at the end
def selection(my_list):
# insertion sort O(n^2), works at the start of a list and each pass creates a slightly longer sorted list
#  merge sort, recusively breaks the list in half until single item sorted list
def merge(my_list):
    if my_list <= 1:
        return my_list
    if len(my_list) > 1:
        mid = len(my_list) / 2
        left = my_list[:mid]
        right = my_list[mid:]
        merge(left)
        merge(right)
        ...
# quick sort uses pivot value and split point
# Find the height of a binary tree recurisvely
def height(n):
    if not n:
        return 0
    return max(height(n.left), height(n.right)) + 1
# Create a list of all nodes at each depth
def list_all(n):
    if not n:
        return
    node_list = []
    print node_list + list_all(n.left) + list_all(n.right)
# Check subtree, if subtree is in bigger tree
def is_equal(first, second):
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
def is_subtree(big, small):
    if not n:
        return False
    if big.data == small.data and is_equal(big, small):
        return True
    else:
        return is_subtree(big.left, small) and is_subtree(big.right, small)
# Fibonacci of nth integer
def Fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return Fib(n-1) + Fib(n-2)
# Edit distance: find out if str is 1 edit away from another string
def edit_one(str1, str2):
    if len(str1) == len(str2):
        # same string
        if str1 == str2:
            return False
        # replacement
        replacements = 0
        for i, char in enumerate(str1):
            if char == str2[i]:
                continue
            else:
                replacements += 1
            if replacements > 1:
                return False
        return True
    # add is the same as delete, easiest to delete at every index from longer str and compare equality
    elif len(str1) == len(str2) + 1:
        for i,char in enumerate(str2):
            str2.pop(i)
            if str1 == str2:
                return True
            else:
                str2.insert(i, char)
    elif len(str1) + 1 == len(str2):
        for i,char in enumerate(str1):
            str1.pop(i)
            if str1 == str2:
                return True
            else:
                str1.insert(i, char)
    else:
        return False
# given 2 numbers, provide the product but can't use multiplication
def multiply(x, y):
    if y <= 0:
        return 0
    return x + multiply(x, y-1)
# given 2 numbers, exponentiation
def exponent(x, y):
    if y <= 0
        return 0
    return x * exponent(x, y-1)
# determine if a string contains balanced parenthesis
def is_balanced(str1):
    stack = []
    for i,char in enumerate(str1):
        if char == "(":
            stack.push(str1.pop())
        elif char == ")" and stack == []:
            return False
        elif char == ")" and stack != []:
            stack.pop()
    return True
# determine how many islands are in the world, nested arrays
def check_surrounds(block):
    if 

def count_islands(array):
    for block in array:
        if block == land:

# check subtree
def is_equal(first, second):

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
def is_subtree(bigger, smaller):

    if not bigger:
        return False
    if bigger.data == smaller.data and is_equal(bigger, smaller):
        return True
    else:
        return is_subtree(bigger.left, smaller) and is_subtree(bigger.right, smaller)
# create a list of all the nodes at each depth
def list_nodes(node):
    if not node:
        return
    node_list = []
    return node_list + list_nodes(node.left) + list_nodes(node.right)
# find the height of a binary tree recursively
def height(node):
    if not node:
        return 0
    return max(height(node.left), height(node.right)) + 1



