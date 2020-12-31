from .Solution import Solution
import unittest

class TestMethods(unittest.TestCase):
    
    def test_case1(self):
        N = 121
        expect = True
        result = Solution().isPalindrome(N)
        self.assertEqual(expect, result)

    def test_case2(self):
        N = -121
        expect = False
        result = Solution().isPalindrome(N)
        self.assertEqual(expect, result)

    def test_case3(self):
        N = 10
        expect = False
        result = Solution().isPalindrome(N)
        self.assertEqual(expect, result)

    def test_case2(self):
        N = -101
        expect = False
        result = Solution().isPalindrome(N)
        self.assertEqual(expect, result)

if __name__ == "__main__":
    unittest.main()