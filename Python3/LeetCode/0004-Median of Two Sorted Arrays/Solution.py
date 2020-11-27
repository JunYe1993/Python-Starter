from typing import List
class Solution:
     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
          len1, len2 = len(nums1), len(nums2)
          lenMerged = len1 + len2

          previous = current = 0
          indexMerged = index1 = index2 = 0
          end = lenMerged // 2
          while indexMerged <= end:
               
               # if lenMerged is even, need to record two value
               previous = current

               # check if run out of either nums1 or nums2
               if index1 == len1:
                    current = nums2[index2]
                    index2 += 1
               elif index2 == len2:
                    current = nums1[index1]
                    index1 += 1
               # compare two value, small one count first
               elif nums1[index1] > nums2[index2]:
                    current = nums2[index2]
                    index2 += 1
               else:
                    current = nums1[index1]
                    index1 += 1

               indexMerged += 1

          return current if lenMerged % 2 else (current+previous)/2