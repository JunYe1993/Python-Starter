from typing import List

class Solution:

    # runtime: 140ms, basically is the same aglorithm with function below
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        length = len(nums)
        answer = []

        # Add extra two condition statement
        # Main idea is taking advantage of sorted array
        for i in range(length):
            if i > 0 and nums[i] == nums[i-1]: continue
            for j in range(i+1, length):
                if j > i+1 and nums[j] == nums[j-1]: continue

                # After picking two numbers then the rest numbers must more than two
                # if length - (j+1) < 2: break

                subTarget = target - (nums[i]+nums[j])
                k, l = j+1, length-1
                
                # Analyzing the subTarget with advantage of sorted array
                # nums[k] would be smallest number in remain numbers, subTarget < nums[k]*2 => no combination would exists
                # nums[l] would be biggest number in remain numbers, subTarget > nums[l]*2 => no combination would exists
                # Fisrt statement would keep this statement from "list index out of range"
                if subTarget < nums[k]*2 or subTarget > nums[l]*2: continue
                
                while k < l:
                    subSum = nums[k] + nums[l]
                    if subSum  == subTarget:
                        answer.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        while k < length and nums[k] == nums[k-1]: k+=1
                    elif subSum > subTarget: l -= 1
                    elif subSum < subTarget: k += 1
           
        return answer

    # runtime: 840ms.
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        length = len(nums)
        answer = []

        # Like 3Sum but add another level
        # Set subTarget (target - (furstNumber+secondNumber)), and find combination
        for i in range(length):

            # Skip if it is duplicated
            if i > 0 and nums[i] == nums[i-1]: continue
            
            for j in range(i+1, length):
                
                # Skip if it is duplicated
                if j > i+1 and nums[j] == nums[j-1]: continue

                # Set subTarget, and start to find combination
                subTarget = target - (nums[i]+nums[j])
                k, l = j+1, length-1
                while k < l:
                    # If combination match then append to the answer
                    # To skip duplication, keep adding index k until nums[k] value not the same
                    subSum = nums[k] + nums[l]
                    if subSum  == subTarget:
                        answer.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        while k < length and nums[k] == nums[k-1]: k+=1
                    elif subSum > subTarget: l -= 1
                    elif subSum < subTarget: k += 1
           
        return answer