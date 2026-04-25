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
            x = preorder[pl]
            cur = TreeNode(x)
            if pl == pr: return cur
            pl += 1
            for mid in range(len(inorder)):
                if inorder[mid] == x: break
            lil, ril, lir, rir = il, mid - 1, mid + 1, ir
            lpl, rpl, lpr, rpr = pl, pl + ril - lil, pl + ril - lil + 1, pr
            cur.left = dfs(lpl, rpl, lil, ril)
            cur.right = dfs(lpr, rpr, lir, rir)
            return cur
        return dfs(0, len(preorder) - 1, 0, len(inorder) - 1)
            
# @lc code=end

