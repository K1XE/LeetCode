#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#
from mytools import *
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = None
        self.right = None
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        def dfs(n: TreeNode):
            if not n: return 0
            l = max(0, dfs(n.left))
            r = max(0, dfs(n.right))
            self.res = max(self.res, l + r + n.val)
            return max(l, r) + n.val
        dfs(root)
        return self.res
# @lc code=end

