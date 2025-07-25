#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = deque([root])
        res = []
        f = True
        while q:
            n = len(q)
            pack = deque()
            for _ in range(n):
                tmp = q.popleft()
                if f: pack.append(tmp.val)
                else: pack.appendleft(tmp.val)
                if tmp.left: q.append(tmp.left)
                if tmp.right: q.append(tmp.right)
            f = not f
            res.append(list(pack))
        return res 
# @lc code=end

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = deque([root])
        res = []
        f = True
        while q:
            n = len(q)
            pack = []
            for _ in range(n):
                tmp = q.popleft()
                pack.append(tmp.val)
                if tmp.left: q.append(tmp.left)
                if tmp.right: q.append(tmp.right)
            res.append(pack) if f else res.append(list(reversed(pack)))
            f = not f
        return res 