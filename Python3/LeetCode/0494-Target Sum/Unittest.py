import unittest
import Solution

class TestMethods(unittest.TestCase):

     def test_case1(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec1 = [1, 1, 1, 1, 1]
          spec2 = 3

          # Act
          result = testclass.findTargetSumWays(spec1, spec2)
          expect = 5

          # Assert
          self.assertEqual(result, expect)

     def test_case2(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec1 = [1]
          spec2 = 1

          # Act
          result = testclass.findTargetSumWays(spec1, spec2)
          expect = 1

          # Assert
          self.assertEqual(result, expect)

     def test_case4(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec1 = [0,0,0,0,0,0,0,0,1]
          spec2 = 1

          # Act
          result = testclass.findTargetSumWays(spec1, spec2)
          expect = 256

          # Assert
          self.assertEqual(result, expect)

if __name__ == '__main__':
     unittest.main()