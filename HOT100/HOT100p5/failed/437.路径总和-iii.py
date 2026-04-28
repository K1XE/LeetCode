#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        h = defaultdict(int)
        h[0] = 1
        s = 0
        res = 0
        def dfs(n):
            nonlocal s, res, targetSum
            if not n: return 0
            s += n.val
            res += h[s - targetSum]
            h[s] += 1
            dfs(n.left)
            dfs(n.right)
            h[s] -= 1
            s -= n.val
        dfs(root)
        return res
# @lc code=end

