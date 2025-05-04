#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(_pre, _in, prel, prer, inl, inr):
            if prel > prer: return None
            tmp = _pre[prel]
            node = TreeNode(tmp)
            if prel == prer: return node
            mid = -1
            for i in range(inl, inr + 1):
                if _in[i] == tmp:
                    mid = i
                    break
            prel += 1
            linl, linr, rinl, rinr = inl, mid - 1, mid + 1, inr
            lprel, lprer, rprel, rprer = prel, prel + linr - linl, prel + linr - linl + 1, prer
            node.left = dfs(_pre, _in, lprel, lprer, linl, linr)
            node.right = dfs(_pre, _in, rprel, rprer, rinl, rinr)
            return node
        return dfs(preorder, inorder, 0, len(preorder) - 1, 0, len(inorder) - 1)
    

# @lc code=end

