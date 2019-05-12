class Solution(object):
     def lengthOfLongestSubstring(self, s):
          """
          :type s: str
          :rtype: int
          """
          res = 0
          temp = ""
          for ch in s:
               if ch in temp:
                    if(len(temp) > res):
                         res = len(temp)
                    temp = temp[temp.index(ch)+1:]
                    temp = temp + ch
               else:
                    temp = temp + ch
          return max(res, len(temp))
               