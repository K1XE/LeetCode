#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#
from mytools import *
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        res = 0
        q = deque([root])
        while q:
            for _ in range(len(q)):
                n = q.popleft()
                if n.left: q.append(n.left)
                if n.right: q.append(n.right)
            res += 1
        return res
# @lc code=end

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(n: Optional[TreeNode]):
            nonlocal res
            if not n: return 0
            l = dfs(n.left)
            r = dfs(n.right)
            res = max(res, max(l, r) + 1)
            return max(l, r) + 1
        dfs(root)
        return res