from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
    
        profit = 0
        holdStockPrice = prices[0]
        for curStockPrice in prices[1:]:
            curProfit = curStockPrice - holdStockPrice
            holdStockPrice = curStockPrice
            if curProfit > 0:
                profit += curProfit
            
        return profit
