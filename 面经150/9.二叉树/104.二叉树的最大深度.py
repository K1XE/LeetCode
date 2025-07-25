#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(n):
            if not n: return 0
            l = dfs(n.left)
            r = dfs(n.right)
            return max(l, r) + 1
        return dfs(root)
# @lc code=end

