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
        
        def dfs(pl, pr, il, ir):
            if pl > pr: return None
            tmp = preorder[pl]
            node = TreeNode(tmp)
            if pl == pr: return node
            mid = -1
            for i in range(il, ir + 1):
                if inorder[i] == tmp:
                    mid = i
                    break
            pl += 1
            lil, lir, ril, rir = il, mid - 1, mid + 1,ir
            lpl, lpr, rpl, rpr = pl, pl + lir - lil, pl + lir - lil + 1, pr
            node.left = dfs(lpl, lpr, lil, lir)
            node.right = dfs(rpl, rpr, ril, rir)
            return node
        return dfs(0, len(preorder) - 1, 0, len(inorder) - 1)
# @lc code=end

