from collections import defaultdict
from typing import List
class Solution:
     def subarraySum(self, nums: List[int], k: int) -> int:
          
          # 舉例 [1, 2, 1, 3] 找目標值 3
          # sub array sum = 0 -> 1 -> 3 -> 4 -> 7 ( 0 為初始值 )
          # 0 -> 3, 1 -> 4, 4 -> 7 所以答案為 3
          # 
          # 作法 : 
          # 做一張表去紀錄過去的和出現之個數 { 1: 1, 3: 1, 4: 1 } 
          # 若現值的和 - 目標值 : 7 - 3 在表裡則計入表裡出現之個數

          lengthOfNums = len(nums)
          sumDict = {0: 1}
          subSum = 0
          ans = 0

          for index in range(lengthOfNums):
               subSum += nums[index]
               ans += sumDict.get(subSum - k, 0)
               sumDict[subSum] = sumDict.get(subSum, 0) + 1
               
          return ans