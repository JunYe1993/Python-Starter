class Solution: 
    def longestPalindrome(self, s: str) -> str:
        
        # 利用 對稱的特性 減少 重複找最長對稱字串
        # 從左開始找 每個字元都試著對稱展開 => O(n^2)
        # 如果上一個對稱字串有覆蓋到你現今找的字元
        # 代表此字元展開的對稱字串至少 大於等於 相對於 上一個對稱字串的中心的 mirror 字元所展開的對稱字串  => O(n)

        # 在字串裡的字元中間塞入'#' 
        modified_s = ""
        for ch in s:
            modified_s += '#' + ch
        modified_s += '#'

        modified_s_len = len(modified_s)
        center = boundary = 0
        ansCenter = maxLen = 0
        p = [0]*modified_s_len
        for i in range(1, modified_s_len):
            
            # i - center = center - i_mirror
            i_mirror = center*2 - i    
            
            # i 大於 邊界 則乖乖原地對稱展開
            # i 小於 則參考對稱點, 對稱點的值有時可能與自身加起來 值超過邊界, 但這Algo只在邊界裡有效, 所以取 boundary-i
            if(i < boundary):
                p[i] = boundary-i if (boundary-i < p[i_mirror]) else p[i_mirror]
            else:
                p[i] = 0

            # 尋找展開的對稱字串
            while ( i+1+p[i] < modified_s_len and i-1-p[i] >= 0 and modified_s[i+1+p[i]] == modified_s[i-1-p[i]]):
                p[i] += 1
            
            # 邊界有更新則更新
            if(i + p[i] > boundary):
                center = i
                boundary = i + p[i]

            # 紀錄對稱字串
            if(p[i] > maxLen):                 
                maxLen = p[i]
                ansCenter = i

        print(maxLen)
        print(ansCenter)
        
        for i in range(0, modified_s_len):
            print(p[i])

        return s[(ansCenter-maxLen)//2:(ansCenter-maxLen)//2+maxLen]


ans = Solution()
print(ans.longestPalindrome("babadada"))