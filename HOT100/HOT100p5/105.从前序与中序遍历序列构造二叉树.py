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
        def dfs(preo, ino, pl, pr, il, ir):
            if pl > pr: return None
            tmp = preo[pl]
            n = TreeNode(tmp)
            if pl == pr: return n
            pl += 1
            for i in range(il, ir + 1):
                if ino[i] == tmp: break
            lil = il
            ril = i - 1
            lir = i + 1
            rir = ir
            lpl = pl
            rpl = lpl + ril - lil
            lpr = rpl + 1
            rpr = pr
            n.left = dfs(preo, ino, lpl, rpl, lil, ril)
            n.right = dfs(preo, ino, lpr, rpr, lir, rir)
            return n
        return dfs(preorder, inorder, 0, len(preorder) - 1, 0, len(inorder) - 1)
            
            
# @lc code=end

