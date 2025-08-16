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
        pre = -inf
        cur = None
        ok = True
        def dfs(n: Optional[TreeNode]):
            nonlocal pre, cur, ok
            if not n: return None
            dfs(n.left)
            cur = n.val
            if cur <= pre: ok = False
            pre = cur
            dfs(n.right)
        dfs(root)
        return ok
# @lc code=end

