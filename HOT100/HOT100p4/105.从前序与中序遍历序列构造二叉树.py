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
            cur = TreeNode(val=x)
            if pl == pr: return cur
            for mid in range(il, ir + 1):
                if inorder[mid] == x: break
            lil, lir, ril, rir = il, mid - 1, mid + 1, ir
            l_ = lir - lil + 1
            pl += 1
            lpl, lpr, rpl, rpr = pl, pl + l_ - 1, pl + l_, pr
            cur.left = dfs(lpl, lpr, lil, lir)
            cur.right = dfs(rpl, rpr, ril, rir)
            return cur
        return dfs(0, len(preorder) - 1, 0, len(inorder) - 1)

# @lc code=end

