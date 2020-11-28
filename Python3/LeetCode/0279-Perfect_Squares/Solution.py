class Solution:
     def numSquares(self, n: int) -> int:
          
          # 從上往下
          squareMap = []
          squareBase = 1
          square = squareBase * squareBase
          while square <= n:
               squareMap.append(square)
               squareBase += 1
               square = squareBase * squareBase

          layerCount = 0
          curLayerNumbers = {n}
          while curLayerNumbers:
               layerCount += 1
               nextLayerNumbers = set()
               for curNumber in curLayerNumbers:
                    for square in squareMap:
                         if square == curNumber:
                              return layerCount
                         elif square > curNumber:
                              break
                         else:
                              nextLayerNumbers.add(curNumber-square)
                    curLayerNumbers = nextLayerNumbers
          return 0
     
     def QnumSquares(self, n: int) -> int:

          # 從下往上
          squareMap = []
          squareBase = 1
          square = squareBase * squareBase
          while square <= n:
               squareMap.append(square)
               squareBase += 1
               square = squareBase * squareBase


          dp = [0]
          for nIndex in range(1, n+1):
               curMin = 1000000000

               for curSquare in squareMap:
                    if curSquare <= nIndex:
                         curMin = min(dp[nIndex-curSquare]+1, curMin)
               dp.append(curMin)
          return dp[n]

     # 4800ms
     def numSquares_alpha(self, n: int) -> int:
          
          # 建立所有的最佳解 map 堆疊到 n 
          dp = [0]
          for nIndex in range(1, n+1):        
               curMax = 1000000000
               
               cur = 1
               curSquares = cur * cur
               while curSquares <= nIndex :
                    curMax = min(dp[nIndex - curSquares]+1, curMax)
                    cur += 1
                    curSquares = cur * cur
               
               dp.append(curMax)

          return dp[n]

     # 4000ms
     def numSquares_beta(self, n: int) -> int:
          
          # 把平方拉出來一次計算 然後建表
          squareList = []
          squareNum = 1
          while squareNum*squareNum <= n :
               squareList.append(squareNum*squareNum)
               squareNum += 1

          dp = [0]
          for nIndex in range(1, n+1):        
               curMax = 1000000000
               for square in squareList : 
                    if square > nIndex : break
                    curMax = min(dp[nIndex-square] + 1, curMax)
               dp.append(curMax)

          return dp[n]

     # 200ms
     def numSquares_gama(self, n: int) -> int:

          # main idea = 只找想要的，因為剩餘的值若剛好等於任一平方則為最佳解 ( BFS )
          # n = 13 會找 n = 4, n = 9, n = 12 => Done.
          # n = 12 會找 n = 3, n = 8, n = 11 => (n = 2), (n = 4, n = 7), (n = 2, n = 7, n = 10) => Done.
          squareList = []
          squareNum = 1
          while squareNum*squareNum <= n :
               squareList.append(squareNum*squareNum)
               squareNum += 1

          layerCount = 0
          layerChoice = {n}
          while layerChoice :
               layerCount += 1
               nextLayerChoice = set()
               for choice in layerChoice :
                    for square in squareList :
                         if square == choice :
                              return layerCount
                         if square > choice : 
                              break
                         nextLayerChoice.add(choice-square)
               layerChoice = nextLayerChoice
          
          return 0

     # 32ms
     def numSquares_godTier(self, n: int) -> int:

          # https://zh.wikipedia.org/wiki/%E5%9B%9B%E5%B9%B3%E6%96%B9%E5%92%8C%E5%AE%9A%E7%90%86
          # 四平方和定理，任一正整數可為 4 個整數的平方和
          # ......

          pass