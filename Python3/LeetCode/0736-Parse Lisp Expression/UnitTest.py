import unittest
import Solution

class TestMethods(unittest.TestCase):

     def test_case1(self):
          testclass = Solution.Solution()
          spec = '(add 1 2)'
          self.assertEqual(testclass.evaluate(spec), 3)

     def test_case2(self):
          testclass = Solution.Solution()
          spec = '(mult 3 (add 2 3))'
          self.assertEqual(testclass.evaluate(spec), 15)
     
     def test_case3(self):
          testclass = Solution.Solution()
          spec = '(let x 2 (mult x 5))'
          self.assertEqual(testclass.evaluate(spec), 10)
     
     def test_case4(self):
          testclass = Solution.Solution()
          spec = '(let x 2 (mult x (let x 3 y 4 (add x y))))'
          self.assertEqual(testclass.evaluate(spec), 14)
     
     def test_case5(self):
          testclass = Solution.Solution()
          spec = '(let x 3 x 2 x)'
          self.assertEqual(testclass.evaluate(spec), 2)
     
     def test_case6(self):
          testclass = Solution.Solution()
          spec = '(let x 1 y 2 x (add x y) (add x y))'
          self.assertEqual(testclass.evaluate(spec), 5)

     def test_case7(self):
          testclass = Solution.Solution()
          spec = '(let x 2 (add (let x 3 (let x 4 x)) x))'
          self.assertEqual(testclass.evaluate(spec), 6)

     def test_case8(self):
          testclass = Solution.Solution()
          spec = '(let a1 3 b2 (add a1 1) b2)'
          self.assertEqual(testclass.evaluate(spec), 4)

if __name__ == '__main__':
     unittest.main()