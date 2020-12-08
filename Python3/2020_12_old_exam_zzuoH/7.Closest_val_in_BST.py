# Question:
# Find the closest value in Binary Search Tree

import unittest

class BSTnode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

class Solution:

    def findClosestValue(self, node: BSTnode, target: int) -> int:
        maxNum = 1000000
        key = [None, maxNum]
        return self.findClosest(node, target, key)

    def findClosest(self, node, target, key):
        if node == None:
            return key[0]
        elif node.val == target:
            return target
        else:
            diff = node.val - target
            if key[1] > abs(diff):
                key[0] = node.val
                key[1] = abs(diff)
            if diff > 0:
                return self.findClosest(node.left, target, key)
            else:
                return self.findClosest(node.right, target, key)
            


    

        
        

class TestMethods(unittest.TestCase):

    def getBST() -> BSTnode:
        root = BSTnode(9)  
        root.left = BSTnode(4)  
        root.right = BSTnode(17) 
        root.left.left = BSTnode(3)  
        root.left.right = BSTnode(6) 
        root.left.right.left = BSTnode(5)  
        root.left.right.right = BSTnode(7)  
        root.right.right = BSTnode(22) 
        root.right.right.left = BSTnode(20)
        return root
    
    def test_case1(self):

        # Arrange 
        testclass = Solution()
        tree = TestMethods.getBST()
        target = 4
        expect = 4
        result = testclass.findClosestValue(tree, target)

        # Assert
        self.assertEqual(result, expect)

    def test_case2(self):

        # Arrange 
        testclass = Solution()
        tree = TestMethods.getBST()
        target = 18
        expect = 17
        result = testclass.findClosestValue(tree, target)

        # Assert
        self.assertEqual(result, expect)

    def test_case3(self):

        # Arrange 
        testclass = Solution()
        tree = TestMethods.getBST()
        target = 12
        expect = 9
        result = testclass.findClosestValue(tree, target)

        # Assert
        self.assertEqual(result, expect)

if __name__ == '__main__':
    unittest.main()