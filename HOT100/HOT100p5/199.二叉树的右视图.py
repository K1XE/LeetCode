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
        cnt = 0
        l = 1
        while q:
            while cnt < l:
                cur = q.popleft()
                cnt += 1
                if cnt == l: res.append(cur.val)
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
            cnt = 0
            
            l = len(q)
        return res
# @lc code=end

