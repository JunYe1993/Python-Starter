from typing import List
from collections import deque
from ..TestingModule.TreeNode import TreeNode

class Solution:
    
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        # Perfrom in-order traversal on both trees, and get two sorted array

        # Note:
        # The container of array1 and array2 would be double-ended queue
        # Because list.pop(0) takes O(n), and deque.popleft() takes constant time.
        answer, array1, array2 = [], deque(), deque()
        self.getInOrderArray(root1, array1)
        self.getInOrderArray(root2, array2)
        
        # Merge 2 sorted array
        while array1 and array2:
            answer.append(array1.popleft() if array1[0] < array2[0] else array2.popleft())

        # It would be only larger one remain.
        return answer + list(array1) + list(array2)

    def getInOrderArray(self, node, returnList):
        if node == None: return
        self.getInOrderArray(node.left, returnList)
        returnList.append(node.val)
        self.getInOrderArray(node.right, returnList)

    def getAllElements_reverse(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        # Try not to use double-ended queue workaround.
        answer, array1, array2 = [], [], []
        self.getReverseInOrderArray(root1, array1)
        self.getReverseInOrderArray(root2, array2)
        
        while array1 or array2:
            
            if not array1: 
                answer.append(array2.pop())
                continue
            if not array2:
                answer.append(array1.pop())
                continue 

            answer.append(array1.pop() if array1[-1] < array2[-1] else array2.pop())

        return answer
        
    def getReverseInOrderArray(self, node, returnList):
        if node == None: return
        self.getReverseInOrderArray(node.right, returnList)
        returnList.append(node.val)
        self.getReverseInOrderArray(node.left, returnList)