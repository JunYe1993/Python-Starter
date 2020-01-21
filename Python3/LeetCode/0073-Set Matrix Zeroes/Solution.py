from typing import List

class Solution:
     def setZeroes(self, matrix: List[List[int]]) -> None:
          
          """
          Do not return anything, modify matrix in-place instead.
          """
          # print()
          if not matrix : return
          rowCount = len(matrix)
          colCount = len(matrix[-1])

          colSet = set()
          for row in range(rowCount) : 
               
               colZero = True
               rowZero = False
               for col in range(colCount) :
                    
                    if matrix[row][col] == 0 : 
                         rowZero = True
                         if col not in colSet:
                              colZero = False
                              colSet.add(col)
                              for allRow in range(row+1) :
                                   matrix[allRow][col] = 0

                    if colZero and col in colSet:
                         matrix[row][col] = 0

               if rowZero :
                    matrix[row] = [0]*colCount
