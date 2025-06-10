#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
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
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(n: Optional[TreeNode]):
            if not n: return [0, 0]
            leftdp = dfs(n.left)
            rightdp = dfs(n.right)
            rob = n.val + leftdp[0] + rightdp[0]
            not_rob = max(leftdp[0], leftdp[1]) + max(rightdp[0], rightdp[1])
            return [not_rob, rob]
        return max(dfs(root))
# @lc code=end

