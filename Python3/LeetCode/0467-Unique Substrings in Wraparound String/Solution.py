class Solution:
     def findSubstringInWraproundString(self, p: str) -> int:
          
          # 建一個 Map 紀錄每個字母最長字串
          map = {}
          for ch in "abcdefghijklmnopqrstuvwxyz":
               map[ch] = 0
          
          # 跑整條字串
          strlen = len(p)
          i = 0
          while i < strlen:
               # 字串長度 init 1
               sublen = 1
               for j in range(i, strlen):
                    # 若字元非最後一個
                    if(j < strlen-1):
                         # 計算是否連號 或 za, 是則長度++, 否則結算並跳出迴圈
                         validate = ord(p[j])+1-ord(p[j+1])
                         if(validate == 0 or validate == 26):
                              sublen += 1
                         else:
                              # 結算長度若等於 3 且起始字元等於 a, 則可推 map['a'] = 3, 再推 map['b'] = 2, map['c'] = 1
                              # 但如果遇到原本的值比較大的, 則直接跳出迴圈不再儲存, 因為依照特性後面原本的值也會比較大
                              for k in range(0, sublen if (sublen < 26) else 26):
                                   curchr = chr(ord('a')+(26+ord(p[i])+k-ord('a'))%26)
                                   if(map[curchr] < sublen - k):
                                        map[curchr] = sublen - k
                                   else:
                                        break
                              # 讓 iterator 跳到結算字元的下一個
                              i = j+1 if(j > i) else i+1
                              break
                    else:   
                         # 若字為最後一個則結算, 同上
                         for k in range(0, sublen if (sublen < 26) else 26):
                              curchr = chr(ord('a')+(26+ord(p[i])+k-ord('a'))%26)
                              if(map[curchr] < sublen - k):
                                   map[curchr] = sublen - k
                              else:
                                   break
                         i = j+1 if(j > i) else i+1
                         break

          # 把 map 裡的值全加起來
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