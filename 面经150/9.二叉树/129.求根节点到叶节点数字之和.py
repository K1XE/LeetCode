#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根节点到叶节点数字之和
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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        s = []
        def dfs(n, s):
            nonlocal res
            if not n: return
            s.append(str(n.val))
            dfs(n.left, s)
            if not n.left and not n.right: res += int(''.join(s))
            dfs(n.right, s)
            s.pop()
        dfs(root, s)
        return res
# @lc code=end

