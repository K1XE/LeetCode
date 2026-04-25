#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        def dfs(l, r):
            if not l and not r: return True
            if (not l and r) or (l and not r): return False
            return dfs(l.left, r.right) and dfs(l.right, r.left) and l.val == r.val
        return dfs(root.left, root.right)
# @lc code=end

