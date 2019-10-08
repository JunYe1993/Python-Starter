from typing import List
class Solution:
     def islandPerimeter(self, grid: List[List[int]]) -> int:
          perimeter = 0
          height = len(grid)
          for i in range(0, height):
               width = len(grid[i])
               for j in range(0, width):
                    if(grid[i][j] == 1):
                         if(i == 0):
                              perimeter += 1
                         elif(grid[i-1][j] == 0):
                              perimeter += 1

                         if(j == 0):
                              perimeter += 1
                         elif(grid[i][j-1] == 0):
                              perimeter += 1

                         if(i == height-1):
                              perimeter += 1
                         elif(grid[i+1][j] == 0):
                              perimeter += 1

                         if(j == width-1):
                              perimeter += 1
                         elif(grid[i][j+1] == 0):
                              perimeter += 1
          return perimeter

ans = Solution()
spec = [[0,1,0,0], [1,1,1,0], [0,1,0,0], [1,1,0,0]]
print(ans.islandPerimeter(spec))