#
# @lc app=leetcode.cn id=427 lang=python3
#
# [427] 建立四叉树
#
from mytools import *
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
# @lc code=start
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        isLeaf = self.isQuadTree(grid)
        l = len(grid)
        if isLeaf == None:
            mid = l // 2
            tl = [[grid[i][j] for j in range(mid)] for i in range(mid)]
            tr = [[grid[i][j] for j in range(mid, l)] for i in range(mid)]
            dl = [[grid[i][j] for j in range(mid)] for i in range(mid, l)]
            dr = [[grid[i][j] for j in range(mid, l)] for i in range(mid, l)]
            node = Node(True, False, self.construct(tl), self.construct(tr), self.construct(dl), self.construct(dr))
        elif isLeaf == True:
            node = Node(True, True, None, None, None, None)
        else:
            node = Node(False, True, None, None, None, None)
        return node
    def isQuadTree(self, grid):
        l = len(grid)
        s = 0
        for i in range(l): s += sum(grid[i])
        if s == l ** 2: return True
        elif s == 0: return False
        else: return None
# @lc code=end

