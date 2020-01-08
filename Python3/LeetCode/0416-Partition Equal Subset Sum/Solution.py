from typing import List

class Solution:
     def canPartition(self, nums: List[int]) -> bool:
          arraysum = 0
          for val in nums: arraysum += val
          if arraysum % 2 == 1: return False

               
          return True