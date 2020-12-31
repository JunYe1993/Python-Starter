from .Solution import Solution
import unittest

class TestMethods(unittest.TestCase):
    
    def test_case1(self):
        N = 6
        expect = 7
        result = Solution().primePalindrome(N)
        self.assertEqual(expect, result)

    def test_case2(self):
        N = 8
        expect = 11
        result = Solution().primePalindrome(N)
        self.assertEqual(expect, result)

    def test_case3(self):
        N = 102
        expect = 131
        result = Solution().primePalindrome(N)
        self.assertEqual(expect, result)

    def test_case4(self):
        N = 13
        expect = 101
        result = Solution().primePalindrome(N)
        self.assertEqual(expect, result)

if __name__ == "__main__":
    unittest.main()