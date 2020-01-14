import unittest
import Solution

class TestMethods(unittest.TestCase):

     def test_case1(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec = [2, 4]

          # Act
          result = testclass.numFactoredBinaryTrees(spec)
          expect = 3

          # Assert
          self.assertEqual(result, expect)

     def test_case2(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec = [2, 4, 5, 10]

          # Act
          result = testclass.numFactoredBinaryTrees(spec)
          expect = 7

          # Assert
          self.assertEqual(result, expect)

     def test_case3(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec = [18,3,6,2]

          # Act
          result = testclass.numFactoredBinaryTrees(spec)
          expect = 12

          # Assert
          self.assertEqual(result, expect)

     def test_case4(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec = [36,3,6,2]

          # Act
          result = testclass.numFactoredBinaryTrees(spec)
          expect = 15

          # Assert
          self.assertEqual(result, expect)

     def test_case5(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec = [36,3,6,2,18]

          # Act
          result = testclass.numFactoredBinaryTrees(spec)
          expect = 36

          # Assert
          self.assertEqual(result, expect)

     def test_case6(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec = [45,42,2,18,23,1170,12,41,40,9,47,24,33,28,10,32,29,17,46,11,759,37,6,26,21,49,31,14,19,8,13,7,27,22,3,36,34,38,39,30,43,15,4,16,35,25,20,44,5,48]

          # Act
          result = testclass.numFactoredBinaryTrees(spec)
          expect = 777

          # Assert
          self.assertEqual(result, expect)
     
     def test_case7(self):

          # Arrange 
          testclass = Solution.Solution()
          spec = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 87, 136, 144, 150, 240, 352, 380, 476, 540, 544, 546, 585, 690, 799, 1056, 1078, 1296, 1400, 1457, 1968, 2162, 2205, 2730, 3128, 4410, 4488, 5040, 5550, 6000, 7056, 8704, 10912, 11616, 18720, 20774, 21645, 24150, 34496, 49588, 61600, 91872, 92928, 197472, 557568, 1689120, 1883700, 3063808, 16262400, 32710656]
          # Act
          result = testclass.numFactoredBinaryTrees(spec)
          expect = 61675593

          # Assert
          self.assertEqual(result, expect)

     def test_case8(self):

          # Arrange 
          testclass = Solution.Solution()
          spec = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 87, 136, 144, 150, 240, 352, 380, 476, 540, 544, 546, 585, 690, 799, 1056, 1078, 1296, 1400, 1457, 1968, 2162, 2205, 2730, 3128, 4410, 4488, 5040, 5550, 6000, 7056, 8704, 10912, 11616, 18720, 20774, 21645, 24150, 34496, 49588, 61600, 91872, 92928, 197472, 557568, 1689120, 1883700, 3063808, 16262400, 32710656, 523370496]
          # Act
          result = testclass.numFactoredBinaryTrees(spec)
          expect = 509730797

          # Assert
          self.assertEqual(result, expect)


if __name__ == '__main__':
     unittest.main()