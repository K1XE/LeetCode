#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
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
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def get_h(n):
            h = 0
            while n: h += 1; n = n.left
            return h
        if not root: return 0
        l = get_h(root.left); r = get_h(root.right)
        if l == r: return (1 << l) + self.countNodes(root.right)
        else: return (1 << r) + self.countNodes(root.left)
# @lc code=end

