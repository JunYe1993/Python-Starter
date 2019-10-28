from typing import List

class Solution:
     def beautifulArray(self, N: int) -> List[int]:
          
          # A[k] * 2 != A[i] + A[j]

          # 1. 可以做線性變化

               # A[k] * 2 + 2 !=  ==> (A[k] + 1) * 2 != (A[i] + 1) + (A[j] + 1)
               # E.g. [1, 3, 2] = Beautiful Array ==> [2, 4, 3] = Beautiful Array
               
               # A[k] * 2 * x != (A[i] + A[j]) * x ==> (A[k] * x) != (A[i] * x) + (A[j] * x)
               # E.g. [1, 3, 2] = Beautiful Array ==> [2, 6, 4] = Beautiful Array

          # 2. A[k] * 2 = 偶數

               # 只要 A[i] A[j] 一奇一偶 則不等式恆成立 

          # 3. Divide and Conquer

               # [1, 3, 2] = Beautiful Array
               # (n in [1, 3, 2]) * 2 - 1 = [1, 5, 3] = Beautiful Array
               # (n in [2, 6, 4]) * 2 = [2, 6, 4] = Beautiful Array
               # [1, 5, 3, 2, 6, 4] = Beautiful Array

          ans = {1:[1]}
          return self.dp(ans, N)

     def dp(self, ans, N) -> List[int]:
          
          if N not in ans:
               
               if N % 2 == 1:
                    left = self.dp(ans, (N+1)//2)
                    right = self.dp(ans, N//2)
               else:
                    left = right = self.dp(ans, N//2)
               
               ans[N] = [2*x-1 for x in left] + [2*x for x in right]

          return ans[N]

     def checkBeautifulArray(self, arr: List[int]) -> bool:

          ans = True
          N = len(arr)
          for i in range(N):
               for k in range(i+1, N):
                    for j in range(k+1, N):
                         if arr[k]*2 == arr[i]+arr[j]:
                              print("i =", arr[i], "k =", arr[k], "j =", arr[j])
                              ans = False
          
          return ans

ans = Solution()
temp = ans.beautifulArray(18)
print(temp)
print(ans.checkBeautifulArray(temp))
# print(ans.checkBeautifulArray([1, 17, 9, 13, 5, 11, 3, 15, 7, 10, 2, 18, 6, 14, 4, 16, 12, 8]))
