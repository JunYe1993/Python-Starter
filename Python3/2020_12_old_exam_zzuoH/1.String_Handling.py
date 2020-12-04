# Question:
# Write a function that takes a string as input and returns a number contained in the
# string. You need to support sign, floating point, and ignore spaces at the beginning or
# end of the string. Otherwise raise an exception.

import unittest
import re

class Solution:
    def extractNumbers (target: str) -> str:
        # regex pattern analysis
        # ^\s*        -> ignore spaces at the beginning     -> not in group 1 
        # [+-]?\d+    -> support sign                       -> in group 1
        # (\.)?       -> support floating point             -> in group 1 & 2
        # (?(2)\d+|)) -> if group 2 (floating point) exist, there must be number follow the floating point
        # \s*$        -> ignore spaces at the end of string -> not in group 1
        # return group 1 
        match = re.search("^\s*([+-]?\d+(\.)?(?(2)\d+|))\s*$", target)
        if match:
            return match.group(1)
        else:
            raise Exception("Wrong imput.")


class TestMethods(unittest.TestCase):
    def test_case1(self):
        
        # Arrange 
        spec   = "   -1098.1  "
        expect = "-1098.1"
        result = Solution.extractNumbers(spec)
        
        # Assert
        self.assertEqual(result, expect)

if __name__ == '__main__':
    unittest.main()