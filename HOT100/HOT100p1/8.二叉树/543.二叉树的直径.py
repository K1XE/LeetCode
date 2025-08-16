#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 1
        def dfs(n):
            if not n: return 0
            l = dfs(n.left)
            r = dfs(n.right)
            self.ans = max(self.ans, l + r + 1)
            return max(l, r) + 1
        dfs(root)
        return self.ans - 1
# @lc code=end

