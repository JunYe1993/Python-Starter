import unittest
import Solution

class TestMethods(unittest.TestCase):

     def test_case1(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec = 12

          # Act
          result = testclass.numSquares_gama(spec)
          expect = 3

          # Assert
          self.assertEqual(result, expect)

     def test_case2(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec = 13
          # Act
          result = testclass.numSquares_gama(spec)
          expect = 2

          # Assert
          self.assertEqual(result, expect)

if __name__ == '__main__':
     unittest.main()