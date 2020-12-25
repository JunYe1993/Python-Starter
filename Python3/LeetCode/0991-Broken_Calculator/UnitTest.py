from .Solution import Solution
import unittest

class TestMethods(unittest.TestCase):
    
    def test_case1(self):
        X, Y = 2, 3
        expect = 2
        result = Solution().brokenCalc(X, Y)
        self.assertEqual(expect, result)

    def test_case2(self):
        X, Y = 5, 8
        expect = 2
        result = Solution().brokenCalc(X, Y)
        self.assertEqual(expect, result)

    def test_case3(self):
        X, Y = 3, 10
        expect = 3
        result = Solution().brokenCalc(X, Y)
        self.assertEqual(expect, result)

    def test_case4(self):
        X, Y = 1024, 1
        expect = 39
        result = Solution().brokenCalc(X, Y)
        self.assertEqual(expect, result)

    def test_case5(self):
        X, Y = 1, 1000000000
        expect = 2284
        result = Solution().brokenCalc(X, Y)
        self.assertEqual(expect, result)

if  __name__ == "__main__":
    unittest.main()