from typing import List

class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # 一一檢視 Sudoku valid 的條件
        
        # Each of the digits 1-9 must occur exactly once in each row.
        # Loop through all the row in the board, and valid every cell in the row with set().
        for rowIndex in range(9):  # Loop rows
            rowExistNum = set()  # Create set() to valid the digit only occur once.
            for colIndex in range(9):  # Loop column to check every cell in the row.
                if board[rowIndex][colIndex] == ".":  # if cell value is dot then ignore this cell
                    continue           
                elif board[rowIndex][colIndex] in rowExistNum:  # if cell value is already in the set, digit occur more than once, then return false.
                    return False       
                else:
                    rowExistNum.add(board[rowIndex][colIndex])  # if cell value not in the set, then set add this digit and go on.
        
        # Each of the digits 1-9 must occur exactly once in each column.
        # Loop through all the column in the board, and valid every cell in the column with set().
        for colIndex in range(9):  # Loop column
            colExistNum = set()  # Create set() to valid the digit only occur once.
            for rowIndex in range(9):  # Loop row to check every cell in the column.
                if board[rowIndex][colIndex] == ".":  # if cell value is dot then ignore this cell
                    continue
                elif board[rowIndex][colIndex] in colExistNum:  # if cell value is already in the set, digit occur more than once, then return false.
                    return False
                else:
                    colExistNum.add(board[rowIndex][colIndex])  # if cell value not in the set, then set add this digit and go on.
        
        # Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
        # Loop through all the 3x3 sub-boxes, and valid evry cell in the sub-boxes with set()
        for subBox in range(9):
            row_offset = (subBox // 3) * 3  # Calculate the row offset for every sub-box
            col_offset = (subBox %  3) * 3  # Calculate the col offset for every sub-box
            subBoxExistNum = set()  # Create set() to valid the digit only occur once.
            for rowIndex in range(3):  # Loop row in the sub-box
                for colIndex in range(3):  # Loop col in the sub-box
                    cellNum = board[rowIndex+row_offset][colIndex+col_offset]  # Get cell value.
                    if cellNum == ".":  # if cell value is dot, then ignore
                        continue
                    elif cellNum in subBoxExistNum:  # if cell value is already in the set, then digit occur more than once so return false.
                        return False
                    else:
                        subBoxExistNum.add(cellNum)  # if cell value is not in the set, then set add this value and go on.

        # if board go through three validing loops above and do not return. then board is valid sudoku.
        return True