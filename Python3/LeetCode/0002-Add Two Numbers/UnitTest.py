import unittest
import Solution
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

class TestMethods(unittest.TestCase):

     def test_case1(self):
          
          # Arrange 
          testclass = Solution.Solution()
          l1 = ListNodes([2, 4, 3])
          l2 = ListNodes([5, 6, 4])

          # Act
          result = testclass.addTwoNumbers(l1, l2)
          expect = ListNodes([7, 0, 8])
          IsEqual = ListNodes.IsEqual(result, expect)

          # Assert
          self.assertEqual(IsEqual, True)

     def test_case2(self):
          
          # Arrange 
          testclass = Solution.Solution()
          l1 = ListNodes([0])
          l2 = ListNodes([0])

          # Act
          result = testclass.addTwoNumbers(l1, l2)
          expect = ListNodes([0])
          IsEqual = ListNodes.IsEqual(result, expect)

          # Assert
          self.assertEqual(IsEqual, True)

     def test_case3(self):
          
          # Arrange 
          testclass = Solution.Solution()
          l1 = ListNodes([9,9,9,9,9,9,9])
          l2 = ListNodes([9,9,9,9])

          # Act
          result = testclass.addTwoNumbers(l1, l2)
          expect = ListNodes([8,9,9,9,0,0,0,1])
          IsEqual = ListNodes.IsEqual(result, expect)

          # Assert
          self.assertEqual(IsEqual, True)

if __name__ == '__main__':
     unittest.main()