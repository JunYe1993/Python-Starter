import unittest
import Solution

class TestMethods(unittest.TestCase):

     def test_case1(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec = "abcabcbb"

          # Act
          result = testclass.lengthOfLongestSubstring(spec)
          expect = 3
          
          # Assert
          self.assertEqual(result, expect)

     def test_case2(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec = "pwwkew"

          # Act
          result = testclass.lengthOfLongestSubstring(spec)
          expect = 3
          
          # Assert
          self.assertEqual(result, expect)

     def test_case3(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec = "bbbbb"

          # Act
          result = testclass.lengthOfLongestSubstring(spec)
          expect = 1
          
          # Assert
          self.assertEqual(result, expect)

if __name__ == '__main__':
     unittest.main()