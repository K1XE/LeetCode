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
        stk = [(root, False)]
        while stk:
            n, f = stk.pop()
            if f: res.append(n.val); continue
            if n.right: stk.append((n.right, False))
            stk.append((n, True))
            if n.left: stk.append((n.left, False))
        return res
    
# @lc code=end

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(n):
            if not n: return n
            nonlocal res
            dfs(n.left)
            res.append(n.val)
            dfs(n.right)
        dfs(root)
        return res