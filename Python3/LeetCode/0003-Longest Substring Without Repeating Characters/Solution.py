from typing import List
class Solution:
     def lengthOfLongestSubstring(self, s: str) -> int:
          curMax = 0                                   # 紀錄 不重複字串長度最大值
          temps = ""                                   # 宣告一個 string 紀錄 當前不重複字串
          for ch in s:
               if ch in temps:                         # 若 當前字元 出現在 當前不重複字串
                    if(len(temps) > curMax):           # 當前不重複字串 長度大於 不重複字串長度最大值 則更新 不重複字串長度最大值
                         curMax = len(temps)
                    temps = temps[temps.index(ch)+1:]  #
                    temps = temps + ch
               else:
                    temps = temps + ch
          return max(len(temps), curMax)
