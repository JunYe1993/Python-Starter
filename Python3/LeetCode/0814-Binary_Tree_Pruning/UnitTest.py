from ..TestingModule.TreeNode import TreeNodes
from .Solution import Solution
import unittest

class TestMethods(unittest.TestCase):
    def test_case1(self):
        spec = [1,None,0,0,1]
        expect = [1,None,0,None,1]
        result = TreeNodes().checkSelf(Solution().pruneTree(TreeNodes(spec)))
        self.assertEqual(expect, result)

if __name__ == "__main__":
    unittest.main()