#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第 K 小的元素
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = -1
        def dfs(n):
            if not n: return
            dfs(n.left)
            nonlocal k, res
            if k == 1: res = n.val
            k -= 1
            dfs(n.right)
        dfs(root)
        return res
# @lc code=end

