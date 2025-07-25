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
            if not n: return
            l = dfs(n.left)
            r = dfs(n.right)
            n.left = r
            n.right = l
            return n
        return dfs(root)
# @lc code=end

