#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
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
    def __init__(self):
        self.pre = -float('inf')
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(n):
            if not n: return True
            b1 = dfs(n.left)
            if n.val <= self.pre: return False
            self.pre = n.val
            b2 = dfs(n.right)
            return b1 and b2
        return dfs(root)
# @lc code=end

