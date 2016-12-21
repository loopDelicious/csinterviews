# Write the function sudokuSolve that checks whether a given sudoku board (i.e. sudoku puzzle) is solvable.
# If so, the function will returns True. Otherwise (i.e. there is no valid solution to the given sudoku board),
# returns False.
#
# In sudoku, the objective is to fill a 9x9 board with digits so that each column, each row, and each of the
# nine 3x3 sub-boards that compose the board contains all of the digits from 1 to 9. The board setter provides
# a partially completed board, which for a well-posed board has a unique solution. As explained above, for this
# problem, it suffices to calculate whether a given sudoku board has a solution. No need to return the actual
# numbers that make up a solution.
#
# A sudoku board is represented in a two dimensional 9x9 array with the numbers 1,2,...,9 and blank spaces, and
# the function should fill the blank spaces with numbers such that the following rules apply:
#
# In every row of the array, all numbers 1,2,...,9 appear exactly once.
# In every column of the array, all numbers 1,2,...,9 appear exactly once.
# In every 3x3 sub-board that is illustrated below, all numbers 1,2,...,9 appear exactly once.
# A solved sudoku is a board with no blank spaces, i.e. all blank spaces are filled with numbers that abide
# to the constraints above. If the function succeeds in solving the sudoku board, it'll return true (false, otherwise).

def sudokuSolve(board):
    """
    Input: board - a sudoku board as described in the question
    Output: True if the board is solvable """

    if (isComplete(board)):
        return True # base case for the recursion

    # get a pair: the row and column of the first empty square in board
    currentSquareIndex = getFirstEmptySquare(board)

    # If the board is full but not completed, it"s invalid
    if (currentSquareIndex == None):
        return False

    row = currentSquareIndex[0]
    col = currentSquareIndex[1]
    candidatesForCurrentSquare = getPossibleCandidates(board, row, col)

    for candidate in candidatesForCurrentSquare
        # Assume the current candidate is a good match, and keep solving
        board[row][col] = candidate
        if (sudokuSolve(board)):
            return True

        # The candidate didn"t prove to be good, let"s reset it. Since 0
        # isn’t a legal value in the board, we can use it to represent
        # an empty square on the board
        board[row][col] = 0

    return False

def isComplete(board):
    ''' Input: board - a sudoku board represented as a 9X9 2D array
    Output: True if the board is complete and legal'''

    nextEmptySquare = getFirstEmptySquare(board)
    if (nextEmptySquare != None):
        return False

    for index from 0 to 8:
        for num from 1 to 9:
            isNumberMissing = !rowContains(board, index, num) or
            !colContains(board, index, num) or
            !subBoardContains(board, index, num)

        if (isNumberMissing):
            return False

    # all numbers appear exactly once in each row, column and sub-board
    return True

def getPossibleCandidates(board, row, col):
    '''Input:
    board - a sudoku board represented as a 9X9 2D array
    row - a row on the board
    col - a column on the board
    Output:
    a subset of the numbers {1,2,...,9}, which may fill the index in the board
    without violating any of the rules described above'''

    # Build a set containing the numbers 1-9
    LEGAL_NUMBERS = new Set([1,2,3,4,5,6,7,8,9])

    numbersUsedInRow = new Set()
    numbersUsedInColumn = new Set();

    for i from 0 to 8:
        # Build a set from the row’th row in the board
        numbersUsedInRow.add(board[row][i])
        # Build a set from the col’th column in the board
        numbersUsedInColumn.add(board[i][col])

    subBoardTopLeftRow = row - (row % 3)
    subBoardTopLeftColumn = col - (col % 3)
    numbersUsedInSubBoard = new Set()

    for i from 0 to 2:
        for j from 0 to 2:
            numUsedInSubBoard = board[subBoardTopLeftRow+i][subBoardTopLeftColumn+j]
            numbersUsedInSubBoard.add(numUsedInSubBoard)

    disqualified = new Set()
    disqualified.union(numbersUsedInSubBoard, numbersUsedInRow, numbersUsedInColumn)
    validNumbersForCurrentSquare = LEGAL_NUMBERS.difference(disqualified)

    return validNumbersForCurrentSquare

def getFirstEmptySquare(board):
    '''Input: board - a sudoku board represented as a 9X9 2D array
    Output: An empty square in the board '''

    for i from 0 to 8:
        for j from 0 to 8:
            if (board[i][j] == 0): # i.e. the square is empty
                # return a a pair of indices (represented as an array of 2)
                return [i,j]

    return None

def rowContains(board, row, num):
    '''Input:
    board - a sudoku board represented as a 9X9 2D array
    row - the index of a row in the board
    num - the number we want to test for
    Output: True in num is in the index-th row of board'''

    for col in 0 to 8:
        if (board[row][col] == num):
            return True

    return False

def colContains(board, col, num):
    '''Input:
    board - a sudoku board represented as a 9X9 2D array
    col - the index of a column in the board
    num - the number we want to test for
    Output: True in num is in the index-th column of board'''

    for row in 0 to 8:
        if (board[row][col] == num):
            return True

    return False

def subBoardContains(board, subBoardIndex, num):
    '''Input: board - a sudoku board represented as a 9X9 2D array
    	subBoardIndex - the index [0-8] of a 3×3 sub-board in the board
    		The code assumes that the sub-boards are numbered from
    		left to right, top to bottom. Examples:
    		- sub-board at index 0 ranges from (0,0) to (2,2)
     		- sub-board at index 5 ranges from (3,6) to (5,8)
    num - the number we want to test for
    Output: True in num is in the index-th column of sub-board '''

    # the row of the top left position in the index-th square of the sub-board
    topLeftPositionRow = subBoardIndex - (subBoardIndex % 3)

    # the column of the top left position in the index-th square of the sub-board
    topLeftPositionCol = 3 * (subBoardIndex % 3)

    for i in 0 to 2:
        for j in 0 to 2:
            if (board[topLeftPositionRow + i][topLeftPositionCol + j] == num):
                return True

    return False


# replace the function getFirstEmptySquare in sudokuSolve with the following function:
def getLeastNumOfCandidatesIndex(board):
    '''Input: board - a sudoku board represented as a 9X9 2D array
    Output: Index of a blank square with the least number of
    candidates possible (possibly none)'''

    minIndex = None
    minNumOfCandidates = MAX_INT

    for i from 0 to 8:
        for j from 0 to 8:
            numOfCurrentCandidates = size(getPossibleCandidates(i,j))
            if ((board[i][j] == 0) and (numOfCurrentCandidaes < minNumOfCandidates)):
                minIndex = [i,j]
            numOfMinCandidates = numOfCurrentCandidaes

    return minIndex