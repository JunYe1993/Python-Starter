
class ListNode:
     def __init__(self, x):
          self.val = x
          self.next = None

class Solution:
     def partition(self, head: ListNode, x: int) -> ListNode:
          
          leftroot = left = ListNode(0)
          rightroot = right = ListNode(0)
          
          while head:

               if x > head.val:
                    left.next = ListNode(head.val)
                    left = left.next
               else:
                    right.next = ListNode(head.val)
                    right = right.next
                    
               head = head.next
          
          left.next = rightroot.next
          return leftroot.next
          