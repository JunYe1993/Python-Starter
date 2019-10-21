import collections
from typing import List
class Solution:
     
     def removeStones(self, stones: List[List[int]]) -> int:
          
          # 想像用 垂直線 跟 水平線 去想辦法連接所有石頭
          # 連接了 n 個, 代表可以去掉 n -1, 看圖
                 
          # 初始樹的數目 以及 複製一個 stones 去做 DFS
          treeNum = 0
          points = {(i, j) for i, j in stones}
          
          # 建立 row 跟 col 兩個 List
          # row 紀錄該 index 下的所有有石頭的 y 座標值
          # col 紀錄該 index 下的所有有石頭的 x 座標值
          row = collections.defaultdict(list)
          col = collections.defaultdict(list)
          for i, j in stones:
               row[i].append(j)
               col[j].append(i)

          for i, j in stones:
               if (i, j) in points:
                    self.dfs(i, j, row, col, points)
                    treeNum += 1

          return len(stones) - treeNum
     
     def dfs(self, x, y, row, col, points):
          
          # 刪除這個點
          points.discard((x, y))

          # 此兩個刪除是為了加速計算
          #row[x].remove(y)
          #col[y].remove(x)

          for i in row[x]:
               if (x, i) in points:
                    self.dfs(x, i, row, col, points)

          for i in col[y]:
               if (i, y) in points:
                    self.dfs(i, y, row, col, points)

ans = Solution()
spec = [[0,0],[0,2],[1,1],[2,0],[2,2]]
print(ans.removeStones(spec))