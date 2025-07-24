#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#
from typing import List, Optional
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def dfs(il, ir, pl, pr):
            if pl > pr: return None
            x = postorder[pr]
            cur = TreeNode(x)
            if pl == pr: return cur
            for mid in range(il, ir + 1):
                if inorder[mid] == x: break
            pr -= 1
            d = mid - il - 1
            lpl, lpr, rpl, rpr = pl, pl + d, pl + d + 1, pr
            lil, lir, ril, rir = il, mid - 1, mid + 1, ir
            cur.left = dfs(lil, lir, lpl, lpr)
            cur.right = dfs(ril, rir, rpl, rpr)
            return cur
        return dfs(0, len(inorder) - 1, 0, len(postorder) - 1)
# @lc code=end

