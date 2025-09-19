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
        hash = defaultdict(int)
        hash[0] = 1
        res = 0
        s = 0
        def dfs(n):
            if not n: return None
            nonlocal res, targetSum, s
            s += n.val
            res += hash[s - targetSum]
            hash[s] += 1
            dfs(n.left)
            dfs(n.right)
            hash[s] -= 1
            s -= n.val
        dfs(root)
        return res
# @lc code=end

