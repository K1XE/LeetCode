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
            mid = (l + r) // 2
            node = TreeNode(nums[mid])
            ll = l
            lr = mid - 1
            rl = mid + 1
            rr = r
            node.left = dfs(ll, lr)
            node.right = dfs(rl, rr)
            return node
        return dfs(0, len(nums) - 1)
# @lc code=end

