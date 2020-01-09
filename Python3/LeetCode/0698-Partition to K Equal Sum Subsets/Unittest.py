import unittest
import Solution

class TestMethods(unittest.TestCase):

     def test_case1(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec1 = [4, 3, 2, 3, 5, 2, 1]
          spec2 = 4
          

          # Act 
          result = testclass.canPartitionKSubsets(spec1, spec2)
          expect = True
          
          # Assert
          self.assertEqual(result, expect)

     def test_case2(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec1 = [2,2,2,2,3,4,5]
          spec2 = 4
          

          # Act 
          result = testclass.canPartitionKSubsets(spec1, spec2)
          expect = False
          
          # Assert
          self.assertEqual(result, expect)

if __name__ == '__main__':
     unittest.main()