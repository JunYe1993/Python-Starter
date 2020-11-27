import unittest
import Solution

class TestMethods(unittest.TestCase):

     def test_case0(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec1 = [1,2,3,4,5,7,8,9,10,11]
          spec2 = [5,6,7]

          # Act
          result = testclass.findMedianSortedArrays(spec1, spec2)
          expect = 6
          
          # Assert
          self.assertEqual(result, expect)

     def test_case1(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec1 = [1,3]
          spec2 = [2]

          # Act
          result = testclass.findMedianSortedArrays(spec1, spec2)
          expect = 2
          
          # Assert
          self.assertEqual(result, expect)

     def test_case2(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec1 = [1,2]
          spec2 = [3,4]

          # Act
          result = testclass.findMedianSortedArrays(spec1, spec2)
          expect = 2.5
          
          # Assert
          self.assertEqual(result, expect)

     def test_case3(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec1 = [0,0]
          spec2 = [0,0]

          # Act
          result = testclass.findMedianSortedArrays(spec1, spec2)
          expect = 0
          
          # Assert
          self.assertEqual(result, expect)

     def test_case4(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec1 = []
          spec2 = [1]

          # Act
          result = testclass.findMedianSortedArrays(spec1, spec2)
          expect = 1
          
          # Assert
          self.assertEqual(result, expect)

     def test_case5(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec1 = [2]
          spec2 = []

          # Act
          result = testclass.findMedianSortedArrays(spec1, spec2)
          expect = 2
          
          # Assert
          self.assertEqual(result, expect)

if __name__ == '__main__':
     unittest.main()