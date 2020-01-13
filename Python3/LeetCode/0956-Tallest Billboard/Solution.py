from typing import List
import collections

class Solution:

     def tallestBillboard(self, rods: List[int]) -> int:
          
          # 空間換取時間 0494 為前導題
          # 建立 Table 紀錄所有"差" 之 的最大值
          # 相較於 0494 有三種 (1) 放左邊柱子 (2) 放右邊柱子 (3) 不放
          # 放左右邊柱子並不是我們想要的，改成 (1) 將"差"擴大的 (2) 將"差"縮小的的 (3) 不放
          dp = {0: 0}
          for rod in rods :

               # 不同於 0494 從舊的演變，這裡就得保留(因為有不放)所以直接複製 
               tempDp = dp.copy()
               for key, value in dp.items() :
                    
                    # 新增差異擴大的
                    tempDp[key+rod] = max(tempDp.get(key+rod, 0), value)

                    # 新增差異縮小的
                    # value + min(rod, key) 為取小值 (3, 6) 取 3, 下個補 3 就會是 3 + 3 = 6 
                    diff = abs(key-rod)
                    tempDp[diff] = max(tempDp.get(diff, 0), value + min(rod, key))

               dp = tempDp
               print(dp)
               
          return dp[0]