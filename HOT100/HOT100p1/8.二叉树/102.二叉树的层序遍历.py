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
        res = []
        q = deque()
        if root: q.append(root)
        while q:
            ans = []
            n = len(q)
            for _ in range(n):
                tmp = q.popleft()
                ans.append(tmp.val)
                if tmp.left: q.append(tmp.left)
                if tmp.right: q.append(tmp.right)
            res.append(ans)
        return res
# @lc code=end

