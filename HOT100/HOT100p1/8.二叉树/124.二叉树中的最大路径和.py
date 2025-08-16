#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#
from typing import Optional
class TreeNode:
    def __init__(self, _val, _left, _right):
        self.val = _val
        self.left = _left
        self.right = _right
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxVal = -float('inf')
        def dfs(n):
            if not n: return 0
            l = max(dfs(n.left), 0)
            r = max(dfs(n.right), 0)
            nonlocal maxVal
            maxVal = max(maxVal, l + r + n.val)
            return max(l, r) + n.val
        dfs(root)
        return maxVal
# @lc code=end

