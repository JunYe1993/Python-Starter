# Question:
# Given a string of three different kind of brackets, ( { [, return true if the string is a valid
# brackets combination. Ex1 ({}[]) is valid Ex2 ({)} is not valid (錯開了) Ex3 (]]] is not
# valid Plus: Use as less if else as possible to do the conditional branch

# LeetCode -> Problem -> 20

import unittest

class Solution:
    def isValid(str: str) -> bool:
        
        brackets = {'[', '{', '('}
        stack = []
        
        for ch in str:

            if ch in brackets:
                stack.append(ch)

            else:
                if ch == ')' and stack != []:
                    if stack[-1] == '(':
                        stack.pop(-1)
                        continue
                    else:
                        return False

                elif ch == ']' and stack != []:
                    if stack[-1] == '[':
                        stack.pop(-1)
                        continue
                    else:
                        return False

                elif ch == '}' and stack != []:
                    if stack[-1] == '{':
                        stack.pop(-1)
                        continue
                    else:
                        return False

                else:
                    return False

        return True if stack == [] else False

class TestMethods(unittest.TestCase):

    def test_case1(self):
        spec = "({}[])"
        expect = True
        result = Solution.validBrackets(spec)
        self.assertEquals(expect, result)

    def test_case2(self):
        spec = "({)}"
        expect = False
        result = Solution.validBrackets(spec)
        self.assertEquals(expect, result)

    def test_case3(self):
        spec = "(]]]"
        expect = False
        result = Solution.validBrackets(spec)
        self.assertEquals(expect, result)

if __name__ == "__main__":
    unittest.main()