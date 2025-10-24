#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#
from mytools import *
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(n, p, q):
            if not n: return None
            if n == p or n == q: return n
            l = dfs(n.left, p, q)
            r = dfs(n.right, p, q)
            if l and r: return n
            return l if l else r
        return dfs(root, p, q)
            
# @lc code=end

