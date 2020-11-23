import unittest
import Solution

class TestMethods(unittest.TestCase):

     def test_case1(self):
          
          # Arrange 
          testclass = Solution.Solution()
          nums = 2,7,11,15
          target = 9

          # Act
          result = testclass.twoSum(nums, target)
          expect = 0,1

          # Assert
          self.assertEqual(result, expect)

if __name__ == '__main__':
     unittest.main()