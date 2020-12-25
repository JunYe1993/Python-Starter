from typing import List

# Binary Tree Node
class TreeNode:

    def __init__(self, x = 0):
        self.val = x
        self.left = None
        self.right = None

class TreeNodes:

    def __init__(self, nums = None):
        # If it is empty
        if not nums:
            self.val = None
            self.left = None
            self.right = None
            self = None
            return
        
        root = TreeNode(nums[0])
        nodes_of_curlevel = [root]
        
        len_of_nums = len(nums)
        index = 1
        while index < len_of_nums:
            nodes_of_nextlevel = []
            for node in nodes_of_curlevel:
                if index >= len_of_nums: 
                    break
                if nums[index] != None:
                    node.left = TreeNode(nums[index])
                    nodes_of_nextlevel.append(node.left)
                index += 1

                if index >= len_of_nums: 
                    break
                if nums[index] != None:
                    node.right = TreeNode(nums[index])
                    nodes_of_nextlevel.append(node.right)
                index += 1
            nodes_of_curlevel = nodes_of_nextlevel
        
        self.val = root.val
        self.left = root.left
        self.right = root.right

    def checkSelf(self, node = None) -> List[int]:
        
        returnList = []
        curlevel = [node] if node else [self]
        while curlevel:
            nextlevel = []
            IsNextLevelExist = False
            for node in curlevel: 
                val = node.val if node else None 
                returnList.append(val)
                if node:
                    nextlevel.append(node.left)
                    nextlevel.append(node.right)
                    IsNextLevelExist |= True if node.left else False
                    IsNextLevelExist |= True if node.right else False
            
            if not IsNextLevelExist:
                break

            curlevel = nextlevel

        while returnList[-1] == None:
            returnList.pop()

        return returnList

    def checkcheckSelf(self):
        root = n = TreeNode(1)
        n.left = None
        n.right = TreeNode(0)
        n = n.right
        n.left = TreeNode(0)
        n.right = TreeNode(1)
        self.val = root.val
        self.left = root.left
        self.right = root.right
        return self.checkSelf(self)