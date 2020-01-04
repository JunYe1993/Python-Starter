import unittest
import Solution

class TestMethods(unittest.TestCase):

     def test_case1(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec1 = [1,1,1]
          spec2 = 2

          # Act
          result = testclass.subarraySum(spec1, spec2)
          expect = 6

          # Assert
          self.assertEqual(result, expect)

if __name__ == '__main__':
     unittest.main()