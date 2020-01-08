from typing import List
from collections import defaultdict

class Solution:

     # Dynamic Programming
     def minStickers(self, stickers: List[str], target: str) -> int:
          
          # 只記錄 target 出現的 ch, 藉此減少記憶體使用
          targetChars = set(target)
          
          # 做一個 stickers char counter
          stickersCounter = []
          for sticker in stickers:
               
               tempCounter = defaultdict(int)
               for ch in sticker:
                    if ch in targetChars:
                         tempCounter[ch] = sticker.count(ch)
               stickersCounter.append(tempCounter)

          # 做一個 dictionary 紀錄運算過程中的 sub target
          # 空字串回傳 0
          ans = {'': 0}
          return self.dp(ans, targetChars, stickersCounter, target)
     
     def dp(self, ans, targetChars, stickersCounter, target: str) -> int:
          
          # 先查表, 有就 return
          if target in ans:
               return ans[target]

          # 做一個 target char counter  ex. "aabbccc" => {'a':2, 'b':2, 'c':3}
          targetCounter = {}
          for ch in targetChars:
               targetCounter[ch] = target.count(ch)

          bigInteger = 1000000
          ansValue = bigInteger

          # 每次都去尋找 target 的第一個字母, 尋找可用的 sticker
          for i in range(len(stickersCounter)):

               # 沒有的 sticker 跳過
               if stickersCounter[i][target[0]] == 0:     
                    continue
               
               # 有的 sticker 紀錄扣掉 sticker 的字串
               subtarget = ''
               for ch in targetChars:
                    if targetCounter[ch] > stickersCounter[i][ch]:
                         subtarget += ch * (targetCounter[ch] - stickersCounter[i][ch])

               # 遞迴直到有表可查並返回值
               # 返回值不等於 -1, 則取最小值
               tmp = self.dp(ans, targetChars, stickersCounter, subtarget)
               if tmp != -1:
                    ansValue = min(ansValue, tmp+1) 
          
          # 若找不到匹配的 sticker, ansValue 會等於 bigInteger
          # 代表 stickers 沒有辦法拼成 target, 回傳 -1
          ans[target] = -1 if ansValue == bigInteger else ansValue
          return ans[target]

spec1 = ["with", "example", "science"]
spec2 = "thehat"

spec1 = ["these", "guess", "about", "garden", "him"]
spec2 = "atomherrr"

# spec1 = ["control","heart","interest","stream","sentence","soil","wonder","them","month","slip","table","miss","boat","speak","figure","no","perhaps","twenty","throw","rich","capital","save","method","store","meant","life","oil","string","song","food","am","who","fat","if","put","path","come","grow","box","great","word","object","stead","common","fresh","the","operate","where","road","mean"]
# spec2 = "stoodcrease"

spec1 = ["ab", "ac"]
spec2 = "aabc"

ans = Solution()
print(ans.minStickers(spec1, spec2))