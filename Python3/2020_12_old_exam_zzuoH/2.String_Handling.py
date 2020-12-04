# Question:
# Important limitations:
# - Do not use any builtin functions for converting string to number.
# - Only one pass over the string is allowed - no multiple passes, so no “trim” operation
# is allowed, need to clean out spaces yourself.
# Examples:
# "I have a number 123" => 123
# "123.45" => 123.45
# "-123.45" => -123.45

import unittest

class Solution:
    def convertNumberString(target: str) -> int:
        value = None
        point = 0
        sign = 1
        
        for ch in target:
            digitC = ord(ch) - ord('0')
            if 0 <= digitC <= 9:
                if value == None:
                    sign = 1 if preC != '-' else -1
                    value = digitC*sign
                elif point > 0:
                    value += (digitC / (10**point)) * sign
                    point += 1
                else:
                    value = value*10 + digitC*sign
            elif ch == '.' and value != None and point == 0:
                point = 1
            preC = ch

        return value

class TestMethods(unittest.TestCase):
    def test_case1(self):
        spec = "I have a -number 123"
        expect = 123
        result = Solution.convertNumberString(spec)

        self.assertEqual(result, expect)
    
    def test_case2(self):
        spec = "I have a number 123.45"
        expect = 123.45
        result = Solution.convertNumberString(spec)

        self.assertEqual(result, expect)
    
    def test_case3(self):
        spec = "I have a number -123.45"
        expect = -123.45
        result = Solution.convertNumberString(spec)

        self.assertEqual(result, expect)

if __name__ == '__main__':
    unittest.main()