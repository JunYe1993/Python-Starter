from ..TestingModule.TreeNode import TreeNode

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # Do a In-order traversal and store node value in an array.
        # Check the array if is sorted.
        treeArray = [] 
        self.travelTree(root, treeArray)
        for i in range(len(treeArray)):
            if i > 0 and treeArray[i] <= treeArray[i-1]:
                return False
        return True

    def travelTree(self, node, treeArray):
        if node != None:
            self.travelTree(node.left, treeArray)
            treeArray.append(node.val)
            self.travelTree(node.right, treeArray)