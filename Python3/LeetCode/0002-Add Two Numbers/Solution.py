from typing import List
class ListNode:
     def __init__(self, x):
          self.val = x
          self.next = None

class Solution:
     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
          root = n = ListNode(0)                       # 宣告 2 個 ListNode，一個去做運算，一個紀錄第一個 Point
          carry = 0                                       
          while l1 or l2 or carry:                     # 有值或進位則跑
               v1 = v2 = 0
               if l1:
                    v1 = l1.val
                    l1 = l1.next
               if l2:
                    v2 = l2.val
                    l2 = l2.next
               n.next = ListNode((v1 + v2 + carry)%10) # 2個值相加，去進位數
               carry = (v1 + v2 + carry)//10           # 紀錄進位數
               n = n.next
          return root.next