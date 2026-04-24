#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res = []
        def dfs(n):
            if not n: return
            dfs(n.left)
            res.append(n.val)
            dfs(n.right)
        dfs(root)
        return res
# @lc code=end

