class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        minStep = [0]
        self.dfs(X, Y, minStep)
        return minStep[0]

    def dfs(self, X, Y, minStep):
        if X == Y:
            return
        else:
            if X > Y:
                minStep[0] += X-Y
                return
            else:
                tempY = (Y//2) + (Y%2)    
                if X == tempY:
                    minStep[0] += 2 if Y % 2 else 1 
                    return
                elif X < tempY:
                    minStep[0] += 3 if Y % 2 else 2 
                    self.dfs(X*2, tempY, minStep)
                elif X > tempY:
                    minStep[0] += 3 if Y % 2 else 2
                    self.dfs(X-1, tempY, minStep)

