from typing import List

class Solution:
    
    # drop some combination not gonna 
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        length = len(nums)
        answer, targetMap, table = [], set(), {}

        for val in nums:
            if val not in targetMap:
                targetMap.add(val)

        for i in range(length):
            # Skip when it's duplicate
            if i > 0 and nums[i] == nums[i-1]: continues
            
            for k in reversed(range(i+1, length)):
                # Skip when it's duplicate
                if k < length-1 and nums[k] == nums[k+1]: continue

                target = 0 - (nums[i]+nums[k])
                if target > nums[-1]: break
                elif target not in targetMap: continue
                elif target not in table:
                    table[target] = [[nums[i], nums[k], i, k]]
                else:
                    table[target].append([nums[i], nums[k], i, k])

        for j in range(length):
            if nums[j] in table:
                for data in table[nums[j]]:
                    if j > data[2] and j < data[3]:
                        answer.append([data[0], nums[j], data[1]])
                        data[2] = length
        return answer

    # Standard answer
    def QthreeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        length = len(nums)
        answer = []

        # Reduce problem to 2 SUM.
        # But this find target first, then find the combination.
        for i in range(length):
            
            # Skip when it's duplicated
            if i > 0 and nums[i] == nums[i-1]: continue
            
            # Set target, and start to find combination.
            target = nums[i] * (-1)
            j, k = i+1, length-1
            while j < k:
                subSum = nums[j] + nums[k]
                # If combination match then append to the answer
                # To skip duplication, index j keep adding until value not the same
                if subSum == target:
                    answer.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < length and nums[j] == nums[j-1]: j += 1
                # If combination bigger than target, index k reduce 1,
                # smaller than target, index j add 1. Because it's sorted array
                elif subSum > target: k -= 1
                elif subSum < target: j += 1
        
        return answer

    
    # Ignore some extreme case. runtime 6000s
    def QthreeSum_v2(self, nums: List[int]) -> List[List[int]]:
        
        answer, table = [], {}
        nums.sort()
        length = len(nums)

        for i in range(length):

            # Skip when it's duplicate
            if i > 0 and nums[i] == nums[i-1]: continue
            
            for k in reversed(range(i+1, length)):

                # Skip when it's duplicate
                if k < length-1 and nums[k] == nums[k+1]: continue

                target = 0 - (nums[i]+nums[k])
                if target > nums[-1]: break
                elif target not in table:
                    table[target] = [[nums[i], nums[k], i, k]]
                else:
                    table[target].append([nums[i], nums[k], i, k])

        for j in range(length):
            if nums[j] in table:
                for data in table[nums[j]]:
                    if j > data[2] and j < data[3]:
                        answer.append([data[0], nums[j], data[1]])
                        data[2] = length
        return answer

    # runtime 7000s
    def QthreeSum(self, nums: List[int]) -> List[List[int]]:
        
        answer, table = [], {}
        nums.sort()
        length = len(nums)
        
        # Reduce problem to 2 SUM.
        # Using exhaustive method to store every combination of first number and second number.
        for i in range(length):
            
            # Skip when it's duplicate
            if i > 0 and nums[i] == nums[i-1]: continue
            
            for j in range(i+1, length):
                
                # Skip when it's duplicate
                if j > i+1 and nums[j] == nums[j-1]: continue
            
                # Save the target number as key, which's sum equal 0, with first and second number. 
                target = 0 - (nums[i]+nums[j])    
                # Table value would be an array, cause there might be more than one different combination 
                # has the same target number. If key doesn't exist then init, otherwise append to array.
                # The target number's index need to be bigger than third element in the array,
                # which is index j.  
                if target not in table:
                    table[target] = [[nums[i], nums[j], j]]
                else:
                    table[target].append([nums[i], nums[j], j])       

        # Loop nums to search for target number, starting from 2 means no duplicate.
        for k in range(2, length):

            if nums[k] > maxTarget:
                break
            if nums[k] in table:    
                for index, arr in enumerate(table[nums[k]]):
                    
                    # Index k need to be bigger than index j for no duplication
                    if k > arr[2]:
                        answer.append([arr[0], arr[1], nums[k]])
                        # Set third element to length(max) means this combination no longer availible
                        # Prevent case like same target number with different index.
                        arr[2] = length   

        return answer
    
    
    # Time Limit Exceeded
    def QthreeSum(self, nums: List[int]) -> List[List[int]]:
        # [-4, -1, -1, 0, 1, 2]
        answer = []
        nums.sort()
        length = len(nums)
        
        
        for i in range(length):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, length):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                for k in range(j+1, length):
                    if k > j+1 and nums[k] == nums[k-1]:
                        continue
                    curSum = nums[i] + nums[j] + nums[k]
                    if curSum == 0:
                        answer.append([nums[i],nums[j],nums[k]])
                    elif curSum > 0:
                        break    

        return answer