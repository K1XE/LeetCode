#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
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
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        n = root
        while n:
            if n.left:
                tmp = n.right
                l = n.left
                while l.right:
                    l = l.right
                l.right = tmp
                n.right = n.left
                n.left = None
            n = n.right
        return root
                
# @lc code=end

