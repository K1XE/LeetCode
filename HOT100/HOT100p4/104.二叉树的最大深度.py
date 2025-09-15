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
        res = 0
        def dfs(n):
            if not n: return 0
            l = dfs(n.left)
            r = dfs(n.right)
            nonlocal res
            res = max(res, 1 + l, 1 + r)
            return 1 + max(l, r)
        dfs(root)
        return res
# @lc code=end

