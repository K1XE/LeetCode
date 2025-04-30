#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#
from typing import List, Optional
class TreeNode:
    def __init__(self, x, l, r):
        self.val = x
        self.left = l
        self.right = r
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, preo, ino, prel, prer, inl, inr):
        if prel > prer: return None
        tmp = preo[prel]
        u = TreeNode(tmp)
        if prel == prer: return u
        mid = 0
        for i in range(inl, inr + 1):
            if ino[i] == tmp:
                mid = i
                break
        linl, linr, rinl, rinr = inl, mid - 1, mid + 1, inr
        prel += 1
        lprel, lprer, rprel, rprer = prel, prel + linr - linl, prel + linr - linl + 1, prer
        u.left = self.dfs(preo, ino, lprel, lprer, linl, linr)
        u.right = self.dfs(preo, ino, rprel, rprer, rinl, rinr)
        return u
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.dfs(preorder, inorder, 0, len(preorder) - 1, 0, len(inorder) - 1)
# @lc code=end

