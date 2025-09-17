#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第 K 小的元素
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None
        def dfs(n):
            if not n: return
            dfs(n.left)
            nonlocal res, k
            k -= 1
            if k == 0: res = n.val; return
            dfs(n.right)
        dfs(root)
        return res if res != None else -1
# @lc code=end

