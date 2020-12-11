from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do some elimination like normal human do Sudoku.
        """
        # Create a double array which element is a set of {1~9}
        possible_values = []
        for i in range(9):
            possible_values.append([])
            for j in range(9): 
                possible_values[i].append(set('123456789'))
        # After elimination, it may come out some right answer for the cell on the board
        # Record them for updating board next time
        nextupdate = []

        # Loop through the board.
        for rowIndex in range(9):
            for colIndex in range(9):
                digit = board[rowIndex][colIndex]
                # If cell value is digit, then do some possible value elimination
                if digit != ".":
                    # The cell have number filled in, so possibility is none
                    possible_values[rowIndex][colIndex].clear()

                    # Eliminate possible value with Sudoku rule.
                    self.eliminateRowPossibleValue(digit, board, possible_values, rowIndex, nextupdate)
                    self.eliminateColPossibleValue(digit, board, possible_values, colIndex, nextupdate)
                    self.eliminateSubBoxPossibleValue(digit, board, possible_values, rowIndex, colIndex, nextupdate)
        
        # It would be new elimination after update the value in nextupdate[]
        for rowIndex, colIndex in nextupdate:
            # update board and do possible value elimination
            # note : when loop the element in nextupdate[], 
            # the elimination function below append new element, and its good for this condition.
            # because statement "for rowIndex, colIndex in nextupdate:" will go through all them
            digit = board[rowIndex][colIndex]
            self.eliminateRowPossibleValue(digit, board, possible_values, rowIndex, nextupdate)
            self.eliminateColPossibleValue(digit, board, possible_values, colIndex, nextupdate)
            self.eliminateSubBoxPossibleValue(digit, board, possible_values, rowIndex, colIndex, nextupdate)
        
        """
        Backtracking like computer do Sudoku
        """
        self.backtracking(board, possible_values)

    # Eliminate possible value with rule "1-9 digit only occur once in a row"
    def eliminateRowPossibleValue(self, digit, board, possible_values, rowIndex, nextupdate):
        # Loop through all the column in a row
        for colIndex in range(9):
            # Eliminate possible value if it is in possible_values set
            if digit in possible_values[rowIndex][colIndex]:    
                possible_values[rowIndex][colIndex].remove(digit)
                # If number of possible values is one, then fill the number on the board. 
                if len(possible_values[rowIndex][colIndex]) == 1:
                    board[rowIndex][colIndex] = possible_values[rowIndex][colIndex].pop()
                    # New update will cause new possible value elemination, so record it
                    nextupdate.append([rowIndex, colIndex])
                
    # Eliminate possible value with rule "1-9 digit only occur once in a column"
    def eliminateColPossibleValue(self, digit, board, possible_values, colIndex, nextupdate):
        for rowIndex in range(9):
            if digit in possible_values[rowIndex][colIndex]:
                possible_values[rowIndex][colIndex].remove(digit)
                if len(possible_values[rowIndex][colIndex]) == 1:
                    board[rowIndex][colIndex] = possible_values[rowIndex][colIndex].pop()
                    nextupdate.append([rowIndex, colIndex])

    # Eliminate possible value with rule "1-9 digit only occur once in a 3x3 sub box"
    def eliminateSubBoxPossibleValue(self, digit, board, possible_values, rowIndex, colIndex, nextupdate):
        rowIndexOffset = (rowIndex // 3) * 3
        colIndexOffset = (colIndex // 3) * 3
        for subBoxRowIndex in range(3):
            for subBoxColIndex in range(3):
                rIndex = subBoxRowIndex + rowIndexOffset
                cIndex = subBoxColIndex + colIndexOffset
                if digit in possible_values[rIndex][cIndex]:
                    possible_values[rIndex][cIndex].remove(digit)
                    if len(possible_values[rIndex][cIndex]) == 1:
                        board[rIndex][cIndex] = possible_values[rIndex][cIndex].pop()
                        nextupdate.append([rIndex, cIndex])

    def backtracking(self, board, possible_values):
        for rowIndex in range(9):
            for colIndex in range(9):
                if board[rowIndex][colIndex] == ".":
                    for num in range(1, 10):
                        fillNum = str(num)
                        if fillNum in possible_values[rowIndex][colIndex]:
                            if self.isValid(board, rowIndex, colIndex, fillNum):
                                board[rowIndex][colIndex] = fillNum
                                if (self.backtracking(board, possible_values)):
                                    return True
                                board[rowIndex][colIndex] = "."
                    return False   # Previous fillNum is wrong cause there is no valid num to fill in.
        return True   # No more "." in board so it is solved.

    def isValid(self, board, rowIndex, colIndex, fillNum) -> bool:
        for cIndex in range(9):
            if board[rowIndex][cIndex] == fillNum:
                return False
        for rIndex in range(9):
            if board[rIndex][colIndex] == fillNum:
                return False
        for rIndex in range(3):
            for cIndex in range(3):
                r = rIndex + (rowIndex//3)*3
                c = cIndex + (colIndex//3)*3
                if board[r][c] == fillNum:
                    return False
        return True