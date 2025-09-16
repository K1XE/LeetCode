#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(l, r):
            if l > r: return None
            mid = l + r >> 1
            nonlocal nums
            cur = TreeNode(val=nums[mid])
            cur.left = dfs(l, mid - 1)
            cur.right = dfs(mid + 1, r)
            return cur
        return dfs(0, len(nums) - 1)
# @lc code=end

