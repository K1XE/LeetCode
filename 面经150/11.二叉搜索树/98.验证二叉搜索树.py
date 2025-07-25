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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        f = True
        pre = inf
        def dfs(n):
            if not n: return
            dfs(n.left)
            nonlocal f, pre
            if pre != inf and pre >= n.val: f = False
            pre = n.val
            dfs(n.right)
        dfs(root)
        return f
# @lc code=end

