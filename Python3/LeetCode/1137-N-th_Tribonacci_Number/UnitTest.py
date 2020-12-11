import unittest
from .Solution import Solution

class TestMethods(unittest.TestCase):
    def test_case1(self):
        target = 4
        expect = 4
        result = Solution().tribonacci(target)
        self.assertEqual(expect, result)

if __name__ == "__main__":
    unittest.main()