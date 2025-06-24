#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -inf
        def dfs(n: Optional[TreeNode]):
            nonlocal res
            if not n: return 0
            l = dfs(n.left)
            r = dfs(n.right)
            res = max(res, n.val + max(0, l) + max(0, r))
            return n.val + max(0, l, r)
        dfs(root)
        return res
# @lc code=end

