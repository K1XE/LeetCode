#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#
from typing import Optional, List
from collections import deque
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()
        if not root: return res
        q.append(root)
        while q:
            n = len(q)
            for i in range(n):
                tmp = q.popleft()
                if tmp.left: q.append(tmp.left)
                if tmp.right: q.append(tmp.right)
                if i == n - 1: res.append(tmp.val)
        return res

# @lc code=end

