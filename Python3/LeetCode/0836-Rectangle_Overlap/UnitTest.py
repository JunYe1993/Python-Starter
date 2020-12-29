from .Solution import Solution
import unittest

class TestMethods(unittest.TestCase):
    def test_case1(self):
        rec1 = [0,0,2,2]
        rec2 = [1,1,3,3]
        expect = True
        result = Solution().isRectangleOverlap(rec1, rec2)
        self.assertEqual(expect, result)
    def test_case2(self):
        rec1 = [0,0,1,1]
        rec2 = [1,0,2,1]
        expect = False
        result = Solution().isRectangleOverlap(rec1, rec2)
        self.assertEqual(expect, result)
    def test_case3(self):
        rec1 = [0,0,1,1]
        rec2 = [2,2,3,3]
        expect = False
        result = Solution().isRectangleOverlap(rec1, rec2)
        self.assertEqual(expect, result)

if __name__ == "__main__":
    unittest.main()