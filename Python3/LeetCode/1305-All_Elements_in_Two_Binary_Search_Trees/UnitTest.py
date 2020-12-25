from ..TestingModule.TreeNode import TreeNodes
from .Solution import Solution
import unittest

class TestMethods(unittest.TestCase):
    
    def Qtest_case1(self):
        tree1, tree2 = [2, 1, 4], [1, 0, 3]
        expect = [0,1,1,2,3,4]
        result = Solution().getAllElements(TreeNodes(tree1), TreeNodes(tree2))
        self.assertEqual(expect, result)

    def Qtest_case2(self):
        tree1, tree2 = [0,-10,10], [5,1,7,0,2]
        expect = [-10,0,0,1,2,5,7,10]
        result = Solution().getAllElements(TreeNodes(tree1), TreeNodes(tree2))
        self.assertEqual(expect, result)

    def Qtest_case3(self):
        tree1, tree2 = [], [5,1,7,0,2]
        expect = [0,1,2,5,7]
        result = Solution().getAllElements(None, TreeNodes(tree2))
        self.assertEqual(expect, result)

    def Qtest_case4(self):
        tree1, tree2 = [0,-10,10], []
        expect = [-10,0,10]
        result = Solution().getAllElements(TreeNodes(tree1), None)
        self.assertEqual(expect, result)

    def test_case5(self):
        tree1, tree2 = [0,None,59,57,90], [60,17,74,6,20,63,97,None,None,None,None,None,None,95]
        expect = [0,6,17,20,57,59,60,63,74,90,95,97]
        result = Solution().getAllElements(TreeNodes(tree1), TreeNodes(tree2))
        self.assertEqual(expect, result)

if __name__ == "__main__":
    unittest.main()
