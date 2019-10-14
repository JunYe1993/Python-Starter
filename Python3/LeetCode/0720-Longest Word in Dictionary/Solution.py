from typing import List
class Solution:
     def longestWord(self, words: List[str]) -> str:
          ans = ""
          wordset = set(words)
          for word in words:
               if len(word) > len(ans) or (len(word) == len(ans) and word < ans):
                    if all(word[:i] in wordset for i in range(1, len(word))):
                         print(word)
                         ans = word
          return ans

ans = Solution()
print(ans.longestWord(["w","wo","wor","worl","world"]))