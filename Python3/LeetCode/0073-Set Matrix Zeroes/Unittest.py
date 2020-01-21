import unittest
import Solution

class TestMethods(unittest.TestCase):

     def test_case1(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec = [[1,1,1],[1,0,1],[1,1,1]]

          # Act
          result = testclass.setZeroes(spec)
          expect = [[1,0,1],[0,0,0],[1,0,1]]

          # Assert
          self.assertEqual(result, expect)

     def test_case2(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
          # Act
          result = testclass.setZeroes(spec)
          expect = [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

          # Assert
          self.assertEqual(result, expect)

if __name__ == '__main__':
     unittest.main()