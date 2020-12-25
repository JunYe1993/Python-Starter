from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        length = len(nums)
        minDiff = 1000000

        for i in range(length):
            if i > 0 and nums[i] == nums[i-1]: continue
            subtarget = target - nums[i]
            j, k = i+1, length - 1
            while j < k:
                subSum = nums[j] + nums[k]
                diff = subSum - subtarget
                minDiff = nums[i]+subSum if abs(minDiff-target) > abs(diff) else minDiff
                if minDiff == target: return minDiff
                elif diff > 0: k-=1
                elif diff < 0: j+=1
                
        return minDiff