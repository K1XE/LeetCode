#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, _val, _left, _right):
        self.val = _val
        self.left = _left
        self.right = _right
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(l, r):
            if not l and not r: return True
            elif not l and r: return False
            elif l and not r: return False
            elif l.val !=r.val: return False
            b1 = dfs(l.left, r.right)
            b2 = dfs(l.right, r.left)
            return b1 and b2
        return dfs(root.left, root.right) if root else True
# @lc code=end

