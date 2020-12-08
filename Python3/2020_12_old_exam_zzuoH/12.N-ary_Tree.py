# Question
# 給定一個N-ary tree,找出出現在最多不同 levels 的元素
# a 出現在 level 1 和 2 ,b 和c 只出現在2 所以答案是 a
# ex: a 
#    / \\
#   a   bc

from typing import List
from collections import defaultdict
import unittest

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        answer = []
        curlevel = 1
        levelnodeCount = defaultdict(int)
        levelnodeCount[0] = 1
        answer.append([])
        for element in root:
            if element != null:
                answer[curlevel-1].append(element)
                levelnodeCount[curlevel] += 1
            else:
                levelnodeCount[curlevel-1] -= 1
                if levelnodeCount[curlevel-1] == 0:
                    answer.append([])
                    curlevel += 1

        return answer


class TestMethods(unittest.TestCase):
    
    def test_case1(self):
        testcase = Solution()
        root = [1,null,3,2,4,null,5,6]
        expect = [[1],[3,2,4],[5,6]]
        result = testcase.levelOrder(root)
        self.assertEquals(expect, result)
    
    def test_case2(self):
        testcase = Solution()
        root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
        expect = [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
        result = testcase.levelOrder(root)
        self.assertEquals(expect, result)

if __name__ == "__main__":
    unittest.main()