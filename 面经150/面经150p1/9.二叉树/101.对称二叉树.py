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
        def dfs(p, q):
            if not p and not q: return True
            elif (not p and q) or (not q and p): return False
            return p.val == q.val and dfs(p.left, q.right) and dfs(p.right, q.left)
        return dfs(root.left, root.right)
# @lc code=end

