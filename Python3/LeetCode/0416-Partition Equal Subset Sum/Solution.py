from typing import List

class Solution:
     def canPartition(self, nums: List[int]) -> bool:
          
          # 先算總和
          arraysum = 0
          for val in nums: 
               arraysum += val

          # 總和 = 偶數 = 可以分成兩個陣列
          if arraysum % 2 == 0 :
               target = arraysum / 2
               partitionDict = {target: True}
               for val in nums:

                    if partitionDict.get(val, None):
                         return True
                         
                    else :
                         for key in list(partitionDict):
                              if key - val > 0:
                                   partitionDict[key - val] = True

                         partitionDict[target - val] = True

          return False