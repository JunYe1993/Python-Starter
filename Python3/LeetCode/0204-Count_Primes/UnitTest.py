from .Solution import Solution
import unittest

class TestMethods(unittest.TestCase):
    def test_case1(self):
        n = 10
        expect = 4
        result = Solution().countPrimes(n)
        self.assertEqual(expect, result)
    def test_case2(self):
        n = 0
        expect = 0
        result = Solution().countPrimes(n)
        self.assertEqual(expect, result)
    def test_case3(self):
        n = 1
        expect = 0
        result = Solution().countPrimes(n)
        self.assertEqual(expect, result)
    def test_case4(self):
        n = 999983
        expect = 78497
        result = Solution().countPrimes(n)
        self.assertEqual(expect, result)

if __name__ == "__main__":
    unittest.main()