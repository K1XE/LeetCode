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
        q = deque([root])
        res = []
        while q:
            cur = []
            for _ in range(len(q)):
                tmp = q.popleft()
                cur.append(tmp.val)
                if tmp.left: q.append(tmp.left)
                if tmp.right: q.append(tmp.right)
            res.append(cur)
        return res
# @lc code=end

