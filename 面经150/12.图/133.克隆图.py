#
# @lc app=leetcode.cn id=133 lang=python3
#
# [133] 克隆图
#
from typing import Optional
from collections import *
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not  None else []
# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        q = deque([node])
        vis = {}
        while q:
            tmp = q.popleft()
            if tmp not in vis:
                vis[tmp] = Node(tmp.val)
            for y in tmp.neighbors:
                if y not in vis:
                    vis[y] = Node(y.val)
                    q.append(y)
                vis[tmp].neighbors.append(vis[y])
        return vis[node]
# @lc code=end

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        vis = {}
        def dfs(x):
            if x in vis:
                return vis[x]
            tmp = Node(x.val)
            vis[x] = tmp
            for y in x.neighbors:
                tmp.neighbors.append(dfs(y))
            return tmp
        return dfs(node)