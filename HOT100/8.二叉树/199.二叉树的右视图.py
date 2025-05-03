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
        res = []
        def dfs(n, depth):
            if not n: return
            if depth == len(res):
                res.append(n.val)
            dfs(n.right, depth + 1)
            dfs(n.left, depth + 1)
        dfs(root, 0)
        return res


# @lc code=end
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        res = []
        if root: q.append(root)
        while q:
            n = len(q)
            for _ in range(len(q)):
                n -= 1
                tmp = q.popleft()
                if tmp.left: q.append(tmp.left)
                if tmp.right: q.append(tmp.right)
                if n == 0: res.append(tmp.val)
        return res
