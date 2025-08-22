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
        def dfs(lp, rp, li, ri):
            if lp > rp: return None
            x = preorder[lp]
            cur = TreeNode(x)
            if lp == rp: return cur
            for mid in range(li, ri + 1):
                if inorder[mid] == x: break
            lp += 1
            gap = mid - li - 1
            lpl, lpr, rpl, rpr = lp, lp + gap, lp + gap + 1, rp
            lil, lir, ril, rir = li, mid - 1, mid + 1, ri
            cur.left = dfs(lpl, lpr, lil, lir)
            cur.right = dfs(rpl, rpr, ril, rir)
            return cur
        return dfs(0, len(preorder) - 1, 0, len(inorder) - 1)
# @lc code=end

