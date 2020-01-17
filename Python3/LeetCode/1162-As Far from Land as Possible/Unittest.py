import unittest
import Solution

class TestMethods(unittest.TestCase):

     def test_case1(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec = [[1,0,1], [0,0,0], [1,0,1]]

          # Act
          result = testclass.maxDistance(spec)
          expect = 2

          # Assert
          self.assertEqual(result, expect)

     def test_case2(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec = [[1,0,0], [0,0,0], [0,0,0]]
          # Act
          result = testclass.maxDistance(spec)
          expect = 4

          # Assert
          self.assertEqual(result, expect)

if __name__ == '__main__':
     unittest.main()