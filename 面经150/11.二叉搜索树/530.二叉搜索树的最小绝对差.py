#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
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
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        pre = inf
        d = inf
        def dfs(n):
            if not n: return
            dfs(n.left)
            nonlocal pre, d
            if pre != inf: d = min(d, n.val - pre)
            pre = n.val
            dfs(n.right)
        dfs(root)
        return d
# @lc code=end

