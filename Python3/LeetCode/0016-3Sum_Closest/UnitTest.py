from .Solution import Solution
import unittest

class TestMethods(unittest.TestCase):
    def test_case1(self):
        spec, target = [-1,2,1,-4], 1
        expect = 2
        result = Solution().threeSumClosest(spec, target)
        self.assertEqual(expect, result)

if __name__ == "__main__":
    unittest.main()