class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        totalsize = len(nums1) + len(nums2)
        i1 = i2 = 0
        for index in range(totalsize >> 1):
            if i1 == len(nums1):
                pass
            elif i2 == len(nums2):
                pass
            else:
                if nums1[i1] < nums2[i2]: 
                    i1 += 1
                else: 
                    i2 += 1
