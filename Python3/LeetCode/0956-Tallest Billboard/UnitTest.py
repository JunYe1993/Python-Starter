import unittest
import Solution

class TestMethods(unittest.TestCase):

     def test_case1(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec = [1,2,3,6]

          # Act
          result = testclass.tallestBillboard(spec)
          expect = 6

          # Assert
          self.assertEqual(result, expect)

     def test_case2(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec = [1,2,3,4,5,6]

          # Act
          result = testclass.tallestBillboard(spec)
          expect = 10

          # Assert
          self.assertEqual(result, expect)

     def test_case3(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec = [1,2]

          # Act
          result = testclass.tallestBillboard(spec)
          expect = 0

          # Assert
          self.assertEqual(result, expect)

if __name__ == '__main__':
     unittest.main()