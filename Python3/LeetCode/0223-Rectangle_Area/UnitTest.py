from .Solution import Solution
import unittest

class TestMethods(unittest.TestCase):
    def test_case1(self):
        A ,B, C, D, E, F, G, H = -3, 0, 3, 4, 0, -1, 9, 2
        expect = 45
        result = Solution().computeArea(A ,B, C, D, E, F, G, H)
        self.assertEqual(expect, result)

    def test_case2(self):
        rec1 = [-3, 0, 3, 4]
        rec2 = [0, -1, 9, 2]
        rec3 = [0, 0, 2, 2]
        expect = 45
        result = Solution().computeAreaHouzz(rec1, rec2, rec3)
        self.assertEqual(expect, result)

if __name__ == "__main__":
    unittest.main()