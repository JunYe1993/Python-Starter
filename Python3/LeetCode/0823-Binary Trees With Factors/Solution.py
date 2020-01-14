from typing import List
class Solution:
     def numFactoredBinaryTrees_alpha(self, A: List[int]) -> int:
          
          # 雙回圈跑完所有組合，Backtracking 所以先 Sort 運算小的組合值
          # 內外圈相乘 數值若不同 再 * 2 
          dp = {}
          A.sort()
          Alen = len(A)
          
          for mainIndex in range(Alen) :
               dp[A[mainIndex]] = dp.get(A[mainIndex], 0) + 1
               
               for subIndex in range(0, mainIndex + 1) :

                    target = A[mainIndex] * A[subIndex]

                    if target in A :
                         dp[target] = dp.get(target, 0) + dp[A[mainIndex]] * dp[A[subIndex]] * ( 2 if mainIndex != subIndex else 1 )

                    # 加速運算，大於 List 最大值則沒意義繼續運算下去
                    if target > A[-1] : break
          
          count = 0
          for val in A :
               count += dp[val]

          return count

     def numFactoredBinaryTrees_beta(self, A: List[int]) -> int :

          # 直接在 Backtracking 的 Map 找，不再去浪費時間判斷是否在 List 裡
          # Map 數值不同會自己再重複運算到，所以不用 * 2
          dp = {}
          A.sort()
          for curVal in A : 
               subSum = 0
               for dpKey in dp :
                    if curVal % dpKey == 0 :
                         subSum += dp.get(curVal//dpKey, 0) * dp[dpKey]

               dp[curVal] = subSum + 1

          return sum(dp.values()) % (10**9 + 7)