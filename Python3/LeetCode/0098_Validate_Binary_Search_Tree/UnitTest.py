from ..TestingModule.TreeNode import TreeNodes
from .Solution import Solution
import unittest

class TestMethods(unittest.TestCase):

    def test_case1(self):
        root = [2, 1, 3]
        expect = True
        result = Solution().isValidBST(TreeNodes(root))
        self.assertEqual(expect, result)

    def test_case2(self):
        root = [5,1,4,None,None,3,6]
        expect = False
        result = Solution().isValidBST(TreeNodes(root))
        self.assertEqual(expect, result)

if __name__ == "__main__":
    unittest.main()