from ..TestingModule.TreeNode import TreeNode

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        # Travel all the binary tree by recursion
        thisNodeNeedtoPrune = self.pruning(root)
        return root if not thisNodeNeedtoPrune else None

    def pruning(self, node: TreeNode) -> bool:
        # If node.val == 1 then this sub tree is no need to be pruned
        thisNodeNeedtoPrune = False if node.val else True 

        # Travel sub tree and return whether sub tree need to be pruned
        # If sub tree need to prune => node.[left/right] = None
        # Using &= because if there is a sub tree is no need to be pruned
        # , then return false
        if node.left: 
            subNodeNeedtoPrune = self.pruning(node.left)
            thisNodeNeedtoPrune &= subNodeNeedtoPrune
            if subNodeNeedtoPrune: node.left = None
        if node.right: 
            subNodeNeedtoPrune = self.pruning(node.right)
            thisNodeNeedtoPrune &= subNodeNeedtoPrune
            if subNodeNeedtoPrune: node.right = None
        return thisNodeNeedtoPrune