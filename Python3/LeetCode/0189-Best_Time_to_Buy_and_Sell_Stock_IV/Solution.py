from typing import List

class Solution:

    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k < 1:
            return 0

        # 記錄所有獲利組合
        profitData = []
        len_profitData = 0
        lenPrices = len(prices)
        boost = [0]*lenPrices
        for buy_index in range(lenPrices-1):
            for sell_index in range(buy_index+1, lenPrices):
                curProfit = prices[sell_index] - prices[buy_index]
                if curProfit > 0:
                    profitData.append([buy_index, sell_index, curProfit])
                    len_profitData += 1
            boost[buy_index+1] = len_profitData
        print(len(boost))
        
        dp = {}
        def getProfit(layer, index):
            if layer in dp.keys():
                if index in dp[layer].keys():
                    return dp[layer][index]

            if index >= lenPrices:
                return 0

            if layer == 1:
                maxProfit = 0
                if boost[index] < len_profitData:
                    for buy_index, sell_index, curProfit in profitData[boost[index]:]:
                        if index > buy_index: continue
                        if curProfit > maxProfit: maxProfit = curProfit
                dp[1] = {index: maxProfit}
                return maxProfit

            maxProfit = 0
            if boost[index] < len_profitData:
                for buy_index, sell_index, curProfit in profitData[boost[index]:]:
                    if index > buy_index: continue
                    curProfit = curProfit + getProfit(layer-1, sell_index+1)
                    if curProfit > maxProfit: maxProfit = curProfit
            dp[layer] = {index: maxProfit}
            return maxProfit

        return getProfit(k, 0)

        
    def QmaxProfit(self, k: int, prices: List[int]) -> int:
        
        if not prices or k < 1:
            return 0

        # 記錄所有獲利組合
        profitData = []
        lenPrices = len(prices)
        for sell_index in range(lenPrices):
            for buy_index in range(sell_index):
                curProfit = prices[sell_index] - prices[buy_index]
                if curProfit > 0:
                    profitData.append([buy_index, sell_index, curProfit])

        # 建第一層
        dp = []
        dp.append([])
        for index in range(lenPrices):
            maxProfit = 0
            for buy_index, sell_index, profit in profitData:
                if buy_index < index:
                    continue
                if profit > maxProfit:
                    maxProfit = profit
            dp[0].append(maxProfit)

        # 建後面層數
        for layer in range(1, k):
            dp.append([])
            for index in range(lenPrices):
                maxProfit = 0
                for buy_index, sell_index, profit in profitData:
                    if buy_index < index:
                        continue
                    preLayerProfit = dp[layer-1][sell_index+1] if sell_index + 1 < lenPrices else 0        
                    curProfit = profit + preLayerProfit
                    maxProfit = curProfit if curProfit > maxProfit else maxProfit

                dp[layer].append(maxProfit)

        return dp[k-1][0]