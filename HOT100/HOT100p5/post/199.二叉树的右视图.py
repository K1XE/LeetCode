#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        q = deque([root])
        res = []
        cur = 0
        while q:
            for _ in range(len(q)):
                tmp = q.popleft()
                cur = tmp.val
                if tmp.left: q.append(tmp.left)
                if tmp.right: q.append(tmp.right)
            res.append(cur)
        return res
# @lc code=end

