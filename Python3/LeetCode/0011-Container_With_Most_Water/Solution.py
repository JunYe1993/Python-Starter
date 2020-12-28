from typing import List
class Solution(object):
    def maxArea(self, height: List[int]) -> int:

        # Measure volume between most left and most right borders: width * minHeight.
        # If there is volume bigger than it, minHeight must be bigger too.
        # So shift indexes to find it.
        #     height[lIndex] > height[rIndex]: move rIndex
        #     height[lIndex] < height[rIndex]: move lIndex

        length = len(height)
        maxArea, lIndex, rIndex = 0, 0, length-1
        while lIndex < rIndex:
            if height[lIndex] > height[rIndex]:
                h = height[rIndex]
                area = h * (rIndex-lIndex)
                maxArea = max(maxArea, area)
                rIndex -= 1
                while rIndex>=0 and height[rIndex]<h: rIndex -= 1
            else:
                h = height[lIndex]
                area = h * (rIndex-lIndex)
                maxArea = max(maxArea, area)
                lIndex += 1
                while lIndex<length and height[lIndex]<h: lIndex += 1
        return maxArea