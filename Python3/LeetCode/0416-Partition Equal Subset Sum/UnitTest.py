import unittest
import Solution

class TestMethods(unittest.TestCase):

     def test_case1(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec = [1, 5, 11, 5]

          # Act
          result = testclass.canPartition(spec)
          expect = True

          # Assert
          self.assertEqual(result, expect)

     def test_case2(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec = [1, 2, 3, 5]

          # Act
          result = testclass.canPartition(spec)
          expect = False

          # Assert
          self.assertEqual(result, expect)

     def test_case3(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec = [1, 2, 5]

          # Act
          result = testclass.canPartition(spec)
          expect = False

          # Assert
          self.assertEqual(result, expect)

     def test_case4(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec = [1, 1]

          # Act
          result = testclass.canPartition(spec)
          expect = True

          # Assert
          self.assertEqual(result, expect)

if __name__ == '__main__':
     unittest.main()