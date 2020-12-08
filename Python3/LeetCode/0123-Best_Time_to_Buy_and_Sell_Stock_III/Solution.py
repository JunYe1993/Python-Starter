from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
    
        profits = []
        holdStockPrice = prices[0]
        for curStockPrice in prices[1:]:
            curProfit = curStockPrice - holdStockPrice
            if curProfit < 0:
                holdStockPrice = curStockPrice
            
        return profit
