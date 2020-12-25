from .Solution import Solution
import unittest

class TestMethods(unittest.TestCase):
    
    def test_case1(self):
        spec =  [-1,0,1,2,-1,-4]
        expect = [[-1,-1,2],[-1,0,1]]
        result = Solution().threeSum(spec)
        self.assertEqual(expect, result)

    def test_case2(self):
        spec =  []
        expect = []
        result = Solution().threeSum(spec)
        self.assertEqual(expect, result)

    def test_case3(self):
        spec =  [0]
        expect = []
        result = Solution().threeSum(spec)
        self.assertEqual(expect, result)

    def test_case4(self):
        spec = [0, 0, 0, 0]
        expect = [[0, 0, 0]]
        result = Solution().threeSum(spec)
        self.assertEqual(expect, result)

    def Qtest_case5(self):
        spec = [-2,0,1,1,2]
        expect = [[-2,0,2],[-2,1,1]]
        result = Solution().threeSum(spec)
        self.assertEqual(expect, result)

    def Qtest_case6(self):
        spec = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
        expect = [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]
        result = Solution().threeSum(spec)
        self.assertEqual(expect, result)

    def test_case7(self):
        spec = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
        expect = [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]
        result = Solution().threeSum(spec)
        self.assertEqual(expect, result)

if __name__ == "__main__":
    unittest.main()