#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
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
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([root])
        res = []
        while q:
            n = len(q)
            s = 0
            for _ in range(n):
                tmp = q.popleft()
                s += tmp.val
                if tmp.left: q.append(tmp.left)
                if tmp.right: q.append(tmp.right)
            res.append(s / n)
        return res
# @lc code=end

