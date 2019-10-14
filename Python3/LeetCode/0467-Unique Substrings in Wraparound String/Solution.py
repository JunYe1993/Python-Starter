class Solution:
     def findSubstringInWraproundString(self, p: str) -> int:
          map = {}

          for ch in "abcdefghijklmnopqrstuvwxyz":
               map[ch] = 0
          
          strlen = len(p)
          i = 0
          while i < strlen:
               #print(i)
               sublen = 1
               for j in range(i, strlen):
                    if(j < strlen-1):
                         validate = ord(p[j])+1-ord(p[j+1])
                         if(validate == 0 or validate == 26):
                              sublen += 1
                         else:
                              for k in range(0, sublen if (sublen < 26) else 26):
                                   curchr = chr(ord('a')+(26+ord(p[i])+k-ord('a'))%26)
                                   if(map[curchr] < sublen - k):
                                        map[curchr] = sublen - k
                                   else:
                                        break
                              i = j+1 if(j > i) else i+1
                              break
                    else:   
                         for k in range(0, sublen if (sublen < 26) else 26):
                              curchr = chr(ord('a')+(26+ord(p[i])+k-ord('a'))%26)
                              if(map[curchr] < sublen - k):
                                   map[curchr] = sublen - k
                              else:
                                   break
                         i = j+1 if(j > i) else i+1
                         break

          ans = 0
          for ch in "abcdefghijklmnopqrstuvwxyz":
               #print(ch, "=", map[ch])
               ans += map[ch]
          return ans

ans = Solution()
spec = "zab"
spec = "abcdefghijklmnopqrstuvwxyza"
spec = "studefghijklmnojklmnopqrstuabcdefghijklmnopqrstufgefghdefghijmnoprstuvwxabcdefghijklmnopqrstuvw"
# spec = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
# spec = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
print(ans.findSubstringInWraproundString(spec))
# print(ans.test(spec))