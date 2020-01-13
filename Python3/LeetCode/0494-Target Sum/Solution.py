import collections
from typing import List
class Solution:
     def findTargetSumWays(self, nums: List[int], S: int) -> int:
          
          # 空間換取時間
          # 建立 Table 紀錄所有組合之 SUM 的出現次數
          # num = [1, 2, 3] ==> {1: 1, -1: 1} > {3: 1, 1: 2, -1: 2, -3: 1} > {6: 1, ...}
          # P.S. 可看出有規律能加判斷式去加速 
          dp = {0: 1}
          for num in nums :
               # 因為是先前的 dict 所演變(不是 + 就是 - )，先用暫存演變結果之後再取代
               tempDp = collections.defaultdict(int)
               for key, count in dp.items() :
                    tempDp[key+num] = tempDp.get(key+num, 0) + count
                    tempDp[key-num] = tempDp.get(key-num, 0) + count
               dp = tempDp.copy()
               
          return dp[S]
          