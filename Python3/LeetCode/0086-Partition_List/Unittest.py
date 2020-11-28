import unittest
from . import Solution
from ..TestingModule.ListNode import ListNode
from ..TestingModule.ListNode import ListNodes

class TestMethods(unittest.TestCase):

     def test_case1(self):
          
          # Arrange 
          testclass = Solution.Solution()
          spec = ListNodes([1,4,3,2,5,2])
          target = 3

          # Act
          result = testclass.partition(spec, target)
          expect = ListNodes([1,2,2,4,3,5])
          IsEqual = ListNodes.IsEqual(result, expect)

          # Assert
          self.assertEqual(IsEqual, True)

if __name__ == '__main__':
     unittest.main()
     