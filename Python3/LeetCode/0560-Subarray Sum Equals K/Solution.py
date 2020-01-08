from collections import defaultdict
from typing import List
class Solution:
     def subarraySum(self, nums: List[int], k: int) -> int:
          # print()
          lengthOfNums = len(nums)
          sumDict = {0: 1}
          subSum = 0
          ans = 0

          for index in range(lengthOfNums):
               # print("before :", sumDict)
               subSum += nums[index]
               ans += sumDict.get(subSum - k, 0)
               sumDict[subSum] = sumDict.get(subSum, 0) + 1
               # print("after  :", sumDict)

          return ans