import unittest
import Solution

class TestMethods(unittest.TestCase):

     def test_case1(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec = "abbcccbbbcaaccbababcbcabca"

          # Act
          result = testclass.longestPalindrome(spec)
          expect = "bbcccbb"
          
          # Assert
          self.assertEqual(result, expect)

     def test_case2(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec = "cbbd"

          # Act
          result = testclass.longestPalindrome(spec)
          expect = "bb"
          
          # Assert
          self.assertEqual(result, expect)

     def test_case3(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec = "a"

          # Act
          result = testclass.longestPalindrome(spec)
          expect = "a"
          
          # Assert
          self.assertEqual(result, expect)

if __name__ == '__main__':
     unittest.main()
     # test = TestMethods()
     # test.test_case1()