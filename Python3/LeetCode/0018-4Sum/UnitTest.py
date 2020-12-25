from .Solution import Solution
import unittest

class TestMethods(unittest.TestCase):
    def test_case1(self):
        spec, target = [1,0,-1,0,-2,2], 0
        expect = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
        result = Solution().fourSum(spec, target)
        self.assertEqual(expect, result)
    def test_case2(self):
        spec, target = [], 0
        expect = []
        result = Solution().fourSum(spec, target)
        self.assertEqual(expect, result)
    def test_case3(self):
        spec, target = [-3,-2,-1,0,0,1,2,3], 0
        expect = [[-3,-2,2,3],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
        result = Solution().fourSum(spec, target)
        self.assertEqual(expect, result)
    def test_case4(self):
        spec, target = [-1,-5,-5,-3,2,5,0,4], -7
        expect = [[-5,-5,-1,4],[-5,-3,-1,2]]
        result = Solution().fourSum(spec, target)
        self.assertEqual(expect, result)

if __name__ == "__main__":
    unittest.main()