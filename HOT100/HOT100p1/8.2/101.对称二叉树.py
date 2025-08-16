#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = deque([(root.left, root.right)])
        while q:
            l, r = q.popleft()
            if not l and not r: continue
            if not l or not r or l.val != r.val: return False
            q.append([l.left, r.right])
            q.append([l.right, r.left])
        return True
# @lc code=end
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(l: Optional[TreeNode], r: Optional[TreeNode]):
            if not l and r: return False
            if l and not r: return False
            if not l and not r: return True
            if l.val != r.val: return False
            b1 = dfs(l.left, r.right)
            b2 = dfs(l.right, r.left)
            return b1 and b2
        return dfs(root.left, root.right)
