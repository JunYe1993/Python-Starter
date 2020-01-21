from typing import List
class Solution:
     def maxDistance(self, grid: List[List[int]]) -> int:
          
          # BFS
          N = len(grid)
          dist = [[0] * N for _ in range(N)]            
          landPoints = [(i, j) for i in range(N) for j in range(N) if grid[i][j] == 1]
          
          # 題目要求回傳 -1
          if len(landPoints) == N*N or len(landPoints) == 0 : return -1

          for x, y in landPoints:
               dist[x][y] = 1

          maxDict = 0
          while landPoints:
               # print(landPoints)
               curLayerLandPoints = landPoints.copy()
               landPoints = []

               isNextLayerExist = False
               for i, j in curLayerLandPoints :  
                    for x, y in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                         # 查 dist 若有值( > 0 ) 等於是上一層
                         if x >= 0 and x < N and y >= 0 and y < N and not dist[x][y] : 
                              dist[x][y] = dist[i][j] + 1
                              landPoints.append((x, y))
                              isNextLayerExist = True
               
               if isNextLayerExist : maxDict += 1

          return maxDict