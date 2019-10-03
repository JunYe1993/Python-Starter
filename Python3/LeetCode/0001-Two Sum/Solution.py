from typing import List

class Solution:
     def twoSum(self, nums: List[int], target: int) -> List[int]:
          map = {}                               # 紀錄對應的值 (target - 自身)
          for i in range(len(nums)):             
               if nums[i] not in map:            # 沒有對應的值則儲存
                    map[target - nums[i]] = i
               else:                             # 有對應的值則 Return
                    return map[nums[i]], i  
          return -1