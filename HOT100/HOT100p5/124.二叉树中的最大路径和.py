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
        hash = defaultdict(int)
        hash[0] = 1
        s = -inf
        def dfs(n):
            nonlocal s
            if not n: return 0
            l = max(0, dfs(n.left))
            r = max(0, dfs(n.right))
            s = max(s, n.val + l + r)
            return n.val + max(l, r)
        dfs(root)
        return s
# @lc code=end

