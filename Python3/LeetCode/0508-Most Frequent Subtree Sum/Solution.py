from collections import defaultdict
from typing import List

class TreeNode:
     def __init__(self, x):
          self.val = x
          self.left = None
          self.right = None

class Solution:
     
     def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
          
          # 宣告 dict 紀錄所有 sum 的次數
          # 宣告 list 記錄所有等同 max 次數的 sum 值
          nodesGroup = defaultdict(int)
          maxGroup = []

          # 防 root 為[]
          if root: self.recur(root, nodesGroup, maxGroup)
          return maxGroup

     def recur(self, node: TreeNode, nodesGroup: dict, maxGroup: list):
          
          # sum 值 先加自己本身
          treesum = node.val

          # 左邊有加左邊, 右邊有加右邊
          if node.left: treesum += self.recur(node.left, nodesGroup, maxGroup)
          if node.right: treesum += self.recur(node.right, nodesGroup, maxGroup)
          
          # 有 defaultdict(int) 所以預設值是 0, 可以直接操作++
          nodesGroup[treesum] += 1

          # 若大於當前 max 值則刷新 max 值, 清空 maxGroup, 最後加上新 sum 值
          if nodesGroup[treesum] > nodesGroup['max']:
               nodesGroup['max'] = nodesGroup[treesum]
               while maxGroup : maxGroup.pop()
               maxGroup.append(treesum)
          
          # 若等於 max 值 則將新 sum 值加入 maxGroup
          elif nodesGroup[treesum] == nodesGroup['max']:
               maxGroup.append(treesum)

          return treesum