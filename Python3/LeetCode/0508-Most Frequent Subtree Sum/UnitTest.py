import unittest
import Solution

class TestMethods(unittest.TestCase):
     
     def test_case1(self):
          testclass = Solution.Solution()
          spec = Solution.TreeNode(5)
          spec.left = Solution.TreeNode(2)
          spec.right = Solution.TreeNode(-3)
          #testclass.findFrequentTreeSum(spec)
          self.assertEqual(testclass.findFrequentTreeSum(spec), [2, -3, 4])

     def test_case2(self):
          testclass = Solution.Solution()
          spec = Solution.TreeNode(5)
          spec.left = Solution.TreeNode(2)
          spec.right = Solution.TreeNode(-5)
          # testclass.findFrequentTreeSum(spec)
          self.assertEqual(testclass.findFrequentTreeSum(spec), [2])

if __name__ == '__main__':
     # TestMethods.test_case1()
     unittest.main()