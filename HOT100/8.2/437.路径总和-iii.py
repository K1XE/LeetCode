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
        res = 0
        hash = defaultdict(int)
        hash[0] = 1
        def dfs(n: Optional[TreeNode], val):
            if not n: return
            val += n.val
            nonlocal res
            res += hash[val - targetSum]
            hash[val] += 1
            dfs(n.left, val)
            dfs(n.right, val)
            hash[val] -= 1
        dfs(root, 0)
        return res

# @lc code=end

