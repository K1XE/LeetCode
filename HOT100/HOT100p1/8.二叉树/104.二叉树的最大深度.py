#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        return 1 + max(l, r)
# @lc code=end

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        level = 0
        if root:
            q.append(root)
        while q:
            level += 1
            n = len(q)
            for _ in range(n):
                tmp = q.popleft()
                if tmp.left: q.append(tmp.left)
                if tmp.right: q.append(tmp.right)
        return level