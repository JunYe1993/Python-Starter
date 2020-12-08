from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
    
        lenPrice = len(prices)
        maxProfit = 0
        holdStockPrice = prices[0]
        for curStockPrice in prices[1:]:
            curProfit = curStockPrice - holdStockPrice
            maxProfit = curProfit if curProfit > maxProfit else maxProfit
            holdStockPrice = curStockPrice if curStockPrice < holdStockPrice else holdStockPrice

        return maxProfit
