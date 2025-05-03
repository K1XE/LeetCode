#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
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
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(n):
            if not n: return
            if n.left:
                tmp = n.right
                n.right = n.left
                n.left = None
                u = n
                while u.right:
                    u = u.right
                u.right = tmp
            dfs(n.right)
        return dfs(root)
# @lc code=end

