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
        stk = []
        res = []
        if root: stk.append((root, 0))
        while stk:
            n, vis = stk.pop()
            if vis:
                res.append(n.val)
                continue
            if n.right: stk.append((n.right, 0))
            stk.append((n, 1))
            if n.left: stk.append((n.left, 0))
        return res
# @lc code=end
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stk = []
        res = []
        q = root
        while stk or q:
            while q:
                stk.append(q)
                q = q.left
            q = stk.pop()
            res.append(q.val)
            q = q.right
        return res
