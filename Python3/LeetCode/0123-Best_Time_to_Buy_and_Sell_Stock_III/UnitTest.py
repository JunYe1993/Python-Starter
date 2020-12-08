import unittest
from . import Solution
from ..TestingModule.ListNode import ListNode

class TestMethods(unittest.TestCase):

    def test_case1(self):
        
        # Arrange 
        testclass = Solution.Solution()
        prices = [7,1,5,3,6,4]

        # Act
        result = testclass.maxProfit(prices)
        expect = 7
    
        # Assert
        self.assertEqual(expect, result)

    def test_case2(self):
        
        # Arrange 
        testclass = Solution.Solution()
        prices = [1,2,3,4,5]

        # Act
        result = testclass.maxProfit(prices)
        expect = 4
    
        # Assert
        self.assertEqual(expect, result)

    def test_case3(self):
        
        # Arrange 
        testclass = Solution.Solution()
        prices = [7,6,4,3,1]

        # Act
        result = testclass.maxProfit(prices)
        expect = 0
    
        # Assert
        self.assertEqual(expect, result)

if __name__ == '__main__':
    unittest.main()
     