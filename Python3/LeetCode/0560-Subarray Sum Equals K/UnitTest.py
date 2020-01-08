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
          expect = 2

          # Assert
          self.assertEqual(result, expect)
     def test_case2(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec1 = [-1,-1,1]
          spec2 = 0

          # Act
          result = testclass.subarraySum(spec1, spec2)
          expect = 1

          # Assert
          self.assertEqual(result, expect)
    
     def test_case3(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec1 = [0,0,0,0,0,0,0,0,0,0]
          spec2 = 0

          # Act
          result = testclass.subarraySum(spec1, spec2)
          expect = 55

          # Assert
          self.assertEqual(result, expect)
     
     def test_case4(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec1 = [-27,125,209,-84,-222,-137,112,-76,200,-139,200,61,-215,121,318,-128,121,216,-132,165,-19,89,193,-59,203,8,140,-128,-201,199,-5,36,-167,-140,-194,-166,182,-50,729,-167,-114,-71,108,-40,-189,188,-109,69,-134,682,173,-89,-114,-177,194,-1,168,-42,-55,-32,198,171,45,25,-18,154,-22,-192,213,86,-16]
          spec2 = 223
          
          # Act
          result = testclass.subarraySum(spec1, spec2)
          expect = 10

          # Assert
          self.assertEqual(result, expect)

     def test_case5(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec1 = [1,2,1,3]
          spec2 = 3

          # Act
          result = testclass.subarraySum(spec1, spec2)
          expect = 3

          # Assert
          self.assertEqual(result, expect)
     
   
if __name__ == '__main__':
     unittest.main()