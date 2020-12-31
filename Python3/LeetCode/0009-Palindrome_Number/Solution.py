class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False

        num, mirrorx = x, 0
        while num > 0:
            mirrorx = mirrorx*10 + num%10
            num = num // 10
        
        return x == mirrorx