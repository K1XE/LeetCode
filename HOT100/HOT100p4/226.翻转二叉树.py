#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(n):
            if not n: return n
            if not n.left and not n.right: return n
            n.left, n.right = n.right, n.left
            dfs(n.left)
            dfs(n.right)
            return n
        dfs(root)
        return root
# @lc code=end

