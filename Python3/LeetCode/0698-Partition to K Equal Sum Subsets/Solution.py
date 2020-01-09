from typing import List
class Solution:
     def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
          
          nums.sort()
          target, rem = divmod(sum(nums), k)
          if rem or nums[-1] > target: return False

          def canPartition(subsets):
               # 空代表回傳可以分
               if not nums : return True

               # pop 出一個數字，試著放在各個 subset
               # subset 裡的總值 + val <= target 代表可以放
               # 若遞迴出 False，subset 裡的總值扣回 val 
               val = nums.pop()
               for index, subset in enumerate(subsets):
                    if subset + val <= target:
                         subsets[index] += val
                         if canPartition(subsets): return True
                         subsets[index] -= val
                    
                    # 若空的都不能塞，這次 partition Fail，用 break 到下面的 partition Fail 程式碼
                    # 此段判斷程式碼會大加福加速
                    if not subset : break

               # 若這次 partition Fail 要把值回來
               nums.append(val)
               return False
     
          return canPartition([0]*k)