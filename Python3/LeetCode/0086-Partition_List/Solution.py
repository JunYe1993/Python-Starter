from ..TestingModule.ListNode import ListNode

class Solution:
     def partition(self, head: ListNode, x: int) -> ListNode:
          leftroot = left = ListNode(0)
          rightroot = right = ListNode(0)

          while head:
               if head.val < x:
                    left.next = ListNode(head.val)
                    left = left.next
               else:
                    right.next = ListNode(head.val)
                    right = right.next

               head = head.next
          
          left.next = rightroot.next
          return leftroot.next 
     
     def Qpartition(self, head: ListNode, x: int) -> ListNode:
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
          