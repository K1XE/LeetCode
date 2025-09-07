#
# @lc app=leetcode.cn id=662 lang=python3
#
# [662] 二叉树最大宽度
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
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        q = deque([(root, 1)])
        while q:
            res = max(res, q[-1][1] - q[0][1] + 1)
            for _ in range(len(q)):
                node, i = q.popleft()
                if node.left: q.append((node.left, 2 * i))
                if node.right: q.append((node.right, 2 * i + 1))
        return res
# @lc code=end

