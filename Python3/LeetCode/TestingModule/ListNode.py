from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class ListNodes:
    
    def __init__(self, nums: List[int]):
        root = n = ListNode(0)
        for i in range(len(nums)):
            n.next = ListNode(nums[i])
            n = n.next
        self.val = root.next.val
        self.next = root.next.next
    
    def IsEqual(l1: ListNode, l2: ListNode):

        while l1 or l2:
            if not l1 or not l2:
                return False
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next
        
        return True
