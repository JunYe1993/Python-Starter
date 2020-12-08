# Question
# Given two arrays a1 and a2, a1 and a2 are both sorted. a1 contains x number of
# placeholders, where x = a2.length, and they are all appended at the tail of a1, merge
# two arrays as one sorted array. Ex1 a1 = [5,6,7,-1,-1] a2 = [1,2] return [1,2,5,6,7] Ex2
# a1 = [2,3,9,-1,-1,-1] a2 = [1,5,10] return [1,2,3,5,9,10] Plus: Can you use just constant
# space?(modify a1 in place)

from typing import List
import unittest

class Solution:
    def mergeArray(a1: List, a2: List) -> List:
        
        len1, len2 = len(a1), len(a2)
        index1 = index2 = 0
        while index1 < len1 and index2 < len2:
            if a1[index1] == -1:
                a1[index1] = a2[index2]
                index2 += 1
            elif a1[index1] > a2[index2]:
                for i in reversed(range(index1, len1-len2+index2)):
                    a1[i+1] = a1[i]
                a1[index1] = a2[index2]
                index2 += 1
            else:
                index1 += 1
        
        return a1

class TestMethods(unittest.TestCase):
    
    def test_case1(self):
        
        # Arrange
        spec1 = [5,6,7,-1,-1]
        spec2 = [1,2]
        expect = [1,2,5,6,7]
        result = Solution.mergeArray(spec1, spec2)

        # Assert
        self.assertEqual(expect, result)

    def test_case2(self):
        
        # Arrange
        spec1 = [2,3,9,-1,-1,-1]
        spec2 = [1,5,10]
        expect = [1,2,3,5,9,10]
        result = Solution.mergeArray(spec1, spec2)

        # Assert
        self.assertEqual(expect, result)

if __name__ == '__main__':
    unittest.main()