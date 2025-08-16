#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()
        if root: q.append(root)
        while q:
            tmp = q.popleft()
            tmp.left, tmp.right = tmp.right, tmp.left
            if tmp.left: q.append(tmp.left)
            if tmp.right: q.append(tmp.right)
        return root
        
        
# @lc code=end

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root