#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res, pack = [], []
        q = deque([root])
        while q:
            pack.clear()
            for _ in range(len(q)):
                n = q.popleft()
                pack.append(n.val)
                if n.left: q.append(n.left)
                if n.right: q.append(n.right)
            res.append(pack[:])
        return res
# @lc code=end

